a = input()
tong = 0
for i in range(len(a)):
    if a[i] == "1":
        tong += 2**i
print(tong)