# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_B
import sys
input = sys.stdin.buffer.readline

from DataStructure.AccumulateSum.Imos2D import Imos2D


def main():
    n = int(input())
    queries = [list(map(int, input().split())) for i in range(n)]

    imos = Imos2D(1000, 1000)
    for hl, wl, hr, wr in queries:
        imos.add(hl, hr, wl, wr, 1)
    imos.build()

    ans = 0
    for i in range(1000):
        for j in range(1000):
            ans = max(ans, imos[i, j])
    print(ans)


if __name__ == '__main__':
    main()
