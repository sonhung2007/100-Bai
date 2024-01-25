def la_so_nguyen_to(a):
    if a < 2:
        return False
    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True
so_nguyen = int(input("Nhập một số nguyên: "))
if la_so_nguyen_to(so_nguyen):
    print(f"{so_nguyen} là số nguyên tố.")
else:
    print(f"{so_nguyen} không phải là số nguyên tố.")
