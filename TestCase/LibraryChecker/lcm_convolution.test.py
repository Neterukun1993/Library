# verification-helper: PROBLEM https://judge.yosupo.jp/problem/lcm_convolution
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Convolution.lcm_convolve import lcm_convolve


def main():
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(*lcm_convolve([0] + a, [0] + b)[1:])


if __name__ == '__main__':
    main()
