chuoi = input("Nhập vào 3 số nguyên, mỗi số cách nhau bởi dấu phẩy: ")
cac_so_nguyen = [int(x) for x in chuoi.split(',')]
tong = sum(cac_so_nguyen)
print(f"Tổng của 3 số nguyên là: {tong}")
