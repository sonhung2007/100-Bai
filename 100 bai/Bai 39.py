# Nhập vào số nguyên dương n từ người dùng
n = int(input("Nhập vào số nguyên dương n: "))
chuoi_n = str(n)
so_chu_so_chan = 0
so_chu_so_le = 0
for chu_so in chuoi_n:
    if int(chu_so) % 2 == 0:
        so_chu_so_chan += 1
    else:
        so_chu_so_le += 1
print(f"Số nguyên dương {n} có:")
print(f"{so_chu_so_chan} chữ số chẵn.")
print(f"{so_chu_so_le} chữ số lẻ.")
