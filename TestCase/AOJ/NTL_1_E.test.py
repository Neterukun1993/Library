# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_E
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Basic.extended_gcd import extended_gcd


def main():
    a, b = map(int, input().split())

    _, x, y = extended_gcd(a, b)
    print(x, y)


if __name__ == '__main__':
    main()
