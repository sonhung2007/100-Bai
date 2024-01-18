n = int(input("Nhập vào số nguyên dương n: "))
chuoi_n = str(n)
tong_chu_so = 0
for chu_so in chuoi_n:
    tong_chu_so += int(chu_so)
print(f"Tổng các chữ số của {n} là: {tong_chu_so}")
