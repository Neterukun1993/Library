# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_C
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Prime.is_prime import is_prime


def main():
    n = int(input())
    x = [int(input()) for i in range(n)]

    ans = 0
    for val in x:
        if is_prime(val):
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
