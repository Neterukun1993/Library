# verification-helper: PROBLEM https://judge.yosupo.jp/problem/shortest_path
import sys
input = sys.stdin.buffer.readline

from Graph.ShortestPath.dijkstra_trace import dijkstra, trace_route


def main():
    n, m, s, t = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    INF = 10 ** 18

    graph = [[] for i in range(n)]
    edge_idx = {}
    for i, (u, v, cost) in enumerate(edges):
        graph[u].append((v, cost))

    dist, parent = dijkstra(s, graph)
    path = trace_route(t, parent)

    if not path:
        print(-1)
    else:
        es = []
        for u, v in zip(path, path[1:]):
            es.append((u, v))
        print(dist[t], len(es))
        for res in es:
            print(*res)

if __name__ == '__main__':
    main()
