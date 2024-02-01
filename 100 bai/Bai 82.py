a = list(map(int, input().split()))
d = {}

# Tạo dictionary từ list a
for i in range(0, len(a), 2):
    d[a[i]] = a[i + 1]

# Tìm key có giá trị lớn nhất trong dictionary
max_key = max(d, key=d.get)

print("Key có giá trị lớn nhất trong dictionary là:", max_key)
