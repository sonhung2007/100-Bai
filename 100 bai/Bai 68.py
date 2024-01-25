def bien_doi_gia_tri_nho_lon(L):
    if len(L) < 2:
        print("List cần có ít nhất 2 phần tử để biến đổi.")
        return
    vi_tri_gia_tri_nho_nhat = L.index(min(L))
    vi_tri_gia_tri_lon_nhat = L.index(max(L))
    L[vi_tri_gia_tri_nho_nhat], L[vi_tri_gia_tri_lon_nhat] = L[vi_tri_gia_tri_lon_nhat], L[vi_tri_gia_tri_nho_nhat]
L = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
bien_doi_gia_tri_nho_lon(L)
print("List sau khi biến đổi:", L)
