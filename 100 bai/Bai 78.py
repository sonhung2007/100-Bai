def tim_chuoi_ngan_nhat(danh_sach_chuoi):
    if not danh_sach_chuoi:
        return None
    chuoi_ngan_nhat = danh_sach_chuoi[0]
    for chuoi in danh_sach_chuoi[1:]:
        if len(chuoi) < len(chuoi_ngan_nhat):
            chuoi_ngan_nhat = chuoi
    return chuoi_ngan_nhat
danh_sach = ["abc", "xyz", "def", "ab", "ghij"]
ket_qua = tim_chuoi_ngan_nhat(danh_sach)
print("Chuỗi ngắn nhất trong danh sách là:", ket_qua)
