from NumberTheory.Convolution.zeta_transform import superset_zeta_transform
from NumberTheory.Convolution.mobius_transform import superset_mobius_transform
MOD = 998244353


def and_convolve(a, b):
    add = lambda x, y: (x + y) % MOD
    inv = lambda x: -x
    mul = lambda x, y: (x * y) % MOD

    a = superset_zeta_transform(a, add)
    b = superset_zeta_transform(b, add)
    res = [mul(v1, v2) for v1, v2 in zip(a, b)]
    res = superset_mobius_transform(res, add, inv)
    return res
