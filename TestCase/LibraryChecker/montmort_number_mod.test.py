# verification-helper: PROBLEM https://judge.yosupo.jp/problem/montmort_number_mod
import sys
input = sys.stdin.buffer.readline

from Combination.montmort_number import montmort_number, montmort_number2


def main():
    n, m = map(int, input().split())

    res = montmort_number(n, m)
    res2 = montmort_number2(n, m)
    assert(res == res2)
    print(*res[1:])


if __name__ == '__main__':
    main()
