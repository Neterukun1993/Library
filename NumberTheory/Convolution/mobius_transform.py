def subset_mobius_transform(a, op, inv):
    n = len(a)
    res = a[:]
    for k in range((n - 1).bit_length()):
        bit = 1 << k
        for i in range(n):
            if i & bit:
                res[i] = op(inv(res[i & ~bit]), res[i])
    return res


def superset_mobius_transform(a, op, inv):
    n = len(a)
    res = a[:]
    for k in range((n - 1).bit_length()):
        bit = 1 << k
        for i in range(n):
            if i & bit:
                res[i & ~bit] = op(res[i & ~bit], inv(res[i]))
    return res
