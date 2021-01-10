# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_B
import sys
input = sys.stdin.buffer.readline

from Graph.Tree.rerooting import rerooting
from Graph.edge_to_vertex import edge_to_vertex


def main():
    n = int(input())
    edges = [list(map(int, input().split())) for i in range(n - 1)]
    edges, vals = edge_to_vertex(n, edges)

    unit = (0, 0)

    def merge(a, b):
        if a[0] > b[0]:
            return (a[0], b[0])
        return (b[0], a[0])

    def addnode(a, v):
        return (a[0] + vals[v], a[1] + vals[v])

    ans = rerooting(n + n - 1, edges, unit, merge, addnode)
    print(max([l1 + l2 for l1, l2 in ans[:n]]))


if __name__ == '__main__':
    main()
