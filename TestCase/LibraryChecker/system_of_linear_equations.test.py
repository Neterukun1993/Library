# verification-helper: PROBLEM https://judge.yosupo.jp/problem/system_of_linear_equations
import sys
input = sys.stdin.buffer.readline

from NumberTheory.ModularArithmetic.linear_equations import linear_equations


def main():
    n, m = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(n)]
    b = list(map(int, input().split()))

    dimension, result, basis_vectors = linear_equations(a, b)
    print(dimension)
    print(*result)
    for vector in basis_vectors:
        print(*vector)


if __name__ == '__main__':
    main()
