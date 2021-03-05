# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Prime.eratosthenes_sieve import eratosthenes_sieve


def main():
    n = int(input())
    x = [int(input()) for i in range(n)]

    _, prime_tbl = eratosthenes_sieve(max(x))
    ans = 0
    for val in x:
        if prime_tbl[val]:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
