# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_C
import sys
input = sys.stdin.buffer.readline

from Graph.ShortestPath.bfs import bfs


def main():
    n = int(input())
    info = [list(map(int, input().split())) for i in range(n)]

    graph = [[] for _ in range(n)]
    for v, k, *nxt_vs in info:
        v -= 1
        for nxt_v in nxt_vs:
            nxt_v -= 1
            graph[v].append(nxt_v)

    dist = bfs(graph, 0)
    for i, d in enumerate(dist):
        if d == 10 ** 18:
            print(i + 1, -1)
        else:
            print(i + 1, d)


if __name__ == '__main__':
    main()
