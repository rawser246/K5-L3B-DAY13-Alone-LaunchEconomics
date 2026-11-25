# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot.

Nhóm: Alone · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc [simulated], gấp 16,3× hoá đơn token chia số yêu cầu (274,7 đ); phạm vi noi_dia + hang_nang 3.414 đ, cộng cố định 4.599 đ [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Làm lại ±51,8% · xem lại ±40,7% · lương +23,1%; giá token chỉ +5,6% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống 5.865 đ/yêu cầu = 0,49× của 12.000 đ; phạm vi pilot 0,38× (0,48× nếu khối lượng còn một nửa); xem lại 100% thì 0,98–1,03× [simulated] | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử: chính 82,83%, bỏ qua gợi ý 27,12%, mở lại 7 ngày 4,25%; trong phạm vi pilot 92,26% · 21,09% · 3,97% (chưa có đối chứng); 10 event đều có trace_id | Xong, có bằng chứng (`chi_so.md`) | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | 20 ca, 5 loại PAIR; đồng thuận 18/20 = 90% (hai lượt của cùng một người, thứ tự xáo), đã thống nhất ca 9 → Do người dùng, ca 13 → Giới hạn hệ thống; 5 cách khắc phục có ngưỡng đo được; ca 7, 20 (báo hoàn sai, hoàn trùng) phải sửa trước pilot | Xong, có bằng chứng (`bang_loi.md`) | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20, mde 6 điểm, 859/nhóm, m ≥ 299, DE 6,96; power 0,64 nếu tác động thật 5 điểm; 3 luật dừng; ~10 ngày ở bước 0.50 để đủ m, quyết định 05/01/2027 | Xong, có bằng chứng (`pilot_plan.yaml`) | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại ×2 → 6.787 đ; xem lại 100% → 0,98×; khối lượng một nửa → +2.370 đ/việc [simulated] | Giả lập | PM trợ lý hoàn phí |

**Đề xuất: Go có điều kiện** cho pilot chỉ noi_dia + hang_nang (loại quoc_te 1,88× và doi_tac 0,85× [simulated]). Con số bất lợi: xem lại 100% thì không tiết kiệm (0,98–1,03× [simulated]), và pilot chỉ thấy được mức chênh 6 điểm (power 0,64 ở 5 điểm).

- Sửa khoá chống trùng và đối soát sổ cái (ca 7, 20) trước ngày bắt đầu · Kỹ sư trưởng agent · kiểm tra trước ngày bắt đầu pilot.
- Ký chấp nhận mức chênh 6 điểm (power 0,64 ở 5 điểm) · Giám đốc vận hành · kiểm tra trước ngày bắt đầu pilot.
- Bật đủ 10 event có trace_id; thay phút simulated bằng phút đo thật sau tuần 1 · PM trợ lý hoàn phí · kiểm tra cuối tuần 1.
- Kế hoạch giảm xem lại theo bậc, mục tiêu mỗi lần xem lại < 5 phút (B4) · Trưởng nhóm CSKH · kiểm tra cuối bước rollout 0.25.
