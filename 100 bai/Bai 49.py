chuoi = input("Nhập vào chuỗi: ")
tong = 0
so_hien_tai = ''
for ky_tu in chuoi:
    if ky_tu.isdigit():
        so_hien_tai += ky_tu
    elif so_hien_tai:
        tong += int(so_hien_tai)
        so_hien_tai = ''
if so_hien_tai:
    tong += int(so_hien_tai)
print(f"Tổng của các con số trong chuỗi là: {tong}")
