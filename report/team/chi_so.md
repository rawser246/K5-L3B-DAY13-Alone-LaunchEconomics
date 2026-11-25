# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Số tính bằng `src/lab13.py` (`python lab13.py cp5`).

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm can thiệp được xử lý bằng trợ lý | số `agent_suggestion_shown` có staff thuộc nhóm can thiệp, chia số `refund_request_created` của nhóm đó | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | số `audit_sample_checked` có `so_tien_da_hoan` khác `so_tien_dung`, chia số đơn được kiểm tra | Không cần tính |

Chỉ số chính trong đợt chạy thử là 82,83%. Đợt chạy thử không có nhóm đối chứng, nên con số này không cho biết trợ lý tạo ra bao nhiêu phần chênh so với baseline 0,70.

### Trong phạm vi pilot (noi_dia + hang_nang, 982 yêu cầu) và ngưỡng dùng trong `pilot_plan.yaml`

| Chỉ số | Đợt chạy thử, trong phạm vi | Ngưỡng / mục tiêu trong pilot | Luật dừng liên quan |
| --- | --- | --- | --- |
| Chính | 92,26% (906/982) | Chênh nhóm trợ lý − đối chứng ≥ 6 điểm (mde 0,06, 859/nhóm) | Chỉ đọc ngày 05/01/2027 |
| Dùng: bỏ qua gợi ý | 21,09% (27/128 được xem lại) | > 40% trong 1 tuần thì dừng chuyển bước; < 15% thì giảm xem lại theo bậc | Luật 3 |
| An toàn: mở lại 7 ngày | 3,97% (39/982) | Cao hơn đối chứng ≥ 2 điểm hoặc vượt 6% | Luật 1 |

Ngưỡng an toàn đặt theo tỉ lệ hiện tại 3,97%: trần 6% cách mức hiện tại ~2 điểm, nên pilot không bị dừng ngay tuần đầu như khi đặt 3%. Chỉ số chính 92,26% trong phạm vi cao hơn cả mẫu (82,83%) vì đã loại quoc_te và doi_tac. Đây chỉ là mô tả đợt chạy thử, không phải tác động của trợ lý.

## Danh sách event

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| refund_request_created | App khách | request_id, loai, so_tien, depot, arm, trace_id | Khi khách gửi yêu cầu |
| agent_run_completed | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| agent_suggestion_shown | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| staff_review_decision | Nhân viên | giu/sua/bo, phut_xem_lai (đo thật), staff_id, trace_id | Khi bấm giữ/sửa/bỏ |
| staff_rework_completed | Nhân viên | phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| refund_ledger_write | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ hoàn tiền |
| handoff_to_staff | Agent | reason, tom_tat, trace_id | Khi chuyển nhân viên |
| ticket_closed | Hệ thống ticket | closed_at, trace_id | Khi đóng yêu cầu |
| ticket_reopened | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| audit_sample_checked | Kế toán | so_tien_da_hoan, so_tien_dung, bang_gia_version, trace_id | Hằng tuần |

**Kiểm tra chéo:** event dùng để tính từng chỉ số.

- Chính: `refund_request_created` (mẫu số, created_at) + `ticket_closed` (đóng trong 24 giờ) + `ticket_reopened` (mở lại trong 7 ngày).
- Dùng (bỏ qua gợi ý): `staff_review_decision` (sua/bo trên tổng số quyết định).
- An toàn (lọt đến khách): `ticket_reopened` chia `refund_request_created`.
- Dùng (tự đề xuất): `agent_suggestion_shown` chia `refund_request_created` theo arm.
- An toàn (tự đề xuất): `audit_sample_checked`.
- Chi phí mỗi việc thành công: `agent_run_completed` (token, tool) + `staff_review_decision` và `staff_rework_completed` (phút đo thật thay cho cột simulated).

## E2 · Rủi ro kinh tế

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, lên 6.787 đ/việc [simulated] | Tỉ lệ làm lại theo tuần > 7% (đợt chạy thử: 4,9% trong phạm vi) | Thu hẹp về noi_dia, rà 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98× (12.415 đ = 1,03× nếu làm lại 15,3 phút như dữ liệu) [simulated] | % yêu cầu được xem lại còn > 50% ở cuối bước 0.25 | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%; mục tiêu mỗi lần xem lại < 5 phút | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yc/tháng, +2.370 đ/việc nếu còn một nửa (5.784 đ = 0,48×) [simulated] | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, đàm phán lại chi phí cố định | PM trợ lý hoàn phí |
| Lương nhân viên tăng 25% | +23,1%, lên 5.506 đ/việc [simulated]; mức nhân viên tự làm cũng tăng lên 15.000 đ nên tỉ lệ so sánh gần như không đổi | Thông báo điều chỉnh lương của phòng nhân sự | Cập nhật `LUONG_PHUT` và `BASELINE` trong mô hình, tính lại hồ sơ | PM trợ lý hoàn phí |
| Giá token gấp đôi | Chỉ +5,6%, lên 4.723 đ/việc [simulated]: rủi ro thấp, token chỉ chiếm ~5,6% tổng chi phí | Hoá đơn nhà cung cấp theo tháng | Không cần hành động trong pilot; theo dõi số lần chạy trung bình/yêu cầu | Kỹ sư trưởng agent |

Thứ tự ưu tiên theo dõi: làm lại > xem lại > lương > token. Giờ nhân viên chiếm 92,5% tổng chi phí [simulated], nên pilot phải đo phút xem lại và làm lại thật qua `staff_review_decision`, `staff_rework_completed`, không đo token.
