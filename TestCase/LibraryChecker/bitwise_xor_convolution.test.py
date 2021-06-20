# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_xor_convolution
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Convolution.xor_convolve import xor_convolve


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(*xor_convolve(a, b))


if __name__ == '__main__':
    main()
