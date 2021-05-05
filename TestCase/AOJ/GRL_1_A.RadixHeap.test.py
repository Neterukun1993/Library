# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_A
import sys
input = sys.stdin.buffer.readline

from DataStructure.Heap.RadixHeap import RadixHeap
from Graph.ShortestPath.dijkstra_radix import dijkstra


def main():
    n, m, s = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    INF = 10 ** 18

    graph = [[] for i in range(n)]
    for u, v, cost in edges:
        graph[u].append((v, cost))

    dist = dijkstra(s, graph, INF)
    for val in dist:
        if val == INF:
            print("INF")
        else:
            print(val)


if __name__ == '__main__':
    main()
