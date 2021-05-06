# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2370
import sys
input = sys.stdin.readline

from Graph.misc.is_bipartite import is_bipartite
from DP.knapsack_bounded import knapsack_bounded


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]

    graph = [[] for i in range(n)]
    for u, v in edges:
        u -= 1
        v -= 1
        graph[u].append(v)
        graph[v].append(u)

    flag, cols, cnts = is_bipartite(graph)
    if not flag:
        print(-1)
        exit()

    diffs = [abs(b - w) for b, w in cnts]
    sum_d = sum(diffs)
    memo = {}
    for diff in diffs:
        memo[diff] = memo.get(diff, 0) + 1
    items = [(val, val, memo[val]) for val in memo]

    dp = knapsack_bounded(sum_d, items)
    diff = 10 ** 8
    for i, val in enumerate(dp):
        if val != 0:
            diff = min(abs(sum_d - 2 * val), diff)

    cntl, cntr = (n + diff) // 2, (n - diff) // 2
    print(cntl * cntr - m)


if __name__ == '__main__':
    main()
