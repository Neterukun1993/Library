from random import randint


def euler_criterion(a, p):
    res = pow(a, (p - 1) // 2, p)
    return 1 if res == 1 else res - p


def tonelli_shanks(a, p):
    a %= p
    if p == 2:
        return a
    if a == 0:
        return 0
    if euler_criterion(a, p) == -1:
        return -1

    z = randint(1, p - 1)
    while euler_criterion(z, p) == 1:
        z = randint(1, p - 1)

    # p - 1 = (2 ** m) * q
    q, m = p - 1, 0
    while q & 1 == 0:
        q //= 2
        m += 1

    c, t = pow(z, q, p), pow(a, q, p)
    res = pow(a, (q + 1) // 2, p)
    if t == 0:
        return 0

    m -= 2
    while t != 1:
        while pow(t, 2 ** m, p) == 1:
            c = c * c % p
            m -= 1
        res = res * c % p
        c = c * c % p
        t = t * c % p
        m -= 1
    return res
