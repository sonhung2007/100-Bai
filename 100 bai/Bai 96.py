def uoc(x):
    tong = 1
    for i in range(2, int(x/2) + 1):
        if x % i == 0:
            tong += i
    return tong
k = int(input())
for m in range(1, k):
    for n in range(m + 1, k + 1):
        if uoc(m) == n and m == uoc(n):
            print(m, n)