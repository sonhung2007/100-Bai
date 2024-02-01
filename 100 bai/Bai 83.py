def tim_key_do_dai_lon_nhat(dictionary):
    if not dictionary:
        return None
    max_key = max(dictionary, key=len)
    return dictionary[max_key]
my_dict = {"key1": "value1", "longest_key": "value2", "key3": "value3"}
result = tim_key_do_dai_lon_nhat(my_dict)
print(f"Giá trị của key có độ dài lớn nhất là: {result}")
