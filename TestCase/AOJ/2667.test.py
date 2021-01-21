# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2667
import sys
input = sys.stdin.buffer.readline

from DataStructure.BinaryIndexedTree.RangeAddRangeSum import BinaryIndexedTree
from Graph.Tree.HLDecomposition import HLDecomposition


def main():
    n, q = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(n - 1)]
    queries = [list(map(int, input().split())) for i in range(q)]

    tree = [[] for i in range(n)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    hld = HLDecomposition(tree)
    bit = BinaryIndexedTree(n)

    ans = []
    for flag, *query in queries:
        if flag == 0:
            u, v = query
            res = 0
            for l, r in hld.range_edge_path(u, v):
                res += bit.sum(l, r)
            ans.append(res)
        else:
            v, x = query
            l, r = hld.range_subtree(v)
            bit.add(l, r, x)
            bit.add(hld[v], hld[v] + 1, -x)
    print('\n'.join(map(str, ans)))


if __name__ == '__main__':
    main()
