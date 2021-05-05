# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=2821
import sys
input = sys.stdin.buffer.readline

from Graph.Tree.treehash import treehash
from DataStructure.UnionFind.UnionFind import UnionFind


def main():
    n1, m1 = map(int, input().split())
    edges1 = [list(map(int, input().split())) for i in range(m1)]
    n2 = int(input())
    edges2 = [list(map(int, input().split())) for i in range(n2 - 1)]

    tree2 = [[] for i in range(n2)]
    for u, v in edges2:
        u -= 1
        v -= 1
        tree2[u].append(v)
        tree2[v].append(u)
    res = treehash(tree2, root=None)

    uf = UnionFind(n1)
    tree1 = [[] for i in range(n1)]
    for u, v in edges1:
        u -= 1
        v -= 1
        uf.merge(u, v)
        tree1[u].append(v)
        tree1[v].append(u)

    ans = 0
    for gp in uf.groups():
        mapping = {v: i for i, v in enumerate(gp)}
        tree = [[] for i in range(len(gp))]
        for v in gp:
            for nxt_v in tree1[v]:
                tree[mapping[v]].append(mapping[nxt_v])
        tmp = treehash(tree, root=None)
        if tmp == res:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
