def mahoa_chuoi(list_chuoi):
    dictionary_mahoa = {chuoi: i for i, chuoi in enumerate(set(list_chuoi))}
    list_mahoa = [dictionary_mahoa[chuoi] for chuoi in list_chuoi]
    return list_mahoa
L = ["đen", "vàng", "xanh", "vàng", "xanh", "đỏ", "hồng"]
L_mahoa = mahoa_chuoi(L)
print("List đã được mã hóa:", L_mahoa)
