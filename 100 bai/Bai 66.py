def dem_gia_tri_lon_nhat(L):
    dem = 0
    max_value = float('-inf')

    for gia_tri in L:
        if gia_tri > max_value:
            max_value = gia_tri
            dem += 1
    return dem
L = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
so_luong = dem_gia_tri_lon_nhat(L)
print(f"Số lượng giá trị lớn hơn tất cả giá trị đứng trước nó là: {so_luong}")
