# verification-helper: PROBLEM https://judge.yosupo.jp/problem/kth_root_integer
import sys
input = sys.stdin.buffer.readline

from NumberTheory.misc.kth_root import kth_root


def main():
    t = int(input())

    for _ in range(t):
        a, k = map(int, input().split())
        print(kth_root(a, k))


if __name__ == '__main__':
    main()
