def la_so_armstrong(a):
    str_a = str(a)
    so_chu_so = len(str_a)
    tong_luy_thua = sum(int(chu_so) ** so_chu_so for chu_so in str_a)
    return a == tong_luy_thua
so_nguyen = int(input("Nhập một số nguyên: "))

if la_so_armstrong(so_nguyen):
    print(f"{so_nguyen} là số Armstrong.")
else:
    print(f"{so_nguyen} không phải là số Armstrong.")
