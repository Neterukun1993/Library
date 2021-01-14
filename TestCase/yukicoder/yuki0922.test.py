# verification-helper: PROBLEM https://yukicoder.me/problems/no/922
import sys
input = sys.stdin.buffer.readline

from DataStructure.UnionFind.UnionFind import UnionFind
from Graph.Tree.DoublingLCA import DoublingLCA
from Graph.Tree.rerooting import rerooting


def main():
    n, m, q = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    queries = [list(map(int, input().split())) for i in range(q)]

    tree = [[] for i in range(n)]
    uf = UnionFind(n)
    for i, (u, v) in enumerate(edges):
        u -= 1
        v -= 1
        tree[u].append(v)
        tree[v].append(u)
        uf.merge(u, v)
        edges[i] = (u, v)

    ans = 0
    weights = [0] * n
    db = DoublingLCA(tree)
    for u, v in queries:
        u -= 1
        v -= 1
        dist = db.distance(u, v)
        if dist == -1:
            weights[u] += 1
            weights[v] += 1
        else:
            ans += dist

    unit = (0, 0)
    merge = lambda x1, x2: (x1[0] + x2[0], x1[1] + x2[1])
    addnode = lambda x1, v: (x1[0] + weights[v], x1[0] + x1[1])

    res = rerooting(n, edges, unit, merge, addnode)
    for gp in uf.groups():
        min_cost = 10 ** 9
        for i in gp:
            min_cost = min(res[i][1], min_cost)
        ans += min_cost

    print(ans)


if __name__ == '__main__':
    main()
