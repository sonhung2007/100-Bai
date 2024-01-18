a = int(input("Nhập vào số nguyên dương a: "))
if a > 0:
    for i in range(1, 11):
        print(f"{a} x {i} = {a * i}")
else:
    print("Vui lòng nhập số nguyên dương.")
