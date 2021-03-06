# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=NTL_1_C
import sys
input = sys.stdin.buffer.readline

from NumberTheory.Basic.gcd_lcm import lcm, all_lcm_int, all_lcm_dict


def main():
    n = int(input())
    a = list(map(int, input().split()))

    lcm0 = 1
    for val in a:
        lcm0 = lcm(lcm0, val)

    lcm1 = all_lcm_int(a)

    factors = all_lcm_dict(a)
    lcm2 = 1
    for val in factors:
        lcm2 *= val ** factors[val]

    assert(lcm0 == lcm1 and lcm1 == lcm2)
    print(lcm0)


if __name__ == '__main__':
    main()
