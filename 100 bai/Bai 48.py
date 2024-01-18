chuoi = input("Nhập vào chuỗi: ")
ky_tu_so = [int(ky_tu) for ky_tu in chuoi if ky_tu.isdigit()]
tong = sum(ky_tu_so)
print(f"Tổng các ký tự số trong chuỗi là: {tong}")
