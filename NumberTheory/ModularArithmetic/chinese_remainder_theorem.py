from NumberTheory.Basic.extended_gcd


def chinese_remainder_theorem(a, m):
    r, M = 0, 1
    for i in range(len(a)):
        g, p, q = extended_gcd(M, m[i])
        if (a[i] - r) % g != 0:
            return -1, -1
        tmp = (a[i] - r) // g * p % (m[i] // g)
        r += M * tmp
        M *= m[i] // g
    return r % M, M
