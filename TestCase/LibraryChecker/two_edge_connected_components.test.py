# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_edge_connected_components
import sys
input = sys.stdin.buffer.readline

from Graph.Decomposition.TwoEdgeConnectedComponents import TwoEdgeConnectedComponents


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]

    tecc = TwoEdgeConnectedComponents(n)
    for u, v in edges:
        tecc.add_edge(u, v)

    tecc.build()
    gp = tecc.groups()

    print(len(gp))
    for res in gp:
        print(len(res), *res)


if __name__ == '__main__':
    main()
