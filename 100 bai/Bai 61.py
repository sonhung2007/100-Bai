def sap_xep_tang_dan(L):
    L.sort()
    print("List sau khi sắp xếp từ bé đến lớn:", L)
L = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
sap_xep_tang_dan(L)
