def tinh_gia_tri_trung_binh(L, a):
    if not L or a <= 0:
        return None
    so_luong_phan_tu = min(a, len(L))
    tong = sum(L[:so_luong_phan_tu])
    return tong / so_luong_phan_tu
danh_sach_so = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
so_phan_tu_dau_tien = 3
ket_qua = tinh_gia_tri_trung_binh(danh_sach_so, so_phan_tu_dau_tien)
print("Giá trị trung bình của", so_phan_tu_dau_tien, "phần tử đầu tiên là:", ket_qua)
