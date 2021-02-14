# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_B
import sys
input = sys.stdin.buffer.readline

from Graph.misc.topological_sorted import topological_sorted as kahn
from Graph.misc.topological_sorted_dfs import topological_sorted


def check(graph, tp_order):
    n = len(graph)
    idxs = [0] * n
    for i, v in enumerate(tp_order):
        idxs[v] = i
    for v in range(n):
        for nxt_v in graph[v]:
            if idxs[v] > idxs[nxt_v]:
                return False
    return True


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]

    graph = [[] for i in range(n)]
    for u, v in edges:
        graph[u].append(v)

    _, tp_order = kahn(graph)
    assert(check(graph, tp_order))

    tp_order = topological_sorted(graph)
    assert(check(graph, tp_order))

    print('\n'.join(map(str, tp_order)))


if __name__ == '__main__':
    main()
