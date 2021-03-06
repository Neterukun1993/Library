# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_1_B
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Basic.gcd_lcm import gcd


def main():
    x, y = map(int, input().split())
    print(gcd(x, y))


if __name__ == '__main__':
    main()
