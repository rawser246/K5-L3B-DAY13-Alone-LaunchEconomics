# CP3 · Lượt gắn nhãn 2

Thứ tự ca đã xáo (seed 2026). Làm **cách lượt 1 ít nhất vài giờ**, không mở `luot_1.md` khi đang gắn. Cột "Ca" là số ca gốc.

Bắt đầu lúc: không ghi · Kết thúc lúc: 18:09 ngày 25/11/2026 (giờ lưu file) (tối đa 8 phút)

## Năm loại lỗi (Google PAIR) · gắn theo NGUYÊN NHÂN GỐC, không theo chỗ cần sửa

| Loại | Định nghĩa |
| --- | --- |
| **Do người dùng** | Gốc lỗi nằm ở thao tác hoặc dữ liệu khách đưa vào (chọn sai, nhập sai, bấm nhầm). |
| **Hệ thống** | Trợ lý hoặc hệ thống làm sai, và cái sai **đã lộ ra** (khách, nhân viên hoặc log nhìn thấy). |
| **Ngữ cảnh** | Trợ lý làm **đúng thiết kế/chính sách**, nhưng thiết kế không khớp với kỳ vọng hay hoàn cảnh của khách. |
| **Giới hạn hệ thống** | Yêu cầu nằm **ngoài khả năng, dữ liệu hoặc phạm vi** của trợ lý. |
| **Ngầm** | Có sai (về tiền, về chi phí…) nhưng **không ai nhận ra** cho tới khi kiểm tra. |

Câu tự hỏi: (1) Gốc lỗi do khách không? (2) Trợ lý có làm đúng thiết kế không? (3) Việc này có nằm trong khả năng của trợ lý không? (4) Cái sai đã có ai thấy chưa?

Ghi tắt: **ND** = Do người dùng · **HT** = Hệ thống · **NC** = Ngữ cảnh · **GH** = Giới hạn hệ thống · **NG** = Ngầm

## Các ca

| STT | Ca | Mô tả | Nhãn |
| --: | --: | --- | --- |
| 1 | 6 | Khách chọn mục “Hoàn phí giao trễ” nhưng nội dung mô tả hàng bị vỡ. Trợ lý xử lý theo luồng giao trễ và từ chối vì đơn giao đúng hạn. |ND|
| 2 | 3 | Theo thiết kế, trợ lý hoàn tiền về ví LogiX trong 5 phút. Khách chờ tiền về tài khoản ngân hàng và báo “chưa được hoàn”. |NC|
| 3 | 1 | Khách nhập số tài khoản nhận hoàn tiền thiếu hai chữ số. Trợ lý tạo lệnh hoàn, ngân hàng trả về lỗi. |ND|
| 4 | 2 | Kiện nội địa 28 kg. Trợ lý gọi tool tra bảng giá với tham số hàng thường thay vì hàng nặng, hoàn thiếu 45.000 đ. Khách mở lại sau 2 ngày. |HT|
| 5 | 14 | Khách bấm nhầm “Xác nhận đã nhận tiền” khi chưa nhận. Yêu cầu bị đóng. |ND|
| 6 | 5 | Kiểm tra mẫu cuối tuần thấy 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình 12.000 đ mỗi đơn. Không khách nào báo, không cảnh báo nào kích. |NG|
| 7 | 12 | Tool tra đơn của depot D05 trả thiếu một trường. Trợ lý vẫn ra kết quả đúng sau nhiều lần gọi, nên tiền token của D05 gấp 3 lần depot khác suốt 3 tuần mà không ai thấy. |NG|
| 8 | 8 | Trợ lý dẫn “Điều 7.2 chính sách hoàn phí” làm căn cứ. Bản chính sách hiện hành không có điều 7.2. Số tiền hoàn vẫn đúng. |HT|
| 9 | 19 | Khách yêu cầu hoàn phí cho đơn từ 14 tháng trước. Trợ lý chỉ truy cập được dữ liệu 12 tháng. Trợ lý nói rõ không tra được và chuyển cho nhân viên kèm tóm tắt. |GH|
| 10 | 7 | API sổ cái trả lỗi 503 ở bước ghi hoàn tiền. Trợ lý thử lại 3 lần rồi vẫn báo khách “đã hoàn tiền thành công”. |HT|
| 11 | 9 | Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn. Trợ lý báo “mã không hợp lệ” rồi dừng, không gợi ý gì. |NC|
| 12 | 13 | Khách hỏi hoàn phí bảo hiểm hàng hoá, sản phẩm của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý. Trợ lý trả lời chung chung về phí vận chuyển, không nói rõ là mình không xử lý được. |HT|
| 13 | 10 | Đơn giao trễ do bão. Trợ lý từ chối hoàn theo điều khoản bất khả kháng, đúng chính sách. Khách thấy vô lý vì ứng dụng vẫn hiện “cam kết giao 24 giờ”. |NC|
| 14 | 16 | Theo thiết kế “gửi ngay khi xong”, trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng. Khách phản ánh bị làm phiền. |NC|
| 15 | 15 | Đơn trễ 26 giờ. Chính sách: trễ 24–48 giờ hoàn 50%. Trợ lý tính hoàn 100%. Nhân viên xem lại bắt được trước khi gửi. |HT|
| 16 | 20 | Khách gửi lại yêu cầu sau 10 phút vì chưa thấy phản hồi. Trợ lý hoàn hai lần cho cùng một đơn vì lệnh thứ hai không có khoá chống trùng. |HT|
| 17 | 18 | Trợ lý tính đúng: phí giao 30.000 đ, hoàn 50%. Tin nhắn chỉ ghi “Đã hoàn 15.000 đ”, không kèm cách tính. Khách cho là hoàn thiếu và mở lại yêu cầu. |NC|
| 18 | 17 | Bảng giá đổi từ ngày 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn dưới 2 kg. Lệch 1.000–2.000 đ mỗi đơn, 212 đơn trong 9 ngày, không ai mở lại. |NG|
| 19 | 11 | Khách gửi tin nhắn thoại 40 giây. Trợ lý không xử lý được âm thanh, trả lời “vui lòng nhập bằng chữ”. |GH|
| 20 | 4 | Khách yêu cầu hoàn phí cho chặng do hãng nước ngoài giao. LogiX không có dữ liệu chặng này. Trợ lý nói không xác định được trạng thái và chuyển cho nhân viên. |Gh|
