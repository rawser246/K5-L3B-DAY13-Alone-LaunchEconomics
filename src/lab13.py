"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas, statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.

Chạy từng phần:  python lab13.py cp1 | cp2 | cp4 | cp5   (không tham số = chạy tất cả)
"""
import math
import sys
from statistics import NormalDist

import pandas as pd

if hasattr(sys.stdout, 'reconfigure'):  # in được tiếng Việt trên Windows console
    sys.stdout.reconfigure(encoding='utf-8')

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000   # chi phí cố định của trợ lý mỗi tháng
YC_THANG = 45_000            # số yêu cầu hoàn phí mỗi tháng ở quy mô đầy đủ
PHAM_VI = ['noi_dia', 'hang_nang']


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print(f'  so_lan_chay_ky_vong(0.8, 2)               = {so_lan_chay_ky_vong(0.8, 2):.2f}')
    print(f'  so_lan_chay_ky_vong(0.8)                  = {so_lan_chay_ky_vong(0.8):.2f}')
    print(f'  he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) = {he_so_chi_phi_moi_viec_thanh_cong(0.8, 3):.2f}')
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy, kể cả lần lỗi (tử số).
    - thanh_cong: chỉ đếm ket_qua == 'thanh_cong' (mẫu số).
    - xem_lai, lam_lai: từ cột *_simulated → số GIẢ LẬP.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:  # B1, B3: bỏ lần chạy vượt giới hạn, yêu cầu vượt coi là chuyển nhân viên
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


def tieu_de(s):
    print('\n' + '=' * 78 + f'\n{s}\n' + '=' * 78)


# ---------- CP1 · A2, A3, A4 ----------
def cp1(runs, reqs):
    tieu_de('CP1 · A1 · Ba phép thử')
    kiem_tra_dap_an_biet_truoc()

    tieu_de('CP1 · A2 · Mô hình chi phí từ trace')
    kq = mo_hinh(runs, reqs)
    nhan = dict(token='đo từ trace', tool='đo từ trace', chay_lai='đo từ trace',
                xem_lai='simulated', lam_lai='simulated', tong='có phần simulated',
                thanh_cong='', cps='simulated', hoa_don_moi_yc='đo từ trace')
    for ten, gt in kq.items():
        print(f'  {ten:15s} {gt:>14,.1f}   {nhan[ten]}')
    print(f'  Số lần gọi tool: {runs.tool_calls.sum():,} · phút xem lại: {reqs.phut_xem_lai_simulated.sum():,} '
          f'· phút làm lại: {reqs.phut_lam_lai_simulated.sum():,} (simulated)')
    print(f'  CPS gấp {kq["cps"] / kq["hoa_don_moi_yc"]:.1f} lần hoá đơn chia số yêu cầu')
    for k in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f'  Tỉ trọng {k:8s}: {kq[k] / kq["tong"] * 100:5.1f}%')
    print(f'  Giờ nhân viên chiếm {(kq["xem_lai"] + kq["lam_lai"]) / kq["tong"] * 100:.1f}% tổng chi phí')
    khong_tc = len(reqs) - kq['thanh_cong']
    ca_he = (kq['tong'] + khong_tc * BASELINE) / len(reqs)
    print(f'  Cả hệ thống mỗi yêu cầu (cộng {khong_tc} ca không thành công × 12.000 đ): '
          f'{ca_he:,.0f} đ = {ca_he / BASELINE:.2f}× (simulated)')

    tieu_de('CP1 · A3 · Tách theo loại yêu cầu')
    print(f'  {"loai":10s} {"so_yc":>6s} {"ti_le_tc":>9s} {"lan/yc":>7s} {"cps":>9s} {"vs12k":>6s}')
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        r = reqs[reqs.loai == loai]
        k = mo_hinh(runs, r)
        lan = runs[runs.request_id.isin(r.request_id)].shape[0] / len(r)
        print(f'  {loai:10s} {len(r):6d} {k["thanh_cong"] / len(r) * 100:8.1f}% {lan:7.2f} '
              f'{k["cps"]:9,.0f} {k["cps"] / BASELINE:5.2f}×')
    print('  Tỉ lệ status=ok theo lần thử (attempt) và loại:')
    m = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    m['ok'] = (m.status == 'ok').astype(float)
    bang = m.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean') * 100
    print(bang.round(1).to_string().replace('\n', '\n  '))

    tieu_de('CP1 · A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)')
    pv = reqs[reqs.loai.isin(PHAM_VI)]
    k = mo_hinh(runs, pv)
    print(f'  Phạm vi: {len(pv)} yêu cầu, {k["thanh_cong"]} thành công, tổng {k["tong"]:,.0f} đ, '
          f'CPS {k["cps"]:,.0f} đ (simulated)')
    for ten, kl in [('45.000 yc/tháng', YC_THANG), ('Một nửa khối lượng', YC_THANG / 2)]:
        tc_thang = kl * k['thanh_cong'] / len(reqs)
        cd = CO_DINH_THANG / tc_thang
        print(f'  {ten:20s} tc/tháng {tc_thang:8,.0f}  cố định/việc {cd:6,.0f} đ  '
              f'CPS+cố định {k["cps"] + cd:6,.0f} đ = {(k["cps"] + cd) / BASELINE:.2f}×')


# ---------- CP2 · B1–B4 ----------
KICH_BAN = {
    'Giá token gấp đôi': dict(gia_vao=52, gia_ra=260),
    'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
    'Xem lại gấp đôi': dict(he_so_xem_lai=2),
    'Xem lại giảm một nửa': dict(he_so_xem_lai=0.5),
    'Làm lại gấp đôi': dict(he_so_lam_lai=2),
    'Làm lại giảm một nửa': dict(he_so_lam_lai=0.5),
    'Lương tăng 25%': dict(luong_phut=2500),
    'Tối đa 2 lần chạy': dict(max_lan_chay=2),
    'Chỉ 1 lần chạy': dict(max_lan_chay=1),
}


def cp2(runs, reqs):
    tieu_de('CP2 · B1 · Đổi từng yếu tố (simulated)')
    goc = mo_hinh(runs, reqs)['cps']
    print(f'  {"Gốc (A2)":25s} {goc:8,.0f}')
    for ten, kw in KICH_BAN.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        print(f'  {ten:25s} {cps:8,.0f} {(cps / goc - 1) * 100:+6.1f}%')

    tieu_de('CP2 · B2 · Đổi một cặp')
    cps = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    print(f'  Token ×2 + xem lại ×2: {cps:,.0f} đ ({(cps / goc - 1) * 100:+.1f}%)')

    tieu_de('CP2 · B3 · Giới hạn số lần chạy và chi phí cả hệ thống (simulated)')
    for g in [1, 2, 3]:
        k = mo_hinh(runs, reqs, max_lan_chay=g)
        ktc = len(reqs) - k['thanh_cong']
        print(f'  {g} lần: trợ lý {k["tong"]:12,.0f}  không TC {ktc:4d}  '
              f'cả hệ thống {k["tong"] + ktc * BASELINE:12,.0f}  CPS {k["cps"]:7,.0f}')

    tieu_de('CP2 · B4 · Xem lại 100% (noi_dia + hang_nang, simulated)')
    pv = reqs[reqs.loai.isin(PHAM_VI)]
    r = runs[runs.request_id.isin(pv.request_id)]
    co_ok = r[r.status == 'ok'].request_id.nunique()
    so_lam_lai = int((pv.ket_qua == 'lam_lai').sum())
    tc = int((pv.ket_qua == 'thanh_cong').sum())
    may = (r.tokens_in / 1000 * GIA_VAO + r.tokens_out / 1000 * GIA_RA + r.tool_calls * GIA_TOOL).sum()
    tb_lam_lai = reqs.loc[reqs.ket_qua == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    tv_lam_lai = reqs.loc[reqs.ket_qua == 'lam_lai', 'phut_lam_lai_simulated'].median()
    print(f'  Yêu cầu có ≥1 lần ok: {co_ok} · ca lam_lai: {so_lam_lai} · thành công: {tc} · token+tool: {may:,.0f} đ')
    for phut_ll in [9, tb_lam_lai]:
        tong = co_ok * 5 * LUONG_PHUT + so_lam_lai * phut_ll * LUONG_PHUT + may
        hoa_von = (BASELINE * tc - may - so_lam_lai * phut_ll * LUONG_PHUT) / (co_ok * LUONG_PHUT)
        print(f'  Làm lại {phut_ll:4.1f} phút/ca: tổng {tong:12,.0f} đ → {tong / tc:7,.0f} đ/việc = '
              f'{tong / tc / BASELINE:.2f}× · hoà vốn khi xem lại ≤ {hoa_von:.1f} phút')
    print(f'  Phút làm lại thực tế trong dữ liệu: trung bình {tb_lam_lai:.1f}, trung vị {tv_lam_lai:.1f} (simulated)')


# ---------- CP4 · D1 ----------
def co_mau(p1, p2, alpha=0.05, power=0.8):
    za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
    pb = (p1 + p2) / 2
    return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                      + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)


def cp4(runs, reqs):
    # ---- D1 · Cỡ mẫu ----
    icc = 0.02
    tieu_de('CP4 · D1 · Cỡ mẫu (baseline 0,70; +5 điểm; alpha 0,05; power 0,8; ICC 0,02)')
    n = co_mau(0.70, 0.75)
    print(f'  a) Theo yêu cầu: {n:,} yêu cầu mỗi nhóm')
    de = 1 + (75 - 1) * icc
    nb = math.ceil(n * de)
    print(f'  b) Theo nhân viên m=75: DE = {de:.2f}, n = {nb:,} mỗi nhóm → {math.ceil(nb / 75)} người/nhóm, '
          f'tổng {2 * math.ceil(nb / 75)} > 40 → không đủ người')
    print(f'  c) 20 nhân viên/nhóm: tối đa c/ICC = {20 / icc:,.0f} < {n:,} → không đạt')
    print(f'  d) 6 depot/nhóm: tối đa {6 / icc:,.0f}')
    n6 = co_mau(0.70, 0.76)
    m = n6 * (1 - icc) / (20 - n6 * icc)
    m = math.ceil(m)
    print(f'  e) Mức chênh 6 điểm: n = {n6} mỗi nhóm; 20 người/nhóm cần m ≥ {m} yc/người '
          f'(DE = {1 + (m - 1) * icc:.2f})')
    try:
        from statsmodels.stats.power import NormalIndPower
        from statsmodels.stats.proportion import proportion_effectsize
        es = proportion_effectsize(0.75, 0.70)
        print(f'  Kiểm tra statsmodels (theo yêu cầu, +5 điểm): {NormalIndPower().solve_power(es, alpha=0.05, power=0.8):,.0f}')
        print(f'  Power nếu tác động thật chỉ 5 điểm với n hiệu dụng {n6}: '
              f'{NormalIndPower().power(es, nobs1=n6, alpha=0.05):.2f}')
    except ImportError:
        print('  (chưa cài statsmodels: bỏ qua phần kiểm tra)')
    print(f'  Tỉ lệ mo_lai_trong_7_ngay hiện tại: {reqs.mo_lai_trong_7_ngay.mean() * 100:.2f}% '
          f'({reqs.mo_lai_trong_7_ngay.sum()}/{len(reqs)}); trong phạm vi: '
          f'{reqs[reqs.loai.isin(PHAM_VI)].mo_lai_trong_7_ngay.mean() * 100:.2f}%')
    # Thời gian cần để mỗi nhân viên đạt m yêu cầu trong phạm vi (40 nhân viên, 45.000 yc/tháng)
    ti_le_pv = reqs.loai.isin(PHAM_VI).mean()
    yc_ngay = YC_THANG / 40 * ti_le_pv / 30
    print(f'  Mỗi nhân viên nhận ~{yc_ngay:.1f} yc/ngày trong phạm vi ({ti_le_pv * 100:.1f}% của 45.000/40/30) '
          f'→ đạt m = {m} sau ~{math.ceil(m / yc_ngay)} ngày ở bước 0.50')

    # ---- D2 – 5 câu “tách được tác động” ----
    tieu_de('CP4 · D2 – 5 câu "tách được tác động"')
    print('  1. Đối chứng chạy cùng thời gian: Có, 20 nhân viên đối chứng làm cùng tuần, cùng depot.')
    print('  2. Phân tầng ngẫu nhiên hay do người chọn: Bốc thăm bằng code với seed, phân tầng theo depot.')
    print('  3. Rủi ro gián tiếp và cách giảm: Chia sẻ câu trả lời trong depot; giảm bằng quyền truy cập theo tài khoản, log lượt mở trợ lý theo staff_id.')
    print('  4. Chỉ số chính, ngưỡng, ngày quyết định đã viết trước: Có, chốt trong file này trước ngày bắt đầu.')
    print('  5. Ít nhất 20 cụm mỗi nhóm: Có, đúng 20 nhân viên mỗi nhóm.')

    return {
        'd1_n': n,
        'd1_de': de,
        'd1_nb': nb,
        'd1e_n': n6,
        'd1e_m': m,
        'ti_le_mo_lai_7_ngay': reqs['mo_lai_trong_7_ngay'].mean(),
    }


# ---------- CP5 · E1 ----------
def cp5(runs, reqs):
    tieu_de('CP5 · E1 · Tính thử ba chỉ số trên 1.200 yêu cầu')
    chinh = (reqs.dong_trong_24h == 1) & (reqs.mo_lai_trong_7_ngay == 0)
    xem = reqs[reqs.duoc_xem_lai == 1]
    bo_qua = xem.quyet_dinh_xem_lai.isin(['sua', 'bo'])
    an_toan = reqs.mo_lai_trong_7_ngay == 1
    print(f'  Chính  : {chinh.mean() * 100:.2f}% ({chinh.sum()}/{len(reqs)})')
    print(f'  Dùng   : {bo_qua.mean() * 100:.2f}% ({bo_qua.sum()}/{len(xem)})')
    print(f'  An toàn: {an_toan.mean() * 100:.2f}% ({an_toan.sum()}/{len(reqs)})')
    pv = reqs[reqs.loai.isin(PHAM_VI)]
    chinh_pv = (pv.dong_trong_24h == 1) & (pv.mo_lai_trong_7_ngay == 0)
    xem_pv = pv[pv.duoc_xem_lai == 1]
    bo_qua_pv = xem_pv.quyet_dinh_xem_lai.isin(['sua', 'bo'])
    print(f'  Trong phạm vi noi_dia + hang_nang: chính {chinh_pv.mean() * 100:.2f}% ({chinh_pv.sum()}/{len(pv)}) · '
          f'dùng {bo_qua_pv.mean() * 100:.2f}% ({bo_qua_pv.sum()}/{len(xem_pv)}) · '
          f'an toàn {pv.mo_lai_trong_7_ngay.mean() * 100:.2f}% ({pv.mo_lai_trong_7_ngay.sum()}/{len(pv)})')
    print(f'  Tỉ lệ làm lại trong phạm vi: {(pv.ket_qua == "lam_lai").mean() * 100:.1f}% (cả mẫu '
          f'{(reqs.ket_qua == "lam_lai").mean() * 100:.1f}%)')
    print(f'  Tỉ lệ được xem lại: {reqs.duoc_xem_lai.mean() * 100:.1f}%')


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    chon = sys.argv[1:] or ['cp1', 'cp2', 'cp4', 'cp5']
    for ten in chon:
        {'cp1': cp1, 'cp2': cp2, 'cp4': cp4, 'cp5': cp5}[ten.lower()](runs, reqs)
