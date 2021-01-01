# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0098
import sys
input = sys.stdin.buffer.readline

from DataStructure.AccumulateSum.AccumulateSum2D import AccumulateSum2D


def main():
    n = int(input())
    a = [list(map(int, input().split())) for i in range(n)]

    acc = AccumulateSum2D(a)
    ans = -10 ** 9
    for hl in range(n):
        for hr in range(hl + 1, n + 1):
            for wl in range(n):
                for wr in range(wl + 1, n + 1):
                    ans = max(acc.sum(hl, hr, wl, wr), ans)
    print(ans)


if __name__ == '__main__':
    main()
