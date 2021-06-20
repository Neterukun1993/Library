# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Convolution.zeta_transform import subset_zeta_transform, superset_zeta_transform
from NumberTheory.Convolution.mobius_transform import subset_mobius_transform, superset_mobius_transform
from misc.xorshift import xorshift32


def naive_subset_zeta_transform(a, op):
    """O(N^2) naive calculation"""
    n = len(a)
    res = a[:]
    for i in range(n):
        for j in range(n):
            if i != j and i & j == j:
                res[i] = op(res[i], a[j])
    return res


def naive_superset_zeta_transform(a, op):
    """O(N^2) naive calculation"""
    n = len(a)
    res = a[:]
    for i in range(n):
        for j in range(n):
            if i != j and i | j == j:
                res[i] = op(res[i], a[j])
    return res


def group_test(arr, op, inv):
    sub_zeta = subset_zeta_transform(arr, op)
    naive_sub_zeta = naive_subset_zeta_transform(arr, op)
    assert(sub_zeta == naive_sub_zeta)

    sup_zeta = superset_zeta_transform(arr, op)
    naive_sup_zeta = naive_superset_zeta_transform(arr, op)
    assert(sup_zeta == naive_sup_zeta)

    sub_mobius = subset_mobius_transform(sub_zeta, op, inv)
    assert(arr == sub_mobius)

    sup_mobius = superset_mobius_transform(sup_zeta, op, inv)
    assert(arr == sup_mobius)


def monoid_test(arr, op):
    sub_zeta = subset_zeta_transform(arr, op)
    naive_sub_zeta = naive_subset_zeta_transform(arr, op)
    assert(sub_zeta == naive_sub_zeta)

    sup_zeta = superset_zeta_transform(arr, op)
    naive_sup_zeta = naive_superset_zeta_transform(arr, op)
    assert(sup_zeta == naive_sup_zeta)


def main():
    rand32 = xorshift32()
    arr = [rand32() for i in range(1000)]

    op = lambda x, y: x + y
    inv = lambda x: -x
    group_test(arr, op, inv)

    monoid_test(arr, max)


if __name__ == '__main__':
    main()
    print("Hello World")
