def tinh_gia_tri_trung_binh(L):
    if len(L) == 0:
        print("List rỗng, không thể tính giá trị trung bình.")
        return 0
    gia_tri_trung_binh = sum(L) / len(L)
    print("Giá trị trung bình của list là:", gia_tri_trung_binh)
    return gia_tri_trung_binh
L = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
tinh_gia_tri_trung_binh(L)
