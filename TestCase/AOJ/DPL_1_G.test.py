# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_G
import sys
input = sys.stdin.buffer.readline

from DP.knapsack_bounded import knapsack_bounded


def main():
    n, w = map(int, input().split())
    items = [list(map(int, input().split())) for i in range(n)]

    ans = max(knapsack_bounded(w, items))
    print(ans)


if __name__ == '__main__':
    main()
