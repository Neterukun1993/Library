# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_B
import sys
input = sys.stdin.buffer.readline

from Graph.misc.topological_sorted import topological_sorted


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]

    graph = [[] for i in range(n)]
    for u, v in edges:
        graph[u].append(v)

    flag, tp_order = topological_sorted(graph)
    print('\n'.join(map(str, tp_order)))


if __name__ == '__main__':
    main()
