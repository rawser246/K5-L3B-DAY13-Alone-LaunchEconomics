# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: Alone
- Lớp: L3B
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Trả lời bốn câu hỏi của Gate 2a cho trợ lý hoàn phí LogiX-VN (có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, pilot thiết kế thế nào) bằng số tính từ 1.200 yêu cầu và 1.624 lần chạy giả lập. Mọi con số do `src/lab13.py` tính; `src/kiem_tra.py` đối chiếu với đáp án (lệch ≤ 2%).

## 3. Giải pháp

- **A · Chi phí** ([bang_chi_phi.md](bang_chi_phi.md)): tử số cộng token + tool của mọi lần chạy, kể cả lỗi, cộng phút xem lại và làm lại; mẫu số chỉ đếm việc thành công. Tách theo loại yêu cầu và cộng chi phí cố định 40 triệu/tháng.
- **B · Độ nhạy** ([bang_chi_phi.md](bang_chi_phi.md)): gọi lại `mo_hinh` cho 9 kịch bản, 1 cặp, giới hạn số lần chạy (chi phí cả hệ thống) và kịch bản xem lại 100%.
- **C · Bảng lỗi** ([bang_loi.md](bang_loi.md)): hai người gắn nhãn độc lập 20 ca theo năm loại Google PAIR, so nhãn, chọn 5 ca để gán cách khắc phục đo được.
- **D · Pilot** ([pilot_plan.yaml](pilot_plan.yaml)): tính cỡ mẫu cho ba cách chia, chọn chia theo nhân viên 20 + 20, chấp nhận mức chênh 6 điểm, đặt 3 luật dừng dựa trên tỉ lệ mở lại hiện tại 4,25%.
- **E · Chỉ số và hồ sơ** ([chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md)): tính thử 3 chỉ số, 10 event có trace_id, 3 dòng rủi ro kinh tế, gom thành hồ sơ 7 mục.

## 4. Kết quả

- Chi phí mỗi việc thành công **4.472 đ** [simulated], gấp 16,3× hoá đơn token chia số yêu cầu; giờ nhân viên chiếm 92,5%.
- Cả hệ thống **5.865 đ/yêu cầu = 0,49×** nhân viên tự làm [simulated]; quoc_te 1,88× nên bị loại khỏi phạm vi.
- Yếu tố nhạy nhất: làm lại (+51,8%), xem lại (+40,7%), lương (+23,1%) [simulated].
- Xem lại 100% thì 0,98–1,03× [simulated]: gần như không tiết kiệm.
- Pilot: theo nhân viên 20 + 20, 859/nhóm, DE 6,96; power 0,64 nếu tác động thật chỉ 5 điểm.
- **Đề xuất: Go có điều kiện** cho noi_dia + hang_nang.
- Kết quả duyệt chéo nhóm nhận được từ hội đồng: chưa có (làm một mình, không có nhóm chấm lại).
- Nhóm làm hội đồng chấm hồ sơ GeminiPro: 30/30, Go có điều kiện (`phieu_cham.md`).

## 5. Khó khăn và cách xử lý

- Lệnh cài đặt trong README viết cho bash, không chạy trong PowerShell (`source`, `export` không tồn tại) → dùng `.\.venv\Scripts\Activate.ps1`.
- Console Windows lỗi `UnicodeEncodeError` khi in tiếng Việt → cấu hình stdout sang UTF-8 trong `lab13.py`.
- Làm một mình nên không có hai người gắn nhãn độc lập ở CP3: thay bằng hai lượt gắn của cùng một người, cách nhau ~6 phút, thứ tự ca đã xáo; trùng 18/20 = 90% (`docs/cp3_gan_nhan/`), và ghi rõ hạn chế này trong `bang_loi.md`.
- File nháp và nội dung sai trong `chi_so.md` (nhầm chỉ số an toàn 4,25% thành chỉ số chính) được phát hiện khi đối chiếu với `kiem_tra.py` và đã khôi phục về số do `lab13.py` tính.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại, làm lại là số giả lập; cần thay bằng phút đo thật từ event `staff_review_decision`, `staff_rework_completed` sau tuần 1 của pilot.
- Chỉ số trong đợt chạy thử không có đối chứng, nên chưa nói được trợ lý tạo ra bao nhiêu phần chênh so với baseline 0,70.
- Pilot chỉ đủ mẫu cho mức chênh 6 điểm; muốn thấy 5 điểm cần thêm nhân viên hoặc kéo dài thời gian.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure"
- Tài liệu statsmodels, `NormalIndPower`
- Có dùng Claude Code (trợ lý AI) để viết code `lab13.py`, `kiem_tra.py` và soạn bản nháp hồ sơ; số liệu được đối chiếu bằng `kiem_tra.py` với đáp án trong hướng dẫn chi tiết.
