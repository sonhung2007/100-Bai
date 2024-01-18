ngay = int(input("Nhập vào ngày: "))
thang = int(input("Nhập vào tháng: "))
if 1 <= thang <= 12 and 1 <= ngay <= 31:
    so_ngay_trong_thang = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    so_ngay = sum(so_ngay_trong_thang[1:thang]) + ngay
    print(f"Ngày {ngay}/{thang} cách ngày đầu năm {so_ngay} ngày.")
else:
    print("Ngày hoặc tháng không hợp lệ.")
