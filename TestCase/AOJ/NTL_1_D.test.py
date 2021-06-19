# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_D
import sys
input = sys.stdin.readline

from NumberTheory.misc.euler_phi import euler_phi


def main():
    n = int(input())
    print(euler_phi(n))


if __name__ == '__main__':
    main()
