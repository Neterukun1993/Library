# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
import sys
input = sys.stdin.buffer.readline

from NumberTheory.misc.matrix_pow import matrix_pow, matvec_mul


MOD = 10 ** 9 + 7
n = 10 ** 4


fib = [0] * (n + 1)
fib[1] = 1
for i in range(n - 1):
    fib[i + 2] = fib[i + 1] + fib[i]
    fib[i + 1] %= MOD


def fib_matrix_pow(k):
    mat = [[1, 1], [1, 0]]
    matpow = matrix_pow(mat, k, MOD)
    vec = matvec_mul(matpow, [1, 0], MOD)
    return vec[1]


def main():
    for i in range(n):
        assert(fib[i] == fib_matrix_pow(i))


if __name__ == '__main__':
    main()
    print("Hello World")
