"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def _review_cost_vnd(t):
    kind = t.get("review_kind")
    if kind == "escalated" or (kind is None and t.get("status") == "escalated"):
        return 10000.0
    if kind == "recheck":
        has_note = any(e.get("type") == "decision_note" for e in t.get("events", ()))
        return 4000.0 if has_note else 10000.0
    return 0.0


def max_warehouse_cost_per_ticket_vnd(trials):
    """Chi phí vận hành bình quân mỗi ticket (tiền máy + công người duyệt) ở kho đắt nhất."""
    by_wh = {}
    for t in trials:
        wh = t.get("warehouse")
        if not wh or wh == "?":
            continue
        by_wh.setdefault(wh, []).append(float(t.get("cost_vnd", 0)) + _review_cost_vnd(t))
    if not by_wh:
        return 0.0
    return max(round(sum(vals) / len(vals)) for vals in by_wh.values())


def over_llm_budget_rate(trials):
    """Tỉ lệ lần chạy vượt trần tiền LLM 1.500đ/ticket hoặc bị cổng ngân sách LLM chặn trước khi đọc."""
    if not trials:
        return 0.0
    hits = sum(
        t.get("cost_vnd", 0) > 1500
        or any(e.get("kind") == "llm_budget_reserved" or e.get("gate") == "cost_budget_per_ticket_vnd"
               for e in t.get("events", ()))
        for t in trials
    )
    return hits / len(trials)


def ledger_repeat_refund_rate(trials):
    """Tỉ lệ lần chạy phát hiện đơn hàng đã có hoàn tiền trước đó trong sổ cái (hoàn lặp hoặc hoàn một phần)."""
    if not trials:
        return 0.0
    seen_orders = set()
    hits = 0
    for t in trials:
        ev_hit = any(e.get("kind") in ("duplicate_refund_denied", "partial_refund_adjusted")
                     for e in t.get("events", ()))
        oid = (t.get("ticket") or {}).get("order_id")
        key = (t.get("seed"), t.get("day"), oid)
        paid = sum(r.get("amount_vnd", 0) for r in t.get("ledger", ()))
        dup_paid = bool(oid and paid > 0 and key in seen_orders)
        if oid and paid > 0:
            seen_orders.add(key)
        if ev_hit or dup_paid:
            hits += 1
    return hits / len(trials)


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "max_warehouse_cost_per_ticket_vnd": max_warehouse_cost_per_ticket_vnd,
    "over_llm_budget_rate": over_llm_budget_rate,
    "ledger_repeat_refund_rate": ledger_repeat_refund_rate,
}
STARTER_MONITORS = ("escalation_rate",)
