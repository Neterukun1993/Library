# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_1_B
import sys
input = sys.stdin.buffer.readline

from DP.knapsack_01 import knapsack_01


def main():
    n, w = map(int, input().split())
    items = [list(map(int, input().split())) for i in range(n)]

    ans = knapsack_01(w, items)
    print(ans)


if __name__ == '__main__':
    main()
