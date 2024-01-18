a = float(input("Nhập vào hệ số a: "))
b = float(input("Nhập vào hệ số b: "))
if a == 0:
    if b == 0:
        print("Phương trình có vô số nghiệm")
    else:
        print("Phương trình vô nghiệm")
else:
    x = -b / a
    print(f"Phương trình có nghiệm duy nhất x = {x}")
