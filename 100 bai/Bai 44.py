chuoi = input("Nhập vào chuỗi: ")
cac_tu = chuoi.split()
if len(cac_tu) > 0:
    print(f"Từ đầu tiên trong chuỗi là: {cac_tu[0]}")
else:
    print("Chuỗi rỗng.")
