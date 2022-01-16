def lagrange_interpolation_naive(points, T, MOD):
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


def lagrange_interpolation(y, T, MOD):
    n = len(y) - 1
    T %= MOD
    if 0 <= T <= n:
        return y[T]

    fact = 1
    inv_fact = [1] * (n + 1)
    for val in range(1, n + 1):
        fact = fact * val % MOD
    inv_fact[n] = pow(fact, MOD - 2, MOD)
    for i in reversed(range(1, n + 1)):
        inv_fact[i - 1] = inv_fact[i] * i % MOD

    left = [1] * (n + 1)
    for i in range(n):
        left[i + 1] = (left[i] * (T - i)) % MOD

    r = 1
    res = 0
    for i in reversed(range(n + 1)):
        numer = r * left[i] % MOD
        denom = inv_fact[i] * inv_fact[n - i] % MOD
        ci = numer * denom % MOD
        if (n - i) % 2 == 1:
            ci *= -1
        res = (res + y[i] * ci) % MOD
        r = r * (T - i) % MOD
    return res
