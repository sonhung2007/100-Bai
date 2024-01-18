# Nhập vào số nguyên dương a từ người dùng
a = int(input("Nhập vào số nguyên dương a: "))
print(f"Các ước của {a} là:")
for i in range(1, a + 1):
    if a % i == 0:
        print(i)
