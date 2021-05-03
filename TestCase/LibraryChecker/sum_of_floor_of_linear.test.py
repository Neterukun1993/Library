# verification-helper: PROBLEM https://judge.yosupo.jp/problem/sum_of_floor_of_linear
import sys
input = sys.stdin.buffer.readline

from NumberTheory.misc.floor_sum import floor_sum


def main():
    t = int(input())
    for _ in range(t):
        n, m, a, b = map(int, input().split())

        ans = floor_sum(n, m, a, b)
        print(ans)


if __name__ == '__main__':
    main()
