# verification-helper: PROBLEM https://judge.yosupo.jp/problem/bitwise_and_convolution
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Convolution.or_convolve import or_convolve


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(*or_convolve(a[::-1], b[::-1])[::-1])


if __name__ == '__main__':
    main()
