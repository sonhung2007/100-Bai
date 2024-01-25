chuoi_a = input("Chuỗi a: ")
chuoi_b = input("Chuỗi b: ")
vi_tri_xuat_hien = chuoi_a.find(chuoi_b)
if vi_tri_xuat_hien != -1:
    chuoi_a_sau_xoa = chuoi_a[:vi_tri_xuat_hien] + chuoi_a[vi_tri_xuat_hien + len(chuoi_b):]
    print(f"Sau khi xóa, chuỗi a: {chuoi_a_sau_xoa}")
else:
    print("Chuỗi b không tồn tại trong chuỗi a.")
