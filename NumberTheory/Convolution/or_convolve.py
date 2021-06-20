from NumberTheory.Convolution.zeta_transform import subset_zeta_transform
from NumberTheory.Convolution.mobius_transform import subset_mobius_transform
MOD = 998244353


def or_convolve(a, b):
    add = lambda x, y: (x + y) % MOD
    inv = lambda x: -x
    mul = lambda x, y: (x * y) % MOD

    a = subset_zeta_transform(a, add)
    b = subset_zeta_transform(b, add)
    res = [mul(v1, v2) for v1, v2 in zip(a, b)]
    res = subset_mobius_transform(res, add, inv)
    return res
