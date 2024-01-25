def sap_xep_chan_le_0(L):
    chan = [x for x in L if x % 2 == 0]
    le = [x for x in L if x % 2 != 0]
    zeros = [0] * (len(L) - len(chan) - len(le))
    ket_qua = chan + zeros + le
    print("List sau khi sắp xếp:", ket_qua)
L = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
sap_xep_chan_le_0(L)
