# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_1_B
import sys
input = sys.stdin.readline

from Graph.ShortestPath.bellman_ford import bellman_ford


def main():
    n, m, s = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    INF = 10 ** 18

    graph = [[] for i in range(n)]
    for u, v, cost in edges:
        graph[u].append((v, cost))

    negative, dist = bellman_ford(s, graph)
    if negative:
        print("NEGATIVE CYCLE")
    else:
        for val in dist:
            if val < 10 ** 15:
                print(val)
            else:
                print("INF")


if __name__ == '__main__':
    main()
