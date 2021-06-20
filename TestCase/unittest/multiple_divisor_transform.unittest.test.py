# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Convolution.multiple_divisor_transform import (
    multiple_zeta_transform,
    multiple_mobius_transform,
    divisor_zeta_transform,
    divisor_mobius_transform
)


def naive_count_divisors(n):
    """O(N^2) naive calculation"""
    res = [0] * n
    for val in range(1, n):
        for div in range(1, val + 1):
            if val % div == 0:
                res[val] += 1
    return res


def naive_count_multiples(n):
    """O(N^2) naive calculation"""
    res = [0] * n
    for div in range(1, n):
        for val in range(div, n):
            if val % div == 0:
                res[div] += 1
    return res


def test(n):
    op = lambda x, y: x + y
    inv = lambda x: -x

    arr = [1] * n
    arr[0] = 0

    mul_zeta = multiple_zeta_transform(arr, op)
    naive_mul_cnt = naive_count_multiples(n)
    assert(mul_zeta == naive_mul_cnt)

    div_zeta = divisor_zeta_transform(arr, op)
    naive_div_cnt = naive_count_divisors(n)
    assert(div_zeta == naive_div_cnt)

    mul_mobius = multiple_mobius_transform(mul_zeta, op, inv)
    assert(arr == mul_mobius)

    div_mobius = divisor_mobius_transform(div_zeta, op, inv)
    assert(arr == div_mobius)


def main():
    test(1000)


if __name__ == '__main__':
    main()
    print("Hello World")
