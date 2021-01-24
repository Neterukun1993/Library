# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_sat
import sys
input = sys.stdin.buffer.readline

from Graph.misc.TwoSAT import TwoSAT


def main():
    p, cfn, n, m = input().split()
    n, m = int(n), int(m)
    info = [list(map(int, input().split())) for i in range(m)]

    ts = TwoSAT(n)
    for i, j, _ in info:
        f, g = True, True
        if i < 0:
            i = -i
            f = False
        if j < 0:
            j = -j
            g = False
        i -= 1
        j -= 1
        ts.add_clause(i, f, j, g)

    flag = ts.satisfy()
    if flag:
        print("s", "SATISFIABLE")
        res = ts.answer()
        print("v", *[(i + 1) if b else -(i + 1) for i, b in enumerate(res)], 0)
    else:
        print("s", "UNSATISFIABLE")


if __name__ == '__main__':
    main()
