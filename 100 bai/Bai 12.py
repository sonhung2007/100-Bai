# Nhập vào 3 số a, b, c từ người dùng
a = float(input("Nhập vào số a: "))
b = float(input("Nhập vào số b: "))
c = float(input("Nhập vào số c: "))
d = (a + b) ** c
ket_qua = 100 <= d <= 200
print("Giá trị d là:", d)
print("Kết quả kiểm tra (d nằm trong khoảng từ 100 đến 200) là:", ket_qua)
