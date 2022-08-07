# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sum_of_totient_function
import sys
input = sys.stdin.buffer.readline

from NumberTheory.misc.totient_sum import totient_sum


MOD = 998244353


def main():
    n = int(input())
    print(totient_sum(n, MOD))


if __name__ == '__main__':
    main()
