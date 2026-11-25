# Báo cáo cá nhân — DoanCongHai-2A202603739

## 1. Thông tin thành viên

- Họ tên: Đoàn Công Hải
- MSSV: 2A202603739
- Email: 26ai.haidc@vinuni.edu.vn
- Vai trong nhóm: cả bốn vai (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ), vì nhóm Alone làm một mình.

## 2. Phần việc phụ trách

Toàn bộ năm nhiệm vụ A–E của Lab 13: mô hình chi phí, bảng độ nhạy, bảng lỗi, kế hoạch pilot, chỉ số và hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN.

## 3. Đóng góp cụ thể

- **A · Chi phí:** viết `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong` (ba phép thử 1,20 · 1,25 · 1,25 ĐẠT) và `mo_hinh`. Chi phí mỗi việc thành công 4.472 đ [simulated], gấp 16,3× hoá đơn token chia số yêu cầu (274,7 đ); giờ nhân viên chiếm 92,5% [simulated]. Theo loại: noi_dia 0,22×, hang_nang 0,69×, quoc_te 1,88×, doi_tac 0,85× so với 12.000 đ [simulated].
- **B · Độ nhạy:** 9 kịch bản, ba yếu tố nhạy nhất là làm lại (+51,8%), xem lại (+40,7%), lương (+23,1%) [simulated]; giới hạn rẻ nhất cho công ty là 2 lần chạy (6.901.220 đ cả hệ thống); xem lại 100% thì 11.743 đ = 0,98× [simulated].
- **C · Bảng lỗi:** gắn nhãn 20 ca theo năm loại Google PAIR, bảng khắc phục 5 ca có cách phát hiện đo được và một vai trò phụ trách.
- **D · Pilot:** cỡ mẫu D1 (1.251 theo yêu cầu; 3.103 theo nhân viên m = 75; tối đa 1.000 với 20 người/nhóm; tối đa 300 theo depot; mức chênh 6 điểm cần 859/nhóm, m ≥ 299, DE 6,96). Chọn chia theo nhân viên 20 + 20, chấp nhận power 0,64 nếu tác động thật chỉ 5 điểm; 3 luật dừng dựa trên tỉ lệ mở lại hiện tại 4,25%; lịch pilot 01/12/2026 – 05/01/2027.
- **E · Chỉ số và hồ sơ:** ba chỉ số tính thử 82,83% · 27,12% · 4,25% (trong phạm vi 92,26% · 21,09% · 3,97%), 10 event có trace_id, 5 dòng rủi ro kinh tế, hồ sơ 7 mục với đề xuất Go có điều kiện.

## 4. Bằng chứng

- `src/lab13.py`: chạy `python lab13.py` in đủ bảng CP1, CP2, CP4, CP5.
- `src/kiem_tra.py`: tự đối chiếu số với đáp án trong hướng dẫn chi tiết (lệch ≤ 2%).
- `report/team/bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`, `group_report.md`.

## 5. Công cụ AI đã dùng

- Claude Code: hỗ trợ viết code `lab13.py`, `kiem_tra.py` và soạn bản nháp hồ sơ.
- Cách kiểm tra: mọi con số trong hồ sơ được in ra từ `lab13.py` và đối chiếu bằng `kiem_tra.py` với đáp án; đã phát hiện và sửa một bản `chi_so.md` có số sai (ghi chỉ số an toàn 4,25% thành chỉ số chính, số token và tỉ lệ lỗi không khớp dữ liệu) bằng cách tính lại từ CSV.

## 6. Tự đánh giá

- Làm tốt: A, B, D khớp đáp án; hồ sơ nêu rõ con số bất lợi (xem lại 100% thì 0,98–1,03× [simulated], power 0,64 ở mức 5 điểm) và thu hẹp phạm vi có lý do bằng số.
- Chưa tốt: CP3 làm một mình nên không có hai bộ nhãn thật sự độc lập; thay bằng hai lượt gắn của chính mình (thứ tự xáo, cách nhau ~6 phút), trùng 18/20 = 90%. Hai lượt quá gần nhau nên độ trùng có thể cao hơn thực tế. Không có buổi duyệt chéo trực tiếp: chấm hồ sơ nhóm GeminiPro trên file (30/30, Go có điều kiện, `phieu_cham.md`).
- Bài học: chi phí thật của agent nằm ở giờ nhân viên chứ không ở token; pilot phải tính cỡ mẫu theo cụm trước khi chọn cách chia.
