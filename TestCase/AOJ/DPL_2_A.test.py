# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_2_A
import sys
input = sys.stdin.buffer.readline

from Graph.ShortestPath.tsp import tsp


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    INF = 10 ** 18

    matrix = [[INF] * n for i in range(n)]
    for a, b, cost in edges:
        matrix[a][b] = cost
    for i in range(n):
        matrix[i][i] = 0

    ans, path = tsp(matrix)
    if ans == INF:
        print(-1)
    else:
        print(ans)


if __name__ == '__main__':
    main()
