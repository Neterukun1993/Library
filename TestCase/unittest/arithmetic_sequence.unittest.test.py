# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Basic.arithmetic_sequence import Arithmetic


def naive_sum(a0, d, r):
    result = 0
    for i in range(r):
        result += a0 + i * d
    return result


def naive_range_sum(a0, d, l, r):
    result = 0
    for i in range(l, r):
        result += a0 + i * d
    return result


def main():
    for a0 in range(-10, 10):
        for d in range(-10, 10):
            for r in range(10):
                assert(Arithmetic.sum(a0, d, r) == naive_sum(a0, d, r))

    for a0 in range(-10, 10):
        for d in range(-10, 10):
            for l in range(10):
                for r in range(l, r):
                    assert(Arithmetic.range_sum(a0, d, l, r)
                           == naive_range_sum(a0, d, l, r))

if __name__ == '__main__':
    main()
    print("Hello World")
