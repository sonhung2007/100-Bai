def kiem_tra_sap_xep_tang_dan(L):
    if L == sorted(L):
        print("True")
    else:
        print("False")
L = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
kiem_tra_sap_xep_tang_dan(L)
