# Nhập vào chuỗi từ người dùng
chuoi = input("Nhập vào chuỗi: ")
so_ky_tu_in_hoa = 0
so_ky_tu_in_thuong = 0
so_ky_tu_so = 0
for ky_tu in chuoi:
    if ky_tu.isupper():
        so_ky_tu_in_hoa += 1
    elif ky_tu.islower():
        so_ky_tu_in_thuong += 1
    elif ky_tu.isdigit():
        so_ky_tu_so += 1
print(f"Số ký tự in hoa trong chuỗi là: {so_ky_tu_in_hoa}")
print(f"Số ký tự in thường trong chuỗi là: {so_ky_tu_in_thuong}")
print(f"Số ký tự số trong chuỗi là: {so_ky_tu_so}")
