thang = int(input("Nhập vào tháng (1-12): "))
nam = int(input("Nhập vào năm: "))
if 1 <= thang <= 12:
    if thang in [1, 3, 5, 7, 8, 10, 12]:
        print(f"Tháng {thang}/{nam} có 31 ngày.")
    elif thang in [4, 6, 9, 11]:
        print(f"Tháng {thang}/{nam} có 30 ngày.")
    else:
        if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
            print(f"Tháng 2/{nam} có 29 ngày (năm nhuận).")
        else:
            print(f"Tháng 2/{nam} có 28 ngày.")
else:
    print("Tháng không hợp lệ. Vui lòng nhập tháng từ 1 đến 12.")
