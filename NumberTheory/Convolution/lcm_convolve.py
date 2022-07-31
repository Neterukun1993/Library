from NumberTheory.Convolution.multiple_divisor_transform import (
    divisor_zeta_transform,
    divisor_mobius_transform
)
MOD = 998244353


def lcm_convolve(a, b):
    add = lambda x, y: (x + y) % MOD
    inv = lambda x: -x
    mul = lambda x, y: (x * y) % MOD

    a = divisor_zeta_transform(a, add)
    b = divisor_zeta_transform(b, add)
    res = [mul(v1, v2) for v1, v2 in zip(a, b)]
    res = divisor_mobius_transform(res, add, inv)
    return res
