M1, R1 = 167772161, 3
M2, R2 = 469762049, 3
M3, R3 = 1224736769, 3


def MOD1(): return M1
def ROOT1(): return R1
def MOD2(): return M2
def ROOT2(): return R2
def MOD3(): return M3
def ROOT3(): return R3


def _ntt(a, h, MOD, ROOT):
    roots = [pow(ROOT(), (MOD() - 1) >> i, MOD()) for i in range(h + 1)]
    for i in range(h):
        m = 1 << (h - i - 1)
        for j in range(1 << i):
            w = 1
            j *= 2 * m
            for k in range(m):
                a[j + k], a[j + k + m] = \
                    (a[j + k] + a[j + k + m]) % MOD(), \
                    (a[j + k] - a[j + k + m]) * w % MOD()
                w *= roots[h - i]
                w %= MOD()


def _intt(a, h, MOD, ROOT):
    roots = [pow(ROOT(), (MOD() - 1) >> i, MOD()) for i in range(h + 1)]
    iroots = [pow(r, MOD() - 2, MOD()) for r in roots]
    for i in range(h):
        m = 1 << i
        for j in range(1 << (h - i - 1)):
            w = 1
            j *= 2 * m
            for k in range(m):
                a[j + k], a[j + k + m] = \
                    (a[j + k] + a[j + k + m] * w) % MOD(), \
                    (a[j + k] - a[j + k + m] * w) % MOD()
                w *= iroots[i + 1]
                w %= MOD()
    inv = pow(1 << h, MOD() - 2, MOD())
    for i in range(1 << h):
        a[i] *= inv
        a[i] %= MOD()


def ntt_convolve(a, b, MOD, ROOT):
    n = 1 << (len(a) + len(b) - 1).bit_length()
    h = n.bit_length() - 1
    a = list(a) + [0] * (n - len(a))
    b = list(b) + [0] * (n - len(b))

    _ntt(a, h, MOD, ROOT), _ntt(b, h, MOD, ROOT)
    a = [va * vb % MOD() for va, vb in zip(a, b)]
    _intt(a, h, MOD, ROOT)
    return a


def arbitrary_mod_convolve(a, b, mod):
    x = ntt_convolve(a, b, MOD1, ROOT1)
    y = ntt_convolve(a, b, MOD2, ROOT2)
    z = ntt_convolve(a, b, MOD3, ROOT3)

    inv1_2 = pow(MOD1(), MOD2() - 2, MOD2())
    inv12_3 = pow(MOD1() * MOD2(), MOD3() - 2, MOD3())
    mod12 = MOD1() * MOD2() % mod

    res = [0] * len(x)
    for i in range(len(x)):
        v1 = (y[i] - x[i]) * inv1_2 % MOD2()
        v2 = (z[i] - (x[i] + MOD1() * v1) % MOD3()) * inv12_3 % MOD3()
        res[i] = (x[i] + MOD1() * v1 + mod12 * v2) % mod
    return res
