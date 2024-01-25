def tim_gia_tri_am_lon_nhat(L):
    gia_tri_am_lon_nhat = float('-inf')
    for gia_tri in L:
        if gia_tri < 0 and gia_tri > gia_tri_am_lon_nhat:
            gia_tri_am_lon_nhat = gia_tri
    if gia_tri_am_lon_nhat == float('-inf'):
        print("Không có giá trị âm trong list.")
        print("0")
    else:
        print("Giá trị âm lớn nhất là:", gia_tri_am_lon_nhat)
L = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
tim_gia_tri_am_lon_nhat(L)
