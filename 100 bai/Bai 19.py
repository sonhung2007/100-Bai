import cmath
a = float(input("Nhập vào hệ số a: "))
b = float(input("Nhập vào hệ số b: "))
c = float(input("Nhập vào hệ số c: "))
delta = b**2 - 4*a*c
if delta > 0:
    x1 = (-b + cmath.sqrt(delta)) / (2*a)
    x2 = (-b - cmath.sqrt(delta)) / (2*a)
    print(f"Phương trình có hai nghiệm phân biệt: x1 = {x1}, x2 = {x2}")
elif delta == 0:
    x = -b / (2*a)
    print(f"Phương trình có nghiệm kép: x = {x}")
else:
    x1 = (-b + cmath.sqrt(delta)) / (2*a)
    x2 = (-b - cmath.sqrt(delta)) / (2*a)
    print(f"Phương trình không có nghiệm thực. Nghiệm phức: x1 = {x1}, x2 = {x2}")
