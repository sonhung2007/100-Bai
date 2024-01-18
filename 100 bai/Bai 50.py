import re
def kiem_tra_mat_khau_manh(chuoi):
    if len(chuoi) <= 6:
        return False
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", chuoi):
        return False
    if not re.search(r"[A-Z]", chuoi):
        return False
    if not re.search(r"[a-z]", chuoi):
        return False
    if not re.search(r"\d", chuoi):
        return False
    return True
chuoi_mat_khau = input("Nhập vào chuỗi mật khẩu: ")
if kiem_tra_mat_khau_manh(chuoi_mat_khau):
    print("Đây là một chuỗi mật khẩu mạnh.")
else:
    print("Đây không phải là một chuỗi mật khẩu mạnh.")
