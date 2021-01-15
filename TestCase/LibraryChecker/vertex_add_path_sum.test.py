# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_path_sum
import sys
input = sys.stdin.buffer.readline

from DataStructure.BinaryIndexedTree.PointAddRangeSum import BinaryIndexedTree
from Graph.Tree.HLDecomposition import HLDecomposition


def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    edges = [list(map(int, input().split())) for i in range(n - 1)]
    queries = [list(map(int, input().split())) for i in range(q)]

    tree = [[] for i in range(n)]
    for u, v in edges:
        tree[u].append(v)
        tree[v].append(u)

    hld = HLDecomposition(tree)
    bit = BinaryIndexedTree(n)

    for i, val in enumerate(a):
        bit.add(hld[i], val)

    ans = []
    for flag, u, v in queries:
        if flag == 0:
            val = v
            bit.add(hld[u], val)
        else:
            res = 0
            for l, r in hld.range_vertex_path(u, v):
                res += bit.sum(l, r)
            ans.append(res)

    print("\n".join(map(str, ans)))


if __name__ == '__main__':
    main()
