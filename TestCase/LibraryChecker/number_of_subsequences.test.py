# verification-helper: PROBLEM https://judge.yosupo.jp/problem/number_of_subsequences
import sys
input = sys.stdin.buffer.readline

from DP.count_subsequence import count_subsequence


def main():
    n = int(input())
    a = list(map(int, input().split()))

    MOD = 998244353

    res = (count_subsequence(a, MOD) - 1) % MOD
    print(res)


if __name__ == '__main__':
    main()
