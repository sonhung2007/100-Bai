def tim_vi_tri_gia_tri_k(lst, k):
    for i, gia_tri in enumerate(lst):
        if gia_tri == k:
            return i
    return -1
danh_sach = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
k = int(input("Nhập vào số nguyên dương k: "))
vi_tri = tim_vi_tri_gia_tri_k(danh_sach, k)

if vi_tri != -1:
    print(f"Phần tử đầu tiên có giá trị {k} nằm ở vị trí {vi_tri}.")
else:
    print(f"Không có phần tử có giá trị {k} trong list.")
