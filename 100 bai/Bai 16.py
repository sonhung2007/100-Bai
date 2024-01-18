a = float(input("Nhập vào số thực dương a: "))
b = float(input("Nhập vào số thực dương b: "))
c = float(input("Nhập vào số thực dương c: "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Đây là tam giác đều")
    elif a == b or b == c or a == c:
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
            print("Đây là tam giác vuông cân")
        else:
            print("Đây là tam giác cân")
    elif a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        print("Đây là tam giác vuông")
    else:
        print("Đây là tam giác thường")
else:
    print("Ba số này không thể cấu thành độ dài của một tam giác")
