from Combination.modinv_combination import Combination


MOD = 10 ** 9 + 7
comb = Combination(10 ** 6 + 10, MOD)


def catalan(n):
    return comb.comb(2 * n, n) * comb.inv(n + 1) % comb.MOD


def catalan_trapezoid(n, k, m=1):
    if 0 <= k < m:
        return comb.comb(n + k, k)
    elif m <= k < n + m:
        return (comb.comb(n + k, k) - comb.comb(n + k, k - m)) % comb.MOD
    else:
        return 0
