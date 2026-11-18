"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Vòng 1: đối chiếu nguồn sự thật, kiểm tra quyền ghi và giới hạn thiệt hại.
"""
from . import helpers as H
from .tools import Verdict


def pre_guard(ctx):
    """Ghim chính sách theo ngày; trả về người khi thiếu dữ kiện gốc."""
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("không có chính sách hiệu lực cho ngày xử lý")
    order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
    if order is None or order.get("customer_id") != ctx.ticket.get("customer_id"):
        return Verdict.escalate("không tìm thấy đơn hoặc người gửi không phải chủ đơn")
    parcels = order.get("parcels") or []
    if not parcels or (ctx.ticket.get("parcel_id") and not any(
            p.get("parcel_id") == ctx.ticket["parcel_id"] for p in parcels)):
        return Verdict.escalate("thiếu kiện hàng hoặc mã kiện không thuộc đơn")
    # Chừa tiền cho cả policy check (kể cả retry), confirm và ghi chú, không chỉ phần đọc chữ.
    prices = ctx.tools.ops_facts().get("llm_cost", {})
    texts = [ctx.ticket.get("text", "")]
    if order.get("checkout_note"):
        texts.append(order["checkout_note"])
    forecast = (ctx.cost_vnd
                + sum(prices.get("extract_base_vnd", 0) + len(text) // 4 * prices.get("extract_per_4_chars_vnd", 0)
                      for text in texts)
                + 2 * prices.get("policy_check_vnd", 0) + prices.get("confirm_vnd", 0)
                + (prices.get("decision_note_vnd", 0) if ctx.gates.get("operations", {}).get("decision_note") else 0))
    budgets = [ctx.gates.get("business", {}).get("cost_budget_per_ticket_vnd"),
               ctx.tools.ops_limits().get("max_llm_cost_per_ticket_vnd")]
    if any(forecast > cap for cap in budgets if cap is not None):
        ctx.log("llm_budget_reserved", forecast_vnd=forecast)
        return Verdict.escalate("dự toán cả luồng vượt trần tiền máy: chuyển người trước khi gọi model")
    ctx.log("policy_pinned", policy_id=policy["policy_id"], as_of=ctx.as_of)
    return Verdict.allow(policy_id=policy["policy_id"])


def _facts(ctx):
    order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if not order or not policy or not order.get("parcels"):
        return None
    try:
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay = H.db_delay_days(parcel, ctx.as_of)
        amount = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
    except (KeyError, TypeError, ValueError):
        return None
    return order, policy, parcel, delay, amount


def _approval_ok(ctx, action, order):
    candidates = ctx.tools.lookup_approvals(approval_id=action.get("approval_id"))
    if len(candidates) != 1:
        return False
    approval = candidates[0]
    approver = ctx.gates.get("operations", {}).get("approver_id")
    try:
        return (approval.get("status") == "valid"
                and approval.get("ticket_id") == ctx.ticket["ticket_id"]
                and approval.get("order_id") == order["order_id"]
                and approval.get("customer_id") == order["customer_id"]
                and bool(approval.get("approver_id"))
                and (not approver or approval["approver_id"] == approver)
                and H.d(approval["expires_at"]) >= H.d(ctx.as_of)
                and approval["max_vnd"] >= action["amount_vnd"]
                and not ctx.tools.ledger_rows(approval_id=approval["approval_id"]))
    except (KeyError, TypeError, ValueError):
        return False


def write_gate(ctx, action):
    facts = _facts(ctx)
    if facts is None:
        return Verdict.escalate("không đủ dữ kiện DB để kiểm tra lệnh ghi")
    order, policy, parcel, delay, entitlement = facts
    tool = action.get("tool")
    extracted = next((e for e in ctx.events if e.get("type") == "llm_extract"), {})

    # Cổng 1: chữ khách là dữ liệu; không để nó thay thế tracking DB.
    claimed = extracted.get("claimed_delay_days")
    if extracted.get("intent") == "LATE" and claimed is not None and claimed != delay:
        ctx.log("claim_db_mismatch", claimed=claimed, db=delay)
        return Verdict.escalate("số ngày khách khai khác tracking DB: cần người đối chiếu")

    if tool == "issue_refund":
        if action.get("order_id") != order["order_id"] or action.get("ticket_id") != ctx.ticket["ticket_id"]:
            return Verdict.escalate("lệnh hoàn không thuộc đơn và ticket đang xử lý")
        # Retry sau khi tiền đã ghi phải bỏ riêng lệnh ghi lặp, không chuyển người sau khi đã trả tiền.
        if any(e.get("type") == "tool" and e.get("tool") == "issue_refund" for e in ctx.events):
            return Verdict.deny("đã ghi hoàn thành công trong lượt này; bỏ lệnh retry")
        rows = ctx.tools.ledger_rows(order_id=order["order_id"])
        already_paid = sum(r.get("amount_vnd", 0) for r in rows)
        remaining = entitlement - already_paid
        if rows and remaining <= 0:
            ctx.log("duplicate_refund_denied", order_id=order["order_id"],
                    already_paid_vnd=already_paid, entitlement_vnd=entitlement)
            return Verdict.deny("sổ cái đã hoàn đủ quyền lợi cho đơn này, không hoàn lặp")
        amount = action.get("amount_vnd")
        if (isinstance(amount, bool) or not isinstance(amount, int) or amount <= 0
                or amount not in (entitlement, remaining)):
            return Verdict.escalate("tiền hoàn khác quyền lợi tính từ tracking DB và chính sách hiệu lực")
        if action.get("payer") != "LOGIX":
            return Verdict.escalate("không cho model tự đổi bên trả tiền sang shop")
        if action.get("basis", "policy") != "policy":
            return Verdict.escalate("không hoàn tự động khi policy check ở chế độ dự phòng fail_open")
        if delay > 0 and parcel.get("delay_cause") is None:
            return Verdict.escalate("tracking chưa ghi nguyên nhân trễ, không tự suy đoán")
        target_amount = remaining if rows else entitlement
        approval_id = action.get("approval_id")
        if (approval_id or target_amount > policy["auto_limit_vnd"]) and not _approval_ok(
                ctx, {**action, "amount_vnd": target_amount}, order):
            return Verdict.escalate("thiếu phê duyệt hợp lệ đúng ticket, đơn, khách, hạn mức và người duyệt")

        # Cổng 2: kiểm trần TRƯỚC khi ghi tiền, kể cả trần lỗi hãng ở bước kế tiếp.
        limits = ctx.tools.ops_limits()
        if not approval_id:
            customer_paid = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(customer_id=order["customer_id"])
                                if not r.get("approval_id") and r.get("basis") != "manual")
            customer_cap = limits.get("max_auto_refund_per_customer_per_day_vnd")
            if customer_cap is not None and customer_paid + target_amount > customer_cap:
                return Verdict.escalate("vượt trần hoàn tự động cho một khách: chuyển người trước khi ghi")
            caps = [limits.get("daily_auto_refund_budget_vnd"),
                    ctx.gates.get("business", {}).get("daily_refund_cap_vnd")]
            if any(ctx.tools.auto_refund_today_vnd() + target_amount > cap for cap in caps if cap is not None):
                return Verdict.escalate("vượt trần hoàn tự động trong ngày: chuyển người trước khi ghi")
        strike_cap = limits.get("max_auto_strikes_per_carrier_per_day")
        if (H.carrier_at_fault(policy, parcel, delay) and strike_cap is not None
                and len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= strike_cap):
            return Verdict.escalate("hãng đã chạm trần lỗi tự động/ngày: người duyệt cả yêu cầu trước khi hoàn")
        if amount != target_amount:
            ctx.log("partial_refund_adjusted", order_id=order["order_id"],
                    already_paid_vnd=already_paid, remaining_vnd=target_amount)
            return Verdict.modify("khấu trừ khoản đã hoàn một phần trước đó trong sổ cái", amount_vnd=target_amount)

    # Cổng 3: lệnh ghi lỗi và thông báo chỉ dùng đúng kiện, đúng hãng, đúng căn cứ DB.
    elif tool == "file_carrier_fault":
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("DB và chính sách hiệu lực không cho phép ghi lỗi hãng")
        expected = {"order_id": order["order_id"], "parcel_id": parcel["parcel_id"],
                    "carrier_id": parcel["carrier_id"], "driver_id": parcel.get("driver_id"), "delay_days": delay}
        if any(action.get(k) != v for k, v in expected.items()):
            return Verdict.modify("sửa hãng, kiện và độ trễ theo tracking DB", **expected)
    elif tool == "notify_carrier":
        payload = {"order_id": order["order_id"], "parcel_id": parcel["parcel_id"],
                   "district": order.get("recipient", {}).get("district"), "delay_days": delay}
        permitted = set(policy.get("carrier_notice_fields", ()))
        blocked = set(ctx.gates.get("legal", {}).get("pii_fields_blocked_to_third_party", ()))
        payload = {k: v for k, v in payload.items() if k in permitted and k not in blocked}
        if action.get("payload") != payload or action.get("carrier_id") != parcel["carrier_id"]:
            return Verdict.modify("chỉ gửi trường nghiệp vụ được phép, bỏ chữ khách và thông tin người nhận",
                                  carrier_id=parcel["carrier_id"], payload=payload)
    return Verdict.allow()
