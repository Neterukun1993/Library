from DataStructure.UnionFind.UnionFind import UnionFind


def boruvka(n, edges):
    INF = 10 ** 18
    uf = UnionFind(n)
    res = 0
    while uf.cnt != 1:
        update = False
        min_costs = [(INF, -1, -1) for _ in range(n)]
        for u, v, cost in edges:
            if not uf.same(u, v):
                rt_u = uf.root(v)
                rt_v = uf.root(u)
                min_costs[rt_u] = min(min_costs[rt_u], (cost, u, v))
                min_costs[rt_v] = min(min_costs[rt_v], (cost, u, v))
        for cost, u, v in min_costs:
            if cost != INF and not uf.same(u, v):
                update = True
                uf.merge(u, v)
                res += cost
        if not update:
            return -1
    return res
