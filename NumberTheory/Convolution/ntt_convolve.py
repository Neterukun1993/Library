MOD = 998244353
ROOT = 5


def _ntt(a, h):
    roots = [pow(ROOT, (MOD - 1) >> i, MOD) for i in range(h + 1)]
    for i in range(h):
        m = 1 << (h - i - 1)
        for j in range(1 << i):
            w = 1
            j *= 2 * m
            for k in range(m):
                a[j + k], a[j + k + m] = \
                    (a[j + k] + a[j + k + m]) % MOD, \
                    (a[j + k] - a[j + k + m]) * w % MOD
                w *= roots[h - i]
                w %= MOD


def _intt(a, h):
    roots = [pow(ROOT, (MOD - 1) >> i, MOD) for i in range(h + 1)]
    iroots = [pow(r, MOD - 2, MOD) for r in roots]
    for i in range(h):
        m = 1 << i
        for j in range(1 << (h - i - 1)):
            w = 1
            j *= 2 * m
            for k in range(m):
                a[j + k], a[j + k + m] = \
                    (a[j + k] + a[j + k + m] * w) % MOD, \
                    (a[j + k] - a[j + k + m] * w) % MOD
                w *= iroots[i + 1]
                w %= MOD
    inv = pow(1 << h, MOD - 2, MOD)
    for i in range(1 << h):
        a[i] *= inv
        a[i] %= MOD


def ntt_convolve(a, b):
    len_ab = len(a) + len(b)
    n = 1 << (len(a) + len(b) - 1).bit_length()
    h = n.bit_length() - 1
    a = list(a) + [0] * (n - len(a))
    b = list(b) + [0] * (n - len(b))

    _ntt(a, h), _ntt(b, h)
    a = [va * vb % MOD for va, vb in zip(a, b)]
    _intt(a, h)
    return a[:len_ab - 1]
