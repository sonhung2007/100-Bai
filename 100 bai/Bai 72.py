def tim_chuoi_voi_vi_tri_in_hoa_lon_nhat(L):
    chuoi_max = None
    vi_tri_in_hoa_max = -1
    for chuoi in L:
        for i, ky_tu in enumerate(chuoi):
            if ky_tu.isupper() and i > vi_tri_in_hoa_max:
                vi_tri_in_hoa_max = i
                chuoi_max = chuoi
    return chuoi_max, vi_tri_in_hoa_max
L = input("Nhập vào list chuỗi, cách nhau bởi dấu cách: ").split()
chuoi_max, vi_tri = tim_chuoi_voi_vi_tri_in_hoa_lon_nhat(L)
if chuoi_max is not None:
    print(f"Chuỗi có vị trí ký tự in hoa lớn nhất là '{chuoi_max}', tại vị trí {vi_tri}.")
else:
    print("Không có chuỗi trong list.")
