# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from NumberTheory.misc.euler_phi import euler_phi_table


def test():
    expected = [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4, 10, 4, 12, 6, 8]
    n = len(expected) - 1

    for i in range(n + 1):
        table = euler_phi_table(i)
        assert table == expected[:i + 1]


def main():
    test()


if __name__ == '__main__':
    main()
    print("Hello World")
