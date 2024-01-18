a = int(input("Nhập vào số nguyên dương a: "))
b = int(input("Nhập vào số nguyên dương b: "))
uoc_chung = []
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        uoc_chung.append(i)
print(f"Các ước chung của {a} và {b} là:")
for uoc in uoc_chung:
    print(uoc)
