a = float(input("Nhập vào số thực dương a: "))
b = float(input("Nhập vào số thực dương b: "))
c = float(input("Nhập vào số thực dương c: "))
if a + b > c and a + c > b and b + c > a:
    print("Ba số này có thể cấu thành độ dài của một tam giác")
else:
    print("Ba số này không thể cấu thành độ dài của một tam giác")
