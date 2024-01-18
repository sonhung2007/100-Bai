a = int(input("Nhập vào số nguyên dương a: "))
so_luong_uoc = 0
for i in range(1, a + 1):
    if a % i == 0:
        so_luong_uoc += 1
print(f"Số lượng ước của {a} là: {so_luong_uoc}")
