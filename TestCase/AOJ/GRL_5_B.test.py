# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_B
import sys
input = sys.stdin.buffer.readline

from Graph.Tree.rerooting import rerooting
from Graph.misc.edge_to_vertex import edge_to_vertex


def main():
    n = int(input())
    edges = [list(map(int, input().split())) for i in range(n - 1)]

    edges, vals = edge_to_vertex(n, edges)
    ans = rerooting(n + n - 1, edges, 0, max, lambda val, v: val + vals[v])

    print('\n'.join(map(str, ans[:n])))


if __name__ == '__main__':
    main()
