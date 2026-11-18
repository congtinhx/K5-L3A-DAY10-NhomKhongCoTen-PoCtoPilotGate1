# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): NhomKhongCoTen
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-NhomKhongCoTen-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

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
| 85–115 | (bạn phụ trách giai đoạn này tự điền tên) | Cổng vòng 1, `config/operating_gates.json`, B7–B8, chốt vòng 1 | |
| 125–200 | | Thẻ sự cố, Phiếu C, quyết định v2 | |
| 200–240 | | Demo, gom bài, nộp | |

Ghi chú bàn giao: thư mục `runs/` (có `journal.jsonl` và report baseline) không lên git (`.gitignore`); bàn giao bằng cách nén và gửi cho người làm giai đoạn sau. File `.gitattributes` giữ đúng kiểu xuống dòng để hash file khoá và tiêu chí đã ký khớp trên mọi máy.

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NguyenCongTinh-2A202603373

### Phần việc phụ trách

Trưởng nhóm, Kỹ sư cổng. Thực hiện giai đoạn phút 0–85: cài đặt repo (origin, upstream, danh tính Git); Phiếu A mục A1–A5 và `config/acceptance_criteria.json`, ký và push tiêu chí; chạy mốc base (lệnh 2, 3, 4) và điền Phiếu B mục B0–B6; xử lý lỗi xuống dòng CRLF/LF (`.gitattributes`) để hash khớp. Bàn giao giai đoạn 85–115 cho bạn phụ trách cổng vòng 1.

Dùng AI (Claude) để: đọc hiểu đề và code, nháp câu trả lời Phiếu A và ngưỡng tiêu chí; bàn đã soát và chốt lại các con số.

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## DuongTuanHung-2A202603416

### Phần việc phụ trách

Kỹ sư cổng. Vòng 1: Phiếu A câu 1.3 (offline metric bước ghi lỗi hãng, cùng Tĩnh); sắp tới: dò trace `T-002@55` (B2), behavioral test và ticket hiểm (B7.3), viết cổng trong `lab10/guards.py`. Vòng 2: dò trace thẻ sự cố, chỉ số theo dõi trong `lab10/monitors.py`.

Dùng AI (Claude) để: đọc hiểu đề và code, nháp câu trả lời Phiếu A và ngưỡng tiêu chí; bàn đã soát và chốt lại các con số.

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## TranDangKhoa-2A202603364

### Phần việc phụ trách

Sản phẩm và kinh doanh, người ký Bản tiêu chí. Vòng 1: Phiếu A câu 1.1, 1.5 (ghi), 1.6; `config/acceptance_criteria.json` (ngưỡng, `business_ops`, `stop_condition`, `decision_rule`), ký ở phút 60–65; sắp tới: bản đồ dữ liệu và drift (B3), `config/operating_gates.json` mục `business` (B7.4), quyết định v1 (B8). Vòng 2: chi phí, ROI, phạm vi pilot, quyết định v2 (C12).

Dùng AI (Claude) để: đọc hiểu đề và code, nháp câu trả lời Phiếu A và ngưỡng tiêu chí; bàn đã soát và chốt lại các con số.

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## NguyenNgocMinhDuc-2A202603421

### Phần việc phụ trách

Vận hành và pháp lý. Vòng 1: Phiếu A câu 1.2, 1.4 (telemetry production); sắp tới: HAZOP vòng 1 (B4), checklist 9 nhóm (B5), `config/operating_gates.json` mục `operations` và `legal`, runbook 1–3 và giờ cao điểm (B7.5–B7.6). Vòng 2: runbook 4–5 (C11), `submission/submission.json`, gom bài (lệnh 7).

Dùng AI (Claude) để: đọc hiểu đề và code, nháp câu trả lời Phiếu A và ngưỡng tiêu chí; bàn đã soát và chốt lại các con số.

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
