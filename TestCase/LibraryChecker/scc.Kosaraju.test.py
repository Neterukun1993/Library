# verification-helper: PROBLEM https://judge.yosupo.jp/problem/scc
import sys
input = sys.stdin.buffer.readline

from Graph.Decomposition.SCC_Kosaraju import StronglyConnectedComponents


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]

    scc = StronglyConnectedComponents(n)
    for v, nxt_v in edges:
        scc.add_edge(v, nxt_v)
    scc.build()
    _, elems = scc.construct_dag()

    print(len(elems))
    for res in elems:
        print(len(res), *res)


if __name__ == '__main__':
    main()
