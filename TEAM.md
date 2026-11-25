# Team

## Thông tin nhóm

- Tên nhóm: Alone (làm một mình)
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-Alone-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo, nhánh nộp, commit chốt: https://github.com/rawser246/K5-L3B-DAY13-Alone-LaunchEconomics · nhánh `main` · commit chốt: điền sau khi push

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Đoàn Công Hải | 2A202603739 | 26ai.haidc@vinuni.edu.vn | rawser246 | Cả bốn vai: người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Làm một mình nên một người giữ cả bốn vai. Hạn chế: CP3 không có hai người gắn nhãn thật sự độc lập (hai bộ nhãn là hai lượt của cùng một người, thứ tự ca đã xáo; xem `report/team/bang_loi.md` và `docs/cp3_gan_nhan/`).

## Cá nhân

Báo cáo cá nhân: [report/team/2A202603739_DoanCongHai.md](report/team/2A202603739_DoanCongHai.md).

## DoanCongHai-2A202603739

### Phần việc phụ trách

- Toàn bộ năm nhiệm vụ A–E: code `src/lab13.py`, sáu file hồ sơ trong `report/team/`, báo cáo nhóm.

### Đóng góp cụ thể

- A, B: viết ba hàm A1, `mo_hinh`, tách theo loại, chi phí cố định, bảng độ nhạy B1–B4 (CPS 4.472 đ [simulated], 16,3× hoá đơn token).
- C: gắn nhãn 20 ca, bảng khắc phục 5 ca đủ năm loại.
- D: tính cỡ mẫu D1 (1.251 · 3.103 · 1.000 · 300 · 859/m ≥ 299), viết `pilot_plan.yaml` với 3 luật dừng.
- E: tính ba chỉ số (82,83% · 27,12% · 4,25%), 10 event có trace_id, 5 dòng rủi ro kinh tế, hồ sơ launch v0 với đề xuất Go có điều kiện.

### Bằng chứng

- `python lab13.py` in đủ CP1, CP2, CP4, CP5; `python kiem_tra.py` đối chiếu với đáp án (lệch ≤ 2%).
- Các file: `src/lab13.py`, `src/kiem_tra.py`, `report/team/*.md`, `report/team/pilot_plan.yaml`.
