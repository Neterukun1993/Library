# verification-helper: PROBLEM https://atcoder.jp/contests/abc175/tasks/abc175_d
import sys
input = sys.stdin.buffer.readline

from Graph.misc.Doubling import Doubling


def main():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))

    p = [p[i] - 1 for i in range(n)]
    db = Doubling(p)

    values = [(c[i], c[i]) for i in range(n)]
    op = lambda x1, x2: (x1[0] + x2[0], max(x1[1], x1[0] + x2[1]))
    e = (0, -10 ** 18)
    db.build_path(values, op, e)

    ans = -10 ** 18
    for i in range(n):
        ans = max(ans, db.fold(i, k)[1])

    print(ans)


if __name__ == '__main__':
    main()
