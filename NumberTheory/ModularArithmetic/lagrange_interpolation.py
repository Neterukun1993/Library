def lagrange_interpolation(points, T, MOD):
    n = len(points) - 1
    x, y = list(zip(*points))
    res = 0
    for i in range(n + 1):
        numer = 1
        denom = 1
        for j in range(n + 1):
            if i == j:
                continue
            numer *= T - x[j]
            numer %= MOD
            denom *= x[i] - x[j]
            denom %= MOD
        ci = numer * pow(denom, MOD - 2, MOD) % MOD
        res += y[i] * ci
        res %= MOD
    return res
