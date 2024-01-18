n = int(input("Nhập vào số nguyên dương n: "))
k = 0
while 2**k < n:
    k += 1
if 2**k == n:
    print(f"{n} là số dạng 2^{k}.")
else:
    print(f"{n} không là số dạng 2^k.")
