"""Tự kiểm tra từng checkpoint của Lab 13.
Chạy trong src/:  python kiem_tra.py          (tất cả)
                  python kiem_tra.py cp1 cp4  (từng CP)
Mỗi dòng in [OK] hoặc [CHƯA]; số so với đáp án đối chiếu, nhận nếu lệch ≤ 2%.
"""
import io
import re
import sys
from contextlib import redirect_stdout
from pathlib import Path

import pandas as pd

import lab13  # lab13 đã cấu hình stdout sang UTF-8

REPORT = Path(__file__).resolve().parent.parent / 'report' / 'team'
ROOT = REPORT.parent.parent
ket_qua = []


def check(dk, mo_ta):
    ket_qua.append(bool(dk))
    print(f'  [{"OK" if dk else "CHƯA"}] {mo_ta}')


def gan(x, dap_an, sai_so=0.02):
    return abs(x - dap_an) <= abs(dap_an) * sai_so


def doc(ten):
    p = REPORT / ten
    return p.read_text(encoding='utf-8') if p.exists() else ''


def khong_con_cho_trong(ten, tu=None, den=None):
    s = doc(ten)
    if tu:
        s = s[s.find(tu):]
    if den and den in s:
        s = s[:s.find(den)]
    return '...' not in s


def cp1(runs, reqs):
    print('CP1 · Nhiệm vụ A')
    try:
        with redirect_stdout(io.StringIO()):
            lab13.kiem_tra_dap_an_biet_truoc()
        check(True, 'Ba phép thử A1 ĐẠT (1,20 · 1,25 · 1,25)')
    except Exception as e:
        check(False, f'Ba phép thử A1: {e!r}')
        return
    k = lab13.mo_hinh(runs, reqs)
    for ten, da in [('token', 245585), ('tool', 84000), ('chay_lai', 93804), ('xem_lai', 1780000),
                    ('lam_lai', 2264000), ('tong', 4373585), ('thanh_cong', 978), ('cps', 4472),
                    ('hoa_don_moi_yc', 274.7)]:
        check(gan(k[ten], da), f'A2 {ten} = {k[ten]:,.1f} (đáp án {da:,})')
    for loai, da in [('noi_dia', 2696), ('hang_nang', 8221), ('quoc_te', 22515), ('doi_tac', 10215)]:
        c = lab13.mo_hinh(runs, reqs[reqs.loai == loai])['cps']
        check(gan(c, da), f'A3 {loai} CPS = {c:,.0f} (đáp án {da:,})')
    s = doc('bang_chi_phi.md')
    check(khong_con_cho_trong('bang_chi_phi.md', '## A1', '## B1'), 'bang_chi_phi.md: phần A1–A4 không còn "..."')
    check('4.472' in s and '16,3' in s, 'bang_chi_phi.md có CPS 4.472 và tỉ lệ 16,3 lần')
    a2 = s[s.find('## A2'):s.find('## A3')]
    check(len(re.findall(r'\|\s*simulated\s*\|', a2)) >= 2, 'Bảng A2 có ít nhất 2 dòng nhãn simulated')


def cp2(runs, reqs):
    print('CP2 · Nhiệm vụ B')
    goc = lab13.mo_hinh(runs, reqs)['cps']
    dap_an = [4723, 4346, 6292, 3562, 6787, 3315, 5506, 4237, 4111]
    for (ten, kw), da in zip(lab13.KICH_BAN.items(), dap_an):
        c = lab13.mo_hinh(runs, reqs, **kw)['cps']
        check(gan(c, da), f'B1 {ten}: {c:,.0f} ({(c / goc - 1) * 100:+.1f}%, đáp án {da:,})')
    c = lab13.mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    check(gan(c, 6543), f'B2 cặp token×2 + xem lại×2: {c:,.0f} (đáp án 6.543)')
    ht = {g: lab13.mo_hinh(runs, reqs, max_lan_chay=g) for g in [1, 2, 3]}
    ht = {g: k['tong'] + (len(reqs) - k['thanh_cong']) * lab13.BASELINE for g, k in ht.items()}
    check(min(ht, key=ht.get) == 2, f'B3 giới hạn rẻ nhất cho công ty = 2 lần ({ht[2]:,.0f} đ)')
    check(khong_con_cho_trong('bang_chi_phi.md', '## B1'), 'bang_chi_phi.md: phần B1–B4 không còn "..."')
    check('11.743' in doc('bang_chi_phi.md'), 'B4 có con số 11.743 đ (0,98×)')


def cp3(runs, reqs):
    print('CP3 · Nhiệm vụ C')
    s = doc('bang_loi.md')
    bang = s[s.find('| Ca | Nhãn người 1'):s.find('**Tỉ lệ đồng thuận')]
    dong = [l for l in bang.splitlines() if re.match(r'\|\s*\d+\s*\|', l)]
    du = [l for l in dong if '...' not in l]
    check(len(du) == 20, f'Hai bộ nhãn độc lập đã điền đủ 20 ca ({len(du)}/20)')
    m = re.search(r'Tỉ lệ đồng thuận:\*\*\s*(\d+)\s*/\s*20', s)
    check(m and int(m.group(1)) >= 16, f'Đồng thuận ≥ 16/20 ({m.group(1) if m else "chưa điền"})')
    khac_phuc = s[s.find('## Bảng khắc phục'):]
    loai = ['Do người dùng', 'Hệ thống', 'Ngữ cảnh', 'Giới hạn hệ thống', 'Ngầm']
    check('...' not in khac_phuc and all(l in khac_phuc for l in loai), 'Bảng khắc phục đủ 5 loại, không còn "..."')
    hang = [l for l in khac_phuc.splitlines() if re.match(r'\|\s*\d+\s*\|', l)]
    check(hang and all('cả đội' not in l.lower() for l in hang),'Không ghi "cả đội" ở cột phụ trách')


def cp4(runs, reqs):
    print('CP4 · Nhiệm vụ D')
    check(lab13.co_mau(0.70, 0.75) in (1250, 1251), f'D1a = {lab13.co_mau(0.70, 0.75)} (đáp án 1.251)')
    check(lab13.co_mau(0.70, 0.76) == 859, f'D1e n = {lab13.co_mau(0.70, 0.76)} (đáp án 859)')
    import yaml
    p = REPORT / 'pilot_plan.yaml'
    try:
        y = yaml.safe_load(p.read_text(encoding='utf-8'))
        check(True, 'pilot_plan.yaml đọc được bằng yaml.safe_load')
    except Exception as e:
        check(False, f'pilot_plan.yaml lỗi YAML: {e}')
        return
    con_hoi = [l for l in p.read_text(encoding='utf-8').splitlines()
               if '?' in l and not l.lstrip().startswith('#')]
    check(not con_hoi, f'Không còn dấu "?" ngoài chú thích ({len(con_hoi)} dòng còn)')
    pl = y.get('pilot', {})
    for f in ['owner', 'scope', 'assignment', 'primary_metric', 'identifiability', 'stop_rules',
              'interim_looks', 'rollback', 'decision_date', 'simulated_inputs']:
        check(f in pl, f'Có trường {f}')
    rules = pl.get('stop_rules', [])
    du = [r for r in rules if all(t in r for t in ['NẾU', 'TRONG', 'THÌ', 'KHÔNG THÌ'])]
    check(len(du) >= 3, f'{len(du)} luật dừng đủ NẾU – TRONG – THÌ – KHÔNG THÌ (cần ≥ 3)')
    check(pl.get('primary_metric', {}).get('clusters_per_arm', 0) >= 20, 'Ít nhất 20 cụm mỗi nhóm')


def cp5(runs, reqs):
    print('CP5 · Nhiệm vụ E')
    chinh = ((reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0)).mean()
    check(gan(chinh, 0.8283), f'Chỉ số chính = {chinh:.2%} (đáp án 82,83%)')
    s = doc('chi_so.md')
    check('82,83' in s and '27,12' in s and '4,25' in s, 'chi_so.md có đủ 3 chỉ số tính thử')
    check(s.count('trace_id') >= 6 and khong_con_cho_trong('chi_so.md'), 'chi_so.md: ≥ 6 event có trace_id, không còn "..."')
    h = doc('ho_so_launch_v0.md')
    check(all(f'| {i} ·' in h for i in range(1, 8)), 'Hồ sơ đủ 7 mục')
    de_xuat = re.search(r'\*\*Đề xuất:\s*(Go có điều kiện|No-go|Go)\*\*', h)
    check(de_xuat, f'Đề xuất là một trong ba: {de_xuat.group(1) if de_xuat else "chưa chọn"}')
    check('Nhóm: ...' not in h, 'Hồ sơ đã điền tên nhóm, lớp')
    check('.../20' not in h, 'Hồ sơ đã điền tỉ lệ đồng thuận từ CP3')
    check(khong_con_cho_trong('phieu_cham.md'), 'phieu_cham.md đã chấm nhóm khác')
    co_prod = [f.name for f in REPORT.iterdir() if f.is_file() and 'production' in f.read_text(encoding='utf-8').lower()]
    check(not co_prod, f'Không có từ "production" trong report/team ({co_prod or "sạch"})')
    ca_nhan = [f.name for f in REPORT.glob('*_*.md') if re.match(r'\d\w*_', f.name)]
    check(ca_nhan, f'Có báo cáo cá nhân MSSV_HoTen.md ({len(ca_nhan)} file)')
    check('|   1 |        |' not in (ROOT / 'TEAM.md').read_text(encoding='utf-8'), 'TEAM.md đã điền thành viên')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    ham = dict(cp1=cp1, cp2=cp2, cp3=cp3, cp4=cp4, cp5=cp5)
    for ten in (sys.argv[1:] or list(ham)):
        ham[ten.lower()](runs, reqs)
        print()
    print(f'Tổng: {sum(ket_qua)}/{len(ket_qua)} mục OK')
