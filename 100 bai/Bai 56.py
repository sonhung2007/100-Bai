def tim_gia_tri_duong_dau_tien(L):
    for gia_tri in L:
        if gia_tri > 0:
            print("Giá trị dương đầu tiên là:", gia_tri)
            return
    print("Không có giá trị dương trong list.")
    print("-1")
L = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
tim_gia_tri_duong_dau_tien(L)
