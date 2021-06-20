def subset_zeta_transform(a, op):
    n = len(a)
    res = a[:]
    for k in range((n - 1).bit_length()):
        bit = 1 << k
        for i in range(n):
            if i & bit:
                res[i] = op(res[i & ~bit], res[i])
    return res


def superset_zeta_transform(a, op):
    n = len(a)
    res = a[:]
    for k in range((n - 1).bit_length()):
        bit = 1 << k
        for i in range(n):
            if i & bit:
                res[i & ~bit] = op(res[i & ~bit], res[i])
    return res
