so_nguyen = int(input("Nhập số nguyên: "))
chuoi_so = str(so_nguyen)[::-1]
chuoi_so_phan_tach = '.'.join([chuoi_so[i:i+3] for i in range(0, len(chuoi_so), 3)])
print(f"Đổi sang chuỗi rồi in ra: {chuoi_so_phan_tach[::-1]}")
