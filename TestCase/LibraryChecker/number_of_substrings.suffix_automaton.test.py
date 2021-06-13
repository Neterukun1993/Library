# verification-helper: PROBLEM https://judge.yosupo.jp/problem/number_of_substrings
import sys
input = sys.stdin.readline

from String.SuffixAutomaton import SuffixAutomaton


def main():
    s = input().replace('\n', '')

    sa = SuffixAutomaton()
    for char in s:
        sa.push(char)

    print(sa.number_of_substrings())


if __name__ == '__main__':
    main()
