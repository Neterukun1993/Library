def primitive_root(p):
    if p == 2:
        return 1
    x = p - 1
    factors = [2]
    while x % 2 == 0:
        x //= 2
    for k in range(3, int(p ** 0.5) + 1, 2):
        if x % k == 0:
            factors.append(k)
            while x % k == 0:
                x //= k
    if x != 1:
        factors.append(x)

    g = 2
    while True:
        ok = True
        for val in factors:
            if pow(g, (p - 1) // val, p) == 1:
                ok = False
                break
        if ok:
            return g
        g += 1
