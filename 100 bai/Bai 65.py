def kiem_tra_dang_song(L):
    n = len(L)
    if n < 3:
        return False
    for i in range(1, n-1):
        if not (L[i-1] < L[i] > L[i+1] or L[i-1] > L[i] < L[i+1]):
            return False
    return True
L = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
if kiem_tra_dang_song(L):
    print("True")
else:
    print("False")
