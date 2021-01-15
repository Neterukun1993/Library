# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_5_D
import sys
input = sys.stdin.buffer.readline

from DataStructure.BinaryIndexedTree.PointAddRangeSum import BinaryIndexedTree
from Graph.Tree.HLDecomposition import HLDecomposition


def main():
    n = int(input())
    nodes = [list(map(int, input().split())) for i in range(n)]
    q = int(input())
    queries = [list(map(int, input().split())) for i in range(q)]

    tree = [[] for i in range(n)]
    for u in range(n):
        for v in nodes[u][1:]:
            tree[u].append(v)
            tree[v].append(u)

    hld = HLDecomposition(tree)
    bit = BinaryIndexedTree(n)

    ans = []
    for flag, *query in queries:
        if flag == 0:
            v, val = query
            bit.add(hld[v], val)
        else:
            v = query[0]
            res = 0
            for l, r in hld.range_edge_path(0, v):
                res += bit.sum(l, r)
            ans.append(res)

    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
