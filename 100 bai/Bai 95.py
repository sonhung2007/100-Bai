def day(x):
    if 1 <= x <= 3:
        return 1
    return day(x - 1) + day(x - 3)
n = int(input())
print(day(n))