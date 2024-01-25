def tim_vi_tri_gia_tri_lon_nhat(lst):
    if not lst:
        print("List rỗng. Không có giá trị để xác định vị trí.")
        return None
    vi_tri_max = 0
    for i in range(1, len(lst)):
        if lst[i] > lst[vi_tri_max]:
            vi_tri_max = i
    return vi_tri_max
danh_sach = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
vi_tri_max = tim_vi_tri_gia_tri_lon_nhat(danh_sach)
if vi_tri_max is not None:
    print(f"Giá trị lớn nhất trong list là {danh_sach[vi_tri_max]} và nằm ở vị trí {vi_tri_max}.")
else:
    print("List không có giá trị nào.")
