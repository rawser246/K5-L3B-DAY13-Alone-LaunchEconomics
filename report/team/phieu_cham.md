# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Alone (L3B, làm một mình: Đoàn Công Hải)
- Nhóm được chấm: GeminiPro (L3B), repo `miao1114/K5-L3B-DAY13-GeminiPro-LaunchEconomics`
- Ghi chú: nhóm Alone làm một mình, không có buổi duyệt chéo trực tiếp; chấm trên hồ sơ của nhóm GeminiPro (`ho_so_launch_v0.md`, `pilot_plan.yaml`, `bang_chi_phi.md`, `chi_so.md`) và chạy lại `src/lab13.py` của nhóm để đối chiếu số.

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | 10 | Go có điều kiện khớp số của nhóm (CPS 4.472 đ [simulated], 16,3×, 859/nhóm, 82,83% · 27,12% · 4,25%); nêu rõ con số bất lợi (power 0,642 nếu tác động thật 5 điểm, xem lại 100% = 0,98–1,03× [simulated]) kèm điều kiện xử lý. Lỗi nhỏ: mục 4, 6 ghi "Xong, có bằng chứng" dù pilot chưa chạy; lệch làm tròn 12.414 đ / 12.415 đ |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | 10 | Nhãn simulated ở mọi bảng và mục dùng cột `_simulated` (A2–A4, B1–B4, mục 1, 2, 3, 7, E2, `simulated_inputs`); loại quoc_te bằng số (1,88× [simulated], tỉ lệ ok 30,0% → 11,4% → 2,2%) và doi_tac (0,85× [simulated], điều khoản riêng); tính đúng hoà vốn ~6.200 yc/tháng (4.659 việc thành công) [simulated] |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | 10 | Chia ngẫu nhiên theo nhân viên 20 + 20 cụm, phân tầng theo depot, đối chứng đồng thời; ghi rõ đánh đổi (tối đa 1.000 < 1.251 → mde 6 điểm, 859/nhóm, DE 6,96); 3 luật dừng đủ 4 vế, ngưỡng an toàn đặt theo tỉ lệ hiện tại 4,25% / 3,97% (trần 6%), có thời hạn và Giám đốc vận hành có quyền dừng. Còn thiếu lịch thu mẫu và người phụ trách `interim_looks` |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Go có điều kiện

**Lý do:** Đồng thuận với đề xuất của nhóm, giữ nguyên 4 điều kiện trong hồ sơ (khoá chống trùng ca 7, 20; ký chấp nhận mde 6 điểm; thay phút simulated bằng đo thật; giảm xem lại theo bậc). Bổ sung một điều kiện: làm rõ tiến độ thu mẫu (đủ m ≥ 299 yêu cầu/người trước 05/01/2027) và người phụ trách `interim_looks` trước khi bắt đầu pilot.

**Một câu hỏi cho đội trình:** Mỗi nhân viên cần đạt tối thiểu m ≥ 299 yêu cầu (cỡ mẫu hiệu dụng 859 mỗi nhóm) nhưng kế hoạch chưa có lịch thu mẫu: nhóm ước tính mỗi ngày một nhân viên xử lý được bao nhiêu yêu cầu noi_dia + hang_nang để đủ mẫu trước ngày quyết định 05/01/2027, và ai theo dõi các lần `interim_looks`?

**Câu trả lời của đội trình (ghi lại tại buổi):** Không có buổi trình trực tiếp (nhóm Alone làm một mình, chấm trên hồ sơ); chưa nhận được câu trả lời.
