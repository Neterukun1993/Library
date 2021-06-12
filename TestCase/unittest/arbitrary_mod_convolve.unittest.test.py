# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from misc.xorshift import xorshift32
from NumberTheory.Convolution.arbitrary_mod_convolve import arbitrary_mod_convolve


rand = xorshift32()


def check(a, b, MOD):
    res1 = arbitrary_mod_convolve(a, b, MOD)
    res2 = [0] * (len(a) + len(b) - 1)
    for i, va in enumerate(a):
        for j, vb in enumerate(b):
            res2[i + j] += va * vb
            res2[i + j] %= MOD
    assert(res1 == res2)


def mod_2():
    a = [rand() for i in range(100)]
    b = [rand() for i in range(100)]
    MOD = 2
    check(a, b, MOD)


def mod_998244353():
    a = [rand() for i in range(100)]
    b = [rand() for i in range(100)]
    MOD = 10 ** 9 + 7
    check(a, b, MOD)


def mod_1000000007():
    a = [rand() for i in range(100)]
    b = [rand() for i in range(100)]
    MOD = 10 ** 9 + 7
    check(a, b, MOD)


def main():
    for _ in range(100):
        mod_2()
        mod_998244353()
        mod_1000000007()


if __name__ == '__main__':
    main()
    print("Hello World")
