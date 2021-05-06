# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from NumberTheory.ModularArithmetic.linear_congruence import linear_congruence


def test(a, b, m):
    _, ans, _ = linear_congruence(a, b, m)

    res = -1
    for i in range(m):
        if a * i % m == b % m:
            res = i
            break
    assert(ans == res)


def main():
    # ax = b (mod m)
    for a in range(50):
        for b in range(50):
            for m in range(1, 50):
                test(a, b, m)


if __name__ == '__main__':
    main()
    print("Hello World")
