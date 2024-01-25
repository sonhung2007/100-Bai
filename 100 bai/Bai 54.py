def tim_so_nho_nhat(L, a, b):
    if not (0 <= a < b < len(L)):
        print("Vui lòng nhập lại giá trị của a và b sao cho 0 <= a < b < len(L).")
        return
    so_nho_nhat = min(L[a:b+1])
    print("Số nhỏ nhất từ vị trí a đến vị trí b là:", so_nho_nhat)
L = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
a = int(input("Nhập giá trị của a (số nguyên dương): "))
b = int(input("Nhập giá trị của b (số nguyên dương, lớn hơn a): "))
tim_so_nho_nhat(L, a, b)
