# verification-helper: PROBLEM https://judge.yosupo.jp/problem/cycle_detection
import sys
input = sys.stdin.buffer.readline

from Graph.misc.cycle_detection import cycle_detection


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for _ in range(m)]

    graph = [[] for i in range(n)]
    edge_idx = {}
    for i, (u, v) in enumerate(edges):
        graph[u].append(v)
        edge_idx[u, v] = i

    cycle = cycle_detection(graph)
    if not cycle:
        print(-1)
    else:
        print(len(cycle))
        for u, v in zip(cycle[0:], cycle[1:] + [cycle[0]]):
            print(edge_idx[u, v])


if __name__ == '__main__':
    main()
