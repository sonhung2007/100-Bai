a = int(input("Nhập vào số nguyên dương a: "))
b = int(input("Nhập vào số nguyên dương b: "))
def tim_uoc_chung(a, b):
    while b:
        a, b = b, a % b
    return a
uoc_chung = tim_uoc_chung(a, b)
print(f"Ước chung lớn nhất của {a} và {b} là: {uoc_chung}")
