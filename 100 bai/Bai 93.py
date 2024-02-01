n = int(input())
i = 2
l = []
while n > 1:
    if n % i == 0:
        l.append(i)
        n //= i
    else:
        i += 1
print(l)