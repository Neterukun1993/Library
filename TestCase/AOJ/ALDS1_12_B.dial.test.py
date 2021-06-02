# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_B
import sys
input = sys.stdin.readline

from Graph.ShortestPath.dial import dial


def main():
    n = int(input())
    info = [list(map(int, input().split())) for i in range(n)]
    INF = 10 ** 18

    graph = [[] * n for i in range(n)]
    max_cost = 0
    for v in range(n):
        for j in range(1, len(info[v]) // 2):
            nxt_v, cost = info[v][slice(2 * j, 2 * (j + 1))]
            graph[v].append((nxt_v, cost))
            max_cost = max(max_cost, cost)

    dist = dial(graph, 0, max_cost)
    for v, ans in enumerate(dist):
        print(v, ans)


if __name__ == '__main__':
    main()
