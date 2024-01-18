def la_so_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
a = int(input("Nhập vào số nguyên dương a: "))
if la_so_nguyen_to(a):
    print(f"{a} là số nguyên tố.")
else:
    print(f"{a} không là số nguyên tố.")
