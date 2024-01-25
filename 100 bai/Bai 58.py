def tim_gia_tri_xa_nhat(L, x):
    if not L:
        print("List rỗng.")
        return
    gia_tri_xa_nhat = None
    khoang_cach_xa_nhat = None
    for gia_tri in L:
        khoang_cach = abs(gia_tri - x)
        if gia_tri_xa_nhat is None or khoang_cach > khoang_cach_xa_nhat:
            gia_tri_xa_nhat = gia_tri
            khoang_cach_xa_nhat = khoang_cach
    print(f"Giá trị trong list xa nhất từ {x} là {gia_tri_xa_nhat}, với khoảng cách là {khoang_cach_xa_nhat}.")
L = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
x = int(input("Nhập vào số nguyên x: "))
tim_gia_tri_xa_nhat(L, x)
