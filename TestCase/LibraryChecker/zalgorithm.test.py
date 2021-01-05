# verification-helper: PROBLEM https://judge.yosupo.jp/problem/zalgorithm
import sys
input = sys.stdin.readline

from String.z_algorithm import z_algorithm


def main():
    s = input().replace('\n', '')
    ans = z_algorithm(s)
    print(*ans)


if __name__ == '__main__':
    main()
