# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A
import sys
input = sys.stdin.readline

from Graph.SpanningTree.prim import prim


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]

    graph = [[] for i in range(n)]
    for u, v, cost in edges:
        graph[u].append((v, cost))
        graph[v].append((u, cost))

    print(prim(graph))


if __name__ == '__main__':
    main()
