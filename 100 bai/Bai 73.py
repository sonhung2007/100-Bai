def bang_cuu_chuong_so_lon_hon(a, b):
    so_lon_hon = max(a, b)
    print(f"Bảng cửu chương của số {so_lon_hon}:")
    for i in range(1, 11):
        print(f"{so_lon_hon} x {i} = {so_lon_hon * i}")
so1 = int(input("Nhập số nguyên thứ nhất: "))
so2 = int(input("Nhập số nguyên thứ hai: "))
bang_cuu_chuong_so_lon_hon(so1, so2)
