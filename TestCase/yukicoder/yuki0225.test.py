# verification-helper: PROBLEM https://yukicoder.me/problems/no/225
import sys
input = sys.stdin.buffer.readline

from DP.levenshtein_distance import levenshtein_distance


def main():
    n, m = map(int, input().split())
    s = input()
    t = input()

    print(levenshtein_distance(s, t))


if __name__ == '__main__':
    main()
