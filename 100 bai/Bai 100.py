def a(N):
    b = []
    for c in range(1, N):
        d = c
        e = [c]
        while d < N:
            c += 1
            d += c
            e.append(c)
            if d == N:
                b.append(e.copy())
                break
    return b