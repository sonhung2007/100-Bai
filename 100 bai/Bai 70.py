def tao_list_K(L):
    if len(L) % 2 != 0:
        print("Số lượng phần tử trong list không chẵn, không thể tiến hành tạo list K.")
        return None

    K = []
    
    for i in range(0, len(L), 2):
        if isinstance(L[i], str) and isinstance(L[i+1], int):
            K.append(L[i] * L[i+1])
        else:
            print(f"Cặp phần tử thứ {i} và {i+1} không phải là chuỗi và số nguyên xen kẽ nhau. Không thể tiến hành tạo list K.")
            return None

    return K

L = input("Nhập vào list số nguyên và chuỗi, xen kẽ nhau, cách nhau bởi dấu cách: ").split()
L = [int(x) if x.isdigit() else x for x in L]
list_K = tao_list_K(L)
if list_K is not None:
    print("List K mới được tạo:", list_K)
