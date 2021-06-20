# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Convolution.and_convolve import and_convolve


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(*and_convolve(a, b))


if __name__ == '__main__':
    main()
