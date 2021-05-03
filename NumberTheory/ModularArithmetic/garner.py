from NumberTheory.Basic.extended_gcd import extended_gcd, mod_inv


def pregarner(a, m, MOD):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    a, m = a[:], m[:]
    n = len(a)
    for i in range(n):
        for j in range(i):
            g = gcd(m[i], m[j])
            if (a[i] - a[j]) % g != 0:
                return -1, a, m
            m[i], m[j] = m[i] // g, m[j] // g
            gi = gcd(m[i], g)
            gj = g // gi
            while True:
                g = gcd(gi, gj)
                gi, gj = gi * g, gj // g
                if g == 1:
                    break
            m[i], m[j] = m[i] * gi, m[j] * gj
            a[i], a[j] = a[i] % m[i], a[j] % m[j]
    lcm = 1
    for i in range(n):
        lcm = lcm * m[i] % MOD
    return lcm, a, m


def garner(a, m, MOD):
    n = len(m)
    m = m + [MOD]
    coeff = [1] * (n + 1)
    res = [0] * (n + 1)
    for i in range(n):
        t = (a[i] - res[i]) * mod_inv(coeff[i], m[i]) % m[i]
        for j in range(i + 1, n + 1):
            res[j] = (res[j] + t * coeff[j]) % m[j]
            coeff[j] = coeff[j] * m[i] % m[j]
    return res[-1]
