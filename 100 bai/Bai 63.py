def tim_vi_tri_tich_lan_can(L):
    n = len(L)
    if n < 3:
        print("List không đủ phần tử để kiểm tra.")
        return -1
    for i in range(1, n - 1):
        if L[i] == L[i-1] * L[i+1]:
            print(f"Vị trí thỏa điều kiện là {i}.")
            return i
    print("Không có vị trí nào thỏa điều kiện.")
    return -1
L = list(map(int, input("Nhập vào list số nguyên, cách nhau bởi dấu cách: ").split()))
tim_vi_tri_tich_lan_can(L)
