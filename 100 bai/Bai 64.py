def kiem_tra_list_chan_le(L):
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            if (L[i] + L[j]) % 2 == 0:
                return False
    return True
L = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
if kiem_tra_list_chan_le(L):
    print("List chẵn lẻ.")
else:
    print("List không chẵn lẻ.")
