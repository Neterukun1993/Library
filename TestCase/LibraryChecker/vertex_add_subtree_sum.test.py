# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum
import sys
input = sys.stdin.buffer.readline

from DataStructure.BinaryIndexedTree.PointAddRangeSum import BinaryIndexedTree
from Graph.Tree.HLDecomposition import HLDecomposition


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    p = list(map(int, input().split()))
    queries = [list(map(int, input().split())) for i in range(q)]

    tree = [[] for i in range(n)]
    for u, v in enumerate(p):
        u += 1
        tree[u].append(v)
        tree[v].append(u)

    hld = HLDecomposition(tree)
    bit = BinaryIndexedTree(n)

    for i, val in enumerate(a):
        bit.add(hld[i], val)

    ans = []
    for flag, *query in queries:
        if flag == 0:
            u, val = query
            bit.add(hld[u], val)
        else:
            u = query[0]
            l, r = hld.range_subtree(u)
            ans.append(bit.sum(l, r))

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
