# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_A
import sys
input = sys.stdin.buffer.readline

from Graph.misc.cycle_detection import cycle_detection


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]

    graph = [[] for i in range(n)]
    for u, v in edges:
        graph[u].append(v)

    cycle = cycle_detection(graph)
    if cycle:
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()
