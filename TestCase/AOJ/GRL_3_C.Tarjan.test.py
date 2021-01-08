# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_C
import sys
import sys
input = sys.stdin.buffer.readline

from Graph.Decomposition.SCC_Tarjan import StronglyConnectedComponents


def main():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    q = int(input())
    queries = [list(map(int, input().split())) for i in range(q)]

    scc = StronglyConnectedComponents(n)
    for v, nxt_v in edges:
        scc.add_edge(v, nxt_v)
    scc.build()

    ans = []
    for u, v in queries:
        ans.append(int(scc.labels[u] == scc.labels[v]))

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
