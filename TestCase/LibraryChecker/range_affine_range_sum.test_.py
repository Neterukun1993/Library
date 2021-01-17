# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_affine_range_sum
import sys
input = sys.stdin.buffer.readline

from DataStructure.SegmentTree.LazySegmentTree import LazySegmentTree


MOD = 998244353
MASK = (1 << 32) - 1
unitA = 1 << 32
unitX = 0


def X_f(x1, x2):
    x = x1 + x2
    return ((x >> 32) % MOD << 32) + (x & MASK) % MOD


def XA_map(x, a):
    x0, x1 = x >> 32, x & MASK
    a0, a1 = a >> 32, a & MASK
    return (((x0 * a0 + x1 * a1) % MOD) << 32) + x1


def A_f(a1, a2):
    a10, a11 = a1 >> 32, a1 & MASK
    a20, a21 = a2 >> 32, a2 & MASK
    return ((a20 * a10 % MOD) << 32) + (a20 * a11 + a21) % MOD


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for i in range(q)]

    lst = LazySegmentTree(n, unitX, unitA, X_f, A_f, XA_map)
    lst.build([(val << 32) + 1 for val in a])

    ans = []
    for flag, *query in queries:
        if flag == 0:
            l, r, b, c = query
            if l + 1 == r:
                lst.apply(l, (b << 32) + c)
            else:
                lst.range_apply(l, r, (b << 32) + c)
        else:
            l, r = query
            if l + 1 == r:
                ans.append(lst[l] >> 32)
            else:
                ans.append(lst.fold(l, r) >> 32)

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
