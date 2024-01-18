import re
chuoi = input("Nhập vào chuỗi: ")
chuoi = re.sub(r'[^a-zA-Z\s]', '', chuoi)
cac_tu = chuoi.split()
so_tu = len(cac_tu)
print(f"Số từ trong chuỗi là: {so_tu}")
