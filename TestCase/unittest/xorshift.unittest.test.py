# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from misc.xorshift import xorshift32


def main():
    sample = [
        723471715,
        2497366906,
        2064144800,
        2008045182,
        3532304609,
        374114282,
        1350636274,
        691148861,
        746858951,
        2653896249
    ]

    for _ in range(2):
        xor32 = xorshift32()
        for val in sample:
            assert(val == xor32())


if __name__ == '__main__':
    main()
    print("Hello World")
