def kiem_tra_bang_nhau(L):
    ket_qua = all(element == L[0] for element in L)
    print(ket_qua)
L = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
kiem_tra_bang_nhau(L)
