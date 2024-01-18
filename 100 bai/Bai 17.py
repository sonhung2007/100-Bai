a = float(input("Nhập vào số thực a: "))
b = float(input("Nhập vào số thực b: "))
c = float(input("Nhập vào số thực c: "))
if a > b:
    a, b = b, a
if a > c:
    a, c = c, a
if b > c:
    b, c = c, b
print("Các số đã sắp xếp theo thứ tự tăng dần là:", a, b, c)
