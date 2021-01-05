# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_palindromes
import sys
input = sys.stdin.readline

from String.Manacher import Manacher


def main():
    s = input().replace('\n', '')
    mn = Manacher(s)

    print(*mn.len_p[1:-1])


if __name__ == '__main__':
    main()
