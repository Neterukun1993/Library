# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_C
import sys
input = sys.stdin.readline

from Graph.ShortestPath.warshall_floyd import warshall_floyd


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    INF = 10 ** 18

    matrix = [[INF] * n for i in range(n)]
    for v in range(n):
        matrix[v][v] = 0
    for u, v, cost in edges:
        matrix[u][v] = cost

    dist = warshall_floyd(matrix)

    negative = False
    for v in range(n):
        if dist[v][v] < 0:
            negative = True

    if negative:
        print("NEGATIVE CYCLE")
    else:
        for res in dist:
            print(*[num if num < 10 ** 15 else "INF" for num in res])


if __name__ == '__main__':
    main()
