# verification-helper: PROBLEM https://judge.yosupo.jp/problem/matrix_rank_mod_2
import sys
input = sys.stdin.buffer.readline

from NumberTheory.ModularArithmetic.get_f2_basis import get_f2_basis


def main():
    n, m = map(int, input().split())
    if m == 0:
        a = [0 for _ in range(n)]
    else:
        a = [int(input(), 2) for _ in range(n)]

    base = get_f2_basis(a)
    print(len(base))


if __name__ == '__main__':
    main()
