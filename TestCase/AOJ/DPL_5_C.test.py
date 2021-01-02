# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_C
import sys
input = sys.stdin.readline

from Combination.twelvefold_way import way3


def main():
    n, k = map(int, input().split())
    print(way3(n, k))


if __name__ == '__main__':
    main()
