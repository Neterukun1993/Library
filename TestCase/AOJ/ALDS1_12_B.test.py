# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_12_B
import sys
input = sys.stdin.readline

from Graph.ShortestPath.dijkstra_v2 import dijkstra_v2


def main():
    n = int(input())
    edges = [list(map(int, input().split())) for i in range(n)]
    INF = 10 ** 18

    matrix = [[INF] * n for i in range(n)]
    for v in range(n):
        matrix[v][v] = 0
        for i in range(1, len(edges[v]) // 2):
            nxt_v, cost = edges[v][slice(2 * i, 2 * (i + 1))]
            matrix[v][nxt_v] = cost

    dist = dijkstra_v2(0, matrix)
    for v, ans in enumerate(dist):
        print(v, ans)


if __name__ == '__main__':
    main()
