# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_A
import sys
input = sys.stdin.buffer.readline

from DataStructure.AccumulateSum.Imos import Imos


def main():
    n, t = map(int, input().split())
    queries = [list(map(int, input().split())) for i in range(n)]

    imos = Imos(10 ** 5)
    for l, r in queries:
        imos.add(l, r, 1)
    imos.build()

    ans = 0
    for i in range(10 ** 5):
        ans = max(imos[i], ans)
    print(ans)


if __name__ == '__main__':
    main()
