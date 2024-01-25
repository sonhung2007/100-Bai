def tim_chuoi_max_va_so_min(L):
    chuoi_max = None
    so_min = float('inf')
    for phan_tu in L:
        if isinstance(phan_tu, str) and (chuoi_max is None or len(phan_tu) > len(chuoi_max)):
            chuoi_max = phan_tu
        elif isinstance(phan_tu, int) and phan_tu < so_min:
            so_min = phan_tu
    if chuoi_max is not None:
        print("Chuỗi có độ dài lớn nhất:", chuoi_max)
    else:
        print("Không có chuỗi trong list.")
    if so_min != float('inf'):
        print("Số nguyên có giá trị nhỏ nhất:", so_min)
    else:
        print("Không có số nguyên trong list.")
L = input("Nhập vào list số nguyên và chuỗi, cách nhau bởi dấu cách: ").split()
L = [int(x) if x.isdigit() else x for x in L]
tim_chuoi_max_va_so_min(L)
