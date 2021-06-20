def multiple_zeta_transform(a, op):
    n = len(a)
    res = a[:]
    prime_table = [1] * n
    for p in range(2, n):
        if not prime_table[p]:
            continue
        i = (n - 1) // p
        while i > 0:
            res[i] = op(res[i], res[i * p])
            prime_table[i * p] = 0
            i -= 1
    return res


def multiple_mobius_transform(a, op, inv):
    n = len(a)
    res = a[:]
    prime_table = [1] * n
    for p in range(2, n):
        if not prime_table[p]:
            continue
        i = 1
        while i * p < n:
            res[i] = op(res[i], inv(res[i * p]))
            prime_table[i * p] = 0
            i += 1
    return res


def divisor_zeta_transform(a, op):
    n = len(a)
    res = a[:]
    prime_table = [1] * n
    for p in range(2, n):
        if not prime_table[p]:
            continue
        i = 1
        while i * p < n:
            res[i * p] = op(res[i], res[i * p])
            prime_table[i * p] = 0
            i += 1
    return res


def divisor_mobius_transform(a, op, inv):
    n = len(a)
    res = a[:]
    prime_table = [1] * n
    for p in range(2, n):
        if not prime_table[p]:
            continue
        i = (n - 1) // p
        while i > 0:
            res[i * p] = op(inv(res[i]), res[i * p])
            prime_table[i * p] = 0
            i -= 1
    return res
