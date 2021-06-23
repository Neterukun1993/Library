# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Convolution.gcd_convolve import gcd_convolve


def naive_gcd_convolve(a, b):
    """O(N^2) naive calculation"""
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x

    n = min(len(a), len(b))
    res = [0] * n
    for i, va in enumerate(a[1:], 1):
        for j, vb in enumerate(b[1:], 1):
            res[gcd(i, j)] += va * vb
    return res


def main():
    n = 1000
    a = [1] * n
    b = [1] * n
    a[0] = 0
    b[0] = 0
    assert(gcd_convolve(a, b) == naive_gcd_convolve(a, b))


if __name__ == '__main__':
    main()
    print("Hello World")
