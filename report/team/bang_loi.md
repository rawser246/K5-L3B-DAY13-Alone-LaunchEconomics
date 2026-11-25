# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

> Hai người gắn nhãn tự điền hai cột dưới đây, ngồi tách nhau, không trao đổi, trước khi xem bảng khắc phục ở cuối file. Không sửa bộ nhãn độc lập sau khi đã so.

Người gắn nhãn 1: Đoàn Công Hải, lượt 1 (`docs/cp3_gan_nhan/luot_1.md`, thứ tự ca 1 → 20) · Người gắn nhãn 2: Đoàn Công Hải, lượt 2 (`docs/cp3_gan_nhan/luot_2.md`, thứ tự ca đã xáo, seed 2026).

> Nhóm Alone làm một mình: hai bộ nhãn là hai lượt gắn của **cùng một người**, thứ tự ca đã đảo; file lượt 1 lưu lúc 18:03, lượt 2 lúc 18:09 ngày 25/11/2026 (cách nhau ~6 phút). Đây không phải hai người độc lập.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | ✅ | Do người dùng |
| 2 | Hệ thống | Hệ thống | ✅ | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | ✅ | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | ✅ | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | ✅ | Ngầm |
| 6 | Do người dùng | Do người dùng | ✅ | Do người dùng |
| 7 | Hệ thống | Hệ thống | ✅ | Hệ thống |
| 8 | Hệ thống | Hệ thống | ✅ | Hệ thống |
| 9 | Do người dùng | Ngữ cảnh | ❌ | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | ✅ | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | ✅ | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | ✅ | Ngầm |
| 13 | Giới hạn hệ thống | Hệ thống | ❌ | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | ✅ | Do người dùng |
| 15 | Hệ thống | Hệ thống | ✅ | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | ✅ | Ngữ cảnh |
| 17 | Ngầm | Ngầm | ✅ | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | ✅ | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | ✅ | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | ✅ | Hệ thống |

**Tỉ lệ đồng thuận:** 18/20 = 90% (lệch ca 9 và ca 13; ca 4 lượt 2 ghi "Gh", tính là GH).

Phân bố nhãn lượt 1: Do người dùng 4 · Hệ thống 5 · Ngữ cảnh 4 · Giới hạn hệ thống 4 · Ngầm 3.

## Quy tắc phân biệt cho các ca không trùng

Định nghĩa dùng khi gắn nhãn (gắn theo nguyên nhân gốc, không theo chỗ cần sửa):

- **Do người dùng:** gốc lỗi nằm ở thao tác hoặc dữ liệu khách đưa vào (chọn sai, nhập sai, bấm nhầm).
- **Hệ thống:** trợ lý hoặc hệ thống làm sai và cái sai đã lộ ra (khách, nhân viên hoặc log thấy).
- **Ngữ cảnh:** trợ lý làm đúng thiết kế hoặc chính sách nhưng không khớp kỳ vọng, hoàn cảnh của khách.
- **Giới hạn hệ thống:** yêu cầu nằm ngoài khả năng, dữ liệu hoặc phạm vi của trợ lý.
- **Ngầm:** có sai (về tiền hoặc chi phí) nhưng không ai nhận ra cho tới khi kiểm tra.

Quy tắc cho các ca không trùng (đồng thuận 18/20 = 90%, không cần viết lại định nghĩa):

- **Ca 9 → Do người dùng** (lượt 1 Do người dùng, lượt 2 Ngữ cảnh): gốc lỗi là khách nhập sai mã (mã đơn sàn thay vì mã vận đơn); nếu khách nhập đúng thì lỗi không xảy ra. Trợ lý báo "mã không hợp lệ" rồi dừng, không gợi ý, là chỗ cần cải thiện, nằm ở cột "Khắc phục thế nào".
- **Ca 13 → Giới hạn hệ thống** (lượt 1 Giới hạn hệ thống, lượt 2 Hệ thống): gốc lỗi là yêu cầu nằm ngoài phạm vi (bảo hiểm hàng hoá); nếu trong phạm vi thì không vướng giới hạn này. Trợ lý trả lời chung chung thay vì từ chối hoặc chuyển đúng luồng là cách xử lý giới hạn kém (chỗ cần sửa), không phải nguyên nhân gốc.
- Quy tắc chung rút ra: gắn nhãn theo điều gì gây ra lỗi; cách trợ lý phản ứng sau đó thuộc cột khắc phục.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (kèm trace_id, mẫu mã nhập); cảnh báo khi > 2% số yêu cầu/ngày | Nhận diện định dạng mã sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh chỗ tìm mã vận đơn | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn "đã hoàn" không có bản ghi `refund_ledger_write` ok cùng trace_id; ngưỡng 0 ca | Chỉ gửi "đã hoàn" khi sổ cái trả ok; 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Tỉ lệ `ticket_reopened` với reason = so_tien mà kiểm tra thấy số tiền đúng, theo tuần; cảnh báo > 1% | Mẫu tin nhắn luôn kèm cách tính: "30.000 đ × 50% = 15.000 đ" và điều khoản áp dụng | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với reason = thieu_du_lieu, đếm theo loại yêu cầu mỗi tuần | Giữ cách chuyển kèm tóm tắt; đưa quoc_te ra khỏi phạm vi pilot (A3: 1,88×, simulated) | PM trợ lý hoàn phí |
| 17 | Ngầm | `audit_sample_checked`: kiểm tra mẫu 100 đơn/tuần so với bảng giá hiện hành; ngưỡng 1% đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới; ghi phiên bản bảng giá vào trace để đối chiếu | Kế toán trưởng |
