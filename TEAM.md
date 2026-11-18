# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): NhomKhongCoTen
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-NhomKhongCoTen-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): `S5`

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Nguyễn Công Tĩnh | 2A202603373 | Kỹ sư cổng | ✅ |
|   2 | Dương Tuấn Hưng | 2A202603416 | Kỹ sư cổng | |
|   3 | Trần Đăng Khoa | 2A202603364 | Sản phẩm và kinh doanh | |
|   4 | Nguyễn Ngọc Minh Đức | 2A202603421 | Vận hành và pháp lý | |

### Phân công theo giai đoạn (đóng góp thực tế)

Cột "Vai" ở bảng trên là người **chịu trách nhiệm nội dung** của phần việc theo vai (người cầm bút ghi trong từng phiếu); bảng dưới ghi **ai thực hiện** từng giai đoạn.

| Giai đoạn (phút) | Người thực hiện | Việc đã làm | Bằng chứng |
| --- | --- | --- | --- |
| 0–15 | Nguyễn Công Tĩnh | Tạo repo, gắn `upstream`, danh tính Git, chạy test công khai, điền `TEAM.md` | commit `6937ef5` |
| 15–65 | Nguyễn Công Tĩnh (có Claude hỗ trợ nháp) | Phiếu A mục A1–A5, `config/acceptance_criteria.json`, ký và push tiêu chí | commit `a5c859d` (Sign acceptance criteria), hash `13484cbd` |
| 65–85 | Nguyễn Công Tĩnh (có Claude hỗ trợ nháp) | Chạy mốc base, gate, trace `T-002@55`; Phiếu B mục B0–B6 | `R-base-before-20261118-083543-bde05c`, commit `37273b4` |
| 85–115 | Dương Tuấn Hưng, Trần Đăng Khoa, Nguyễn Ngọc Minh Đức | Cổng vòng 1 (`lab10/guards.py`), `config/operating_gates.json`, Phiếu B mục B7–B8, chốt vòng 1 | `R-base-prepared-20261118-162549-345c70`, hash `27df2c92`, commit `323660f` |
| 125–200 | Dương Tuấn Hưng, Nguyễn Công Tĩnh, Trần Đăng Khoa, Nguyễn Ngọc Minh Đức | Nhận thẻ `S5`, đo mốc prepared, phân tích trace `S5-02, 20, 21, 50, 51, 70`, sửa `guards.py` + `monitors.py` + `operating_gates.json`, điền Phiếu C mục C0–C12, quyết định v2 (`Thu hẹp`) | `R-S5-grade-20261118-164447-0590dc` (trước sửa) → `R-S5-grade-20261118-165649-9dc810` (`PASS-VISIBLE`) |
| 200–240 | Cả bàn (Tĩnh, Hưng, Khoa, Đức) | Kiểm tra lại bộ nền, gom bài nộp `submission/` (`check_submission --collect` đạt `ĐỦ THÀNH PHẦN`), cập nhật `TEAM.md` và đẩy bài nộp | `submission/manifest.json`, `R-S5-after-20261118-165650-9dc810`, `R-base-after-20261118-165649-9dc810` |

Ghi chú bàn giao: thư mục `runs/` (có `journal.jsonl` và report baseline) không lên git (`.gitignore`); bàn giao bằng cách nén và gửi cho người làm giai đoạn sau. File `.gitattributes` giữ đúng kiểu xuống dòng để hash file khoá và tiêu chí đã ký khớp trên mọi máy.

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenCongTinh-2A202603373

### Phần việc phụ trách

Trưởng nhóm, Kỹ sư cổng. Thực hiện giai đoạn phút 0–85: cài đặt repo (origin, upstream, danh tính Git); Phiếu A mục A1–A5 và `config/acceptance_criteria.json`, ký và push tiêu chí; chạy mốc base (lệnh 2, 3, 4) và điền Phiếu B mục B0–B6; xử lý lỗi xuống dòng CRLF/LF (`.gitattributes`) để hash khớp. Ở vòng 2: phối hợp kiểm tra cổng `write_gate` cho đơn hoàn lặp / hoàn một phần trên thẻ `S5` và đối chiếu không hồi quy trên bộ nền.

Dùng AI để: đọc hiểu đề và code, nháp câu trả lời Phiếu A–C và ngưỡng tiêu chí; bàn đã soát và chốt lại các con số.

### Đóng góp cụ thể

- Khởi tạo repo nhóm, cấu hình `.gitattributes` để bảo toàn SHA-256 của các file khoá và `acceptance_criteria.lock` giữa macOS/Windows.
- Thiết kế offline metric cho bước `file_carrier_fault` (Phiếu A mục A2, câu 1.3), chạy đánh giá mốc `base` đầu tiên sau khi ký tiêu chí, phân tích lỗi chìm `T-002@55` (`model_override` lấy 5 ngày khách khai đè lên 2 ngày DB).
- Ở vòng 2 trên thẻ `S5`: đối chiếu kết quả giữa mốc `base` (`R-S5-before-20261118-164448-0590dc`) và `prepared` (`R-S5-prepared-20261118-164448-0590dc`), xác định nguyên nhân `S5-21` hỏng ở mốc `prepared` (đơn `O-2521` đã hoàn tay một phần `10.000đ` trong `ledger_seed`, cần hoàn bù `12.000đ`) và bổ sung dòng Risk register cho rủi ro đồng bộ sổ cái.

### Bằng chứng

- Commit `6937ef5` (Team roster), `a5c859d` (Sign acceptance criteria, hash `13484cbd`), `37273b4` (Phiếu A5, Phiếu B B0–B6), `af47255` (`.gitattributes`).
- Mã lần chạy: `R-base-before-20261118-083543-bde05c`, `R-S5-grade-20261118-164447-0590dc`, `R-S5-grade-20261118-165649-9dc810`.
- Mục phiếu: Phiếu A mục A2 (câu 1.3), A5; Phiếu B mục B0, B1, B2; Phiếu C mục C1, C6, C9, C10.

### Exit ticket

- **Một điều học được:** Một cổng an toàn ở vòng 1 (`if rows: escalate`) tuy chặn được mất tiền hoàn lặp (`890.000đ → 0đ`) nhưng nếu không tính số dư còn lại (`entitlement - already_paid`) và không phân biệt `deny` với `escalate` thì sẽ làm hỏng nghiệp vụ hoàn bù một phần (`S5-21`) và đẩy chi phí công người duyệt tăng vọt.
- **Một điều còn chưa chắc:** Khi triển khai thật với nhiều worker chạy song song, cần kiểm chứng thêm cơ chế khoá giao dịch (transaction / unique constraint theo `order_id`) ở tầng cơ sở dữ liệu vì `write_gate` trong Python chỉ đọc trạng thái sổ cái tại thời điểm gọi hàm.

## DuongTuanHung-2A202603416

### Phần việc phụ trách

Kỹ sư cổng. Vòng 1: Phiếu A câu 1.3 (cùng Tĩnh), dò trace `T-002@55` (B2), viết 3 nhóm cổng phòng ngừa trong `lab10/guards.py` (`pre_guard` và `write_gate`), behavioral test và 2 ticket hiểm (B7.1–B7.3), chốt cổng vòng 1 (`checkpoint`). Vòng 2: nhận thẻ `S5`, dò trace các ca sự cố (`S5-02, S5-20, S5-21, S5-50, S5-51, S5-70`), sửa `lab10/guards.py` và viết 3 chỉ số theo dõi mới trong `lab10/monitors.py` (Phiếu C mục C2, C7, C8).

Dùng AI để: đọc hiểu đề và code, nháp câu trả lời và kiểm tra các nhánh biên; bàn đã soát và chạy thực nghiệm lại toàn bộ.

### Đóng góp cụ thể

- Viết cổng phòng ngừa vòng 1 trong `lab10/guards.py` (ghim `policy_id` theo `as_of`, dự toán tổng phí LLM cả luồng trong `pre_guard`, đối chiếu `entitlement_vnd` và `carrier_at_fault` từ tracking DB, lọc trường PII trong `notify_carrier`), giúp ở mốc `prepared` trên thẻ `S5` chặn ngay `890.000đ` hoàn sai, `20` lỗi hãng oan và giữ `llm_cost_max = 764đ <= 1.500đ`.
- Ở vòng 2 (thẻ `S5`): sửa nhánh `issue_refund` trong `lab10/guards.py` để tính `already_paid` từ `ledger_rows(order_id)` và `remaining = entitlement - already_paid` — trả `Verdict.deny` khi `remaining <= 0` (`S5-02, 03, 05, 20`) và `Verdict.modify(..., amount_vnd=remaining)` khi `0 < remaining < entitlement` (`S5-21` hoàn đúng `12.000đ`).
- Thiết kế và cài đặt 3 chỉ số theo dõi trong `lab10/monitors.py`: `max_warehouse_cost_per_ticket_vnd`, `over_llm_budget_rate`, `ledger_repeat_refund_rate` (cả 3 đều sáng đèn ở cả `before` và `after`).

### Bằng chứng

- Commit `323660f` (chốt cổng vòng 1, hash `27df2c92`), file `lab10/guards.py`, `lab10/guards_round1.py`, `lab10/monitors.py`.
- Mã lần chạy: `R-base-after-20261118-162548-345c70`, `R-base-prepared-20261118-162549-345c70`, `R-S5-after-20261118-165619-cb2bbf`, `R-S5-after-20261118-165649-9dc810`, `R-S5-grade-20261118-165649-9dc810` (`PASS-VISIBLE`).
- Mục phiếu: Phiếu B mục B2, B7.1–B7.3; Phiếu C mục C0, C2, C6, C7, C8, C9.

### Exit ticket

- **Một điều học được:** Có những bài toán (như kho sỉ `HCM-B2B` tốn `10.382đ/ticket > 10.000đ` làm tay trong lần chạy `R-S5-after-20261118-165619-cb2bbf`) mà dù code `guards.py` đã đạt `pass_rate = 1,0` và 0 lỗi an toàn thì vẫn vượt trần kinh doanh; chỗ sửa đúng phải là phạm vi `pilot_scope` trong config chứ không phải cố viết thêm if/else trong code.
- **Một điều còn chưa chắc:** Với các ticket kho lẻ dán phụ lục email dài (`S5-70, 73, 76`), hiện `pre_guard` chuyển người trước khi gọi LLM để giữ trần 1.500đ; trong pilot thật cần thử nghiệm thêm việc cắt bỏ phần lịch sử email đính kèm ở tầng tiền xử lý xem có giảm thêm được tỷ lệ chuyển người ở kho `HN` mà không làm mất thông tin quan trọng hay không.

## TranDangKhoa-2A202603364

### Phần việc phụ trách

Sản phẩm và kinh doanh, người ký Bản tiêu chí. Vòng 1: Phiếu A câu 1.1, 1.5, 1.6; `config/acceptance_criteria.json` (ngưỡng, `business_ops`, `stop_condition`, `decision_rule`), bản đồ dữ liệu và drift (B3), `config/operating_gates.json` mục `business` (B7.4), quyết định v1 (B8). Vòng 2: mở lại bản đồ dữ liệu (C3.5), viết specification (C5 câu 3.2), thu hẹp `business.pilot_scope` về 4 kho lẻ `["HN", "HCM", "DN", "CT"]`, phân tích chi phí/ROI theo kho và viết quyết định Gate 1 v2 (C12).

Dùng AI để: đọc hiểu đề và code, nháp câu trả lời và kiểm tra tính toán chi phí/ROI; bàn đã soát và chốt lại các con số.

### Đóng góp cụ thể

- Xây dựng Bản tiêu chí chấp nhận `config/acceptance_criteria.json` với `cost_per_ticket_vnd_max = 7000`, `roi_min = 0.4`, 3 chỉ số an toàn = 0 và quy tắc 4 quyết định (`Tiếp tục`, `Thu hẹp`, `Cải tiến thêm`, `Dừng`).
- Phân tích bảng phân khúc theo kho trên thẻ `S5`: chỉ ra kho sỉ `HCM-B2B` có 100% đơn từ 2,2–3,4 triệu đồng, khi trễ ≥ 7 ngày quyền lợi là `230.000đ > auto_limit_vnd (200.000đ)` nên 100% ticket phải chuyển người, khiến tự động hoá ở kho sỉ luôn lỗ (`10.382–11.326đ/ticket > 10.000đ` làm tay).
- Cấu hình `business.pilot_scope = {"mode": "warehouse", "warehouses": ["HN", "HCM", "DN", "CT"], "percent": 100}` (cắt `HCM-B2B` về luồng làm tay, giữ độ phủ `0,6` trên S5 và `1,0` trên bộ nền), đưa chi phí bình quân từ `8.188đ` xuống `3.980đ/ticket` và ROI từ `0,22` lên `1,51`, rồi lập quyết định Gate 1 v2 là **Thu hẹp**.

### Bằng chứng

- File `config/acceptance_criteria.json` (hash `13484cbd`), `config/operating_gates.json` (mục `business`).
- Mã lần chạy: `R-S5-after-20261118-165619-cb2bbf` (khi chưa cắt `HCM-B2B`: chi phí 6.541đ nhưng `HCM-B2B` 10.382đ > làm tay) so với `R-S5-after-20261118-165649-9dc810` (sau khi cắt `HCM-B2B`: chi phí 3.980đ, ROI 1,51, 0 vượt trần).
- Mục phiếu: Phiếu A mục A1, A3, A4; Phiếu B mục B3, B6, B7.4, B8; Phiếu C mục C1, C3.5, C5 (câu 3.2), C8, C10, C12.

### Exit ticket

- **Một điều học được:** Tự động hoá bằng AI không phải lúc nào cũng rẻ hơn làm tay: ở phân khúc mà quy định hạn mức (`auto_limit_vnd = 200.000đ`) bắt buộc con người phải duyệt lại gần như 100% như kho sỉ `HCM-B2B`, việc cho AI đọc trước chỉ làm tốn thêm tiền máy chồng lên 100% công người; quyết định **Thu hẹp** phạm vi dựa trên số liệu theo phân khúc là quyết định kinh doanh đúng đắn.
- **Một điều còn chưa chắc:** Với 12 ticket/ngày của kho sỉ `HCM-B2B` đang cắt về làm tay, trước Gate 2 cần làm việc với Finance và Ops xem có nên thiết kế hạn mức tự động riêng cho đơn sỉ có hợp đồng hoặc luồng phê duyệt theo lô hay giữ làm tay lâu dài.

## NguyenNgocMinhDuc-2A202603421

### Phần việc phụ trách

Vận hành và pháp lý. Vòng 1: Phiếu A câu 1.2, 1.4 (telemetry production); HAZOP vòng 1 (B4), checklist 9 nhóm việc (B5), `config/operating_gates.json` mục `operations` và `legal`, runbook 1–3 và giờ cao điểm (B7.5–B7.6). Vòng 2: HAZOP của thẻ `S5` (C4), giả định môi trường (C5 câu 3.3), cập nhật checklist 9 nhóm việc và viết runbook phần 4–5 (C11), điền `submission/submission.json` và chạy lệnh 7 gom bài nộp.

Dùng AI để: đọc hiểu đề và code, nháp câu trả lời HAZOP và runbook; bàn đã soát và chốt lại các con số.

### Đóng góp cụ thể

- Thiết lập cổng vận hành và pháp lý trong `config/operating_gates.json` (`pic = NV-TUNG`, `approver_id = NV-HANH`, `reviewers_on_shift = 1`, `review_capacity_per_hour = 6`, `max_queue_wait_minutes = 60`, `decision_note = true`, `review_sampling_pct = 10`, chặn các trường PII gửi sang hãng và bắt buộc `carrier_fault_requires_recorded_cause = true`).
- Thực hiện phân tích HAZOP của thẻ `S5` (Phiếu C mục C4) và chỉ ra giả định môi trường bị phá vỡ ngoài thực tế (cờ `refund_status` chỉ đồng bộ theo batch đêm trong khi CSKH hoàn tay một phần/toàn phần và khách gửi lặp nhiều kênh; khách email dán bảng kê dài).
- Cập nhật `operations.stop_conditions`, hoàn thiện Checklist 9 nhóm việc (mọi dòng đều có PIC và bằng chứng mốc `after`), viết Runbook 4–5 (quy trình đối soát huỷ 20 lỗi hãng ghi đúp ở dữ liệu PoC cũ với chị Oanh và 3 kịch bản ứng phó tuần đầu pilot), điền `submission/submission.json` và kiểm tra đủ thành phần nộp bài.

### Bằng chứng

- File `config/operating_gates.json` (mục `operations`, `legal`), `submission/submission.json`, `submission/manifest.json`.
- Mã lần chạy: `R-S5-grade-20261118-165649-9dc810`, `R-base-after-20261118-165649-9dc810`.
- Mục phiếu: Phiếu A mục A1 (câu 1.2), A2 (câu 1.4); Phiếu B mục B4, B5, B7.5, B7.6; Phiếu C mục C4, C5 (câu 3.3), C10, C11, C12.

### Exit ticket

- **Một điều học được:** Rủi ro vận hành lớn nhất trong thẻ `S5` nằm ở "thứ bậc hệ thống" giữa hai quy trình cùng ghi vào một sổ cái (CSKH hoàn tay và trợ lý tự động) khi cờ trạng thái chỉ đồng bộ theo batch đêm; nếu runbook và cổng không quy định lấy sổ cái thời gian thực làm nguồn sự thật thì cả tiền hoàn lẫn lỗi phạt hãng vận chuyển đều bị nhân đôi âm thầm.
- **Một điều còn chưa chắc:** Tỉ lệ kiểm mẫu `10%` kết hợp `decision_note = true` đang giả định mỗi ca kiểm lại tốn đúng `0,4` đơn vị công (4 phút); khi chạy thử thật cần đo lại thời gian thực tế nhân viên của chị Hạnh đọc ghi chú và đối chiếu sổ cái xem có giữ được dưới 4 phút/ca hay không.
