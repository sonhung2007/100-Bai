def kiem_tra_cap_so_cong(L):
    if len(L) < 3:
        print("Không thể kiểm tra vì list có ít hơn 3 phần tử.")
        return None
    cong_sai = L[1] - L[0]
    for i in range(2, len(L)):
        if L[i] - L[i-1] != cong_sai:
            print("None")
            return None
    print(f"Công sai của cấp số cộng là: {cong_sai}")
    return cong_sai
L = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
kiem_tra_cap_so_cong(L)
