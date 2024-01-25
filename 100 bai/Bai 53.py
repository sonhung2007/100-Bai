L = [int(x) for x in input("Nhập vào danh sách số nguyên, cách nhau bởi dấu cách: ").split()]
if len(L) > 0:
    max_value = max(L)
    print("Giá trị lớn nhất trong danh sách là:", max_value)
else:
    print("Danh sách rỗng.")
