# verification-helper: PROBLEM https://judge.yosupo.jp/problem/gcd_convolution
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Convolution.gcd_convolve import gcd_convolve


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(*gcd_convolve([0] + a, [0] + b)[1:])


if __name__ == '__main__':
    main()
