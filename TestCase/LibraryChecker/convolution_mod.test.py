# verification-helper: PROBLEM https://judge.yosupo.jp/problem/convolution_mod
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Convolution.ntt_convolve import ntt_convolve


def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(*ntt_convolve(a, b))


if __name__ == '__main__':
    main()
