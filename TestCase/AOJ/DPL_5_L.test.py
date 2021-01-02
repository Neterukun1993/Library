# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_L
import sys
input = sys.stdin.readline

from Combination.twelvefold_way import way12


def main():
    n, k = map(int, input().split())
    print(way12(n, k))


if __name__ == '__main__':
    main()
