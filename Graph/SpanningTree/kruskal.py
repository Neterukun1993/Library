from operator import itemgetter
from DataStructure.UnionFind.UnionFind import UnionFind


def kruskal(n, edges):
    edges = sorted(edges, key=itemgetter(2))
    uf = UnionFind(n)
    res = 0
    for u, v, cost in edges:
        if not uf.same(u, v):
            uf.merge(u, v)
            res += cost
    return res
