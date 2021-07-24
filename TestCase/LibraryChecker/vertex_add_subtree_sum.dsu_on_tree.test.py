# verification-helper: PROBLEM https://judge.yosupo.jp/problem/vertex_add_subtree_sum
import sys
input = sys.stdin.buffer.readline

from DataStructure.BinaryIndexedTree.PointAddRangeSum import BinaryIndexedTree
from Graph.Tree.dsu_on_tree import dsu_on_tree


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

    ans = [-1] * (q + 1)
    update = [[] for i in range(n)]
    answer = [[] for i in range(n)]
    for i in range(n):
        update[i].append((0, a[i]))
    for t, (flag, *qu) in enumerate(queries, 1):
        if flag == 0:
            u, x = qu
            update[u].append((t, x))
        else:
            u = qu[0]
            answer[u].append(t)

    bit = BinaryIndexedTree(q + 1)

    def add(v):
        for t, val in update[v]:
            bit.add(t, val)

    def sub(v):
        for t, val in update[v]:
            bit.add(t, -val)

    def query(v):
        for t in answer[v]:
            ans[t] = bit.sum(0, t)

    dsu_on_tree(tree, 0, add, sub, query)
    print("\n".join(map(str, [val for val in ans if val != -1])))


if __name__ == '__main__':
    main()
