# verification-helper: PROBLEM https://judge.yosupo.jp/problem/queue_operate_all_composite
import sys
input = sys.stdin.buffer.readline

from DataStructure.misc.SlidingWindowAggregation import SlidingWindowAggregation


MOD = 998244353
MASK = (1 << 32) - 1


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
    q = int(input())
    queries = [list(map(int, input().split())) for i in range(q)]

    swag = SlidingWindowAggregation(A_f)
    ans = []
    for query in queries:
        if query[0] == 0:
            _, a, b = query
            swag.append((a << 32) + b)
        elif query[0] == 1:
            swag.popleft()
        else:
            _, x = query
            if len(swag) == 0:
                ans.append(x)
            else:
                a = swag.fold_all()
                res = XA_map((x << 32) + 1, a)
                ans.append(res >> 32)

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
