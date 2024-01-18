# Khởi tạo biến số lớn nhất và số nhỏ nhất
so_lon_nhat = float('-inf')
so_nho_nhat = float('inf')
while True:
    so = int(input("Nhập một số nguyên (nhập -1 để kết thúc): "))
    if so == -1:
        break
    so_lon_nhat = max(so, so_lon_nhat)
    so_nho_nhat = min(so, so_nho_nhat)
if so_lon_nhat != float('-inf'):
    print(f"Số lớn nhất là: {so_lon_nhat}")
    print(f"Số nhỏ nhất là: {so_nho_nhat}")
else:
    print("Dãy số trống.")
