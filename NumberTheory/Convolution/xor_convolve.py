MOD = 998244353


def _wht(a, h):
    for k in range(h):
        bit = 1 << k
        for i in range(1 << h):
            if i & bit == 0:
                x, y = a[i], a[i | bit]
                a[i] = (x + y) % MOD
                a[i | bit] = (x - y) % MOD


def _iwht(a, h):
    _wht(a, h)
    invn = pow(1 << h, MOD - 2, MOD)
    for i in range(1 << h):
        a[i] *= invn
        a[i] %= MOD


def xor_convolve(a, b):
    n = 1 << (max(len(a), len(b)) - 1).bit_length()
    h = n.bit_length() - 1
    a = list(a) + [0] * (n - len(a))
    b = list(b) + [0] * (n - len(b))

    _wht(a, h), _wht(b, h)
    a = [(va * vb) % MOD for va, vb in zip(a, b)]
    _iwht(a, h)
    return a
