# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_E
import sys
input = sys.stdin.readline

from Combination.modinv_combination import combination


def main():
    n, k = map(int, input().split())
    MOD = 10 ** 9 + 7
    if n > k:
        print(0)
    else:
        print(combination(k, n, MOD))


if __name__ == '__main__':
    main()
