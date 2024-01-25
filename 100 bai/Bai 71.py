def tim_vi_tri_chuoi_nhieu_tu_nhat(L):
    vi_tri = None
    so_tu_max = 0
    for i, chuoi in enumerate(L):
        so_tu = len(chuoi.split())
        if so_tu > so_tu_max:
            so_tu_max = so_tu
            vi_tri = i
    return vi_tri
L = input("Nhập vào list chuỗi, cách nhau bởi dấu cách: ").split()
vi_tri = tim_vi_tri_chuoi_nhieu_tu_nhat(L)
if vi_tri is not None:
    print(f"Chuỗi có nhiều từ nhất ở vị trí {vi_tri}: {L[vi_tri]}")
else:
    print("Không có chuỗi trong list.")
