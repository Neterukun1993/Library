from NumberTheory.Convolution.multiple_divisor_transform import (
    multiple_zeta_transform,
    multiple_mobius_transform
)
MOD = 998244353


def gcd_convolve(a, b):
    add = lambda x, y: (x + y) % MOD
    inv = lambda x: -x
    mul = lambda x, y: (x * y) % MOD

    a = multiple_zeta_transform(a, add)
    b = multiple_zeta_transform(b, add)
    res = [mul(v1, v2) for v1, v2 in zip(a, b)]
    res = multiple_mobius_transform(res, add, inv)
    return res
