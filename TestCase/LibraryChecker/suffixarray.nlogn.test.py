# verification-helper: PROBLEM https://judge.yosupo.jp/problem/suffixarray
import sys
input = sys.stdin.readline

from String.SA_nlogn import SuffixArray


def main():
    s = input().replace('\n', '')
    sa = SuffixArray(s)

    print(*sa.sa[1:])


if __name__ == '__main__':
    main()
