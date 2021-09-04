# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

import itertools
from Combination.catalan import catalan, catalan_trapezoid


def naive_catalan(n):
    """DFS naive calculation"""
    def dfs(cnt_pl, cnt_mi):
        if cnt_pl > n or cnt_mi > n or cnt_pl < cnt_mi:
            return 0
        if cnt_pl == n and cnt_mi == n:
            return 1
        return dfs(cnt_pl + 1, cnt_mi) + dfs(cnt_pl, cnt_mi + 1)

    return dfs(0, 0)


def naive_catalan_trapezoid(n, k, m):
    """DFS naive calculation"""
    def dfs(cnt_pl, cnt_mi):
        if cnt_pl > n or cnt_mi > k or cnt_pl + (m - 1) < cnt_mi:
            return 0
        if cnt_pl == n and cnt_mi == k:
            return 1
        return dfs(cnt_pl + 1, cnt_mi) + dfs(cnt_pl, cnt_mi + 1)

    return dfs(0, 0)


def main():
    for n in range(10):
        assert(catalan(n) == naive_catalan(n))

    for n in range(5):
        for k in range(5):
            for m in range(5):
                assert(catalan_trapezoid(n, k, m)
                       == naive_catalan_trapezoid(n, k, m))


if __name__ == '__main__':
    main()
    print("Hello World")
