n = int(input("Nhập vào số nguyên dương n: "))
S = 0
k = 0
while S <= n:
    k += 1
    S += k
k -= 1
print(f"Giá trị k tìm được là: {k}")
