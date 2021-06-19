from DataStructure.UnionFind.UnionFind import UnionFind


def offline_lca(tree, queries, root):
    n = len(tree)
    q = len(queries)
    uf = UnionFind(n)
    par = [-1] * n
    anc = [-1] * n
    ans = [-1] * q
    qs = [[] for i in range(n)]
    for i, (u, v) in enumerate(queries):
        qs[u].append((v << 24) + i)
        qs[v].append((u << 24) + i)

    stack = [root]
    while stack:
        v = stack.pop()
        if v < 0:
            v = ~v
            for tmp in qs[v]:
                nxt_v = tmp >> 24
                i = tmp - (nxt_v << 24)
                ans[i] = anc[uf.root(nxt_v)]
            uf.merge(par[v], v)
            anc[uf.root(par[v])] = par[v]
            continue
        stack.append(~v)
        for nxt_v in tree[v]:
            if par[v] == nxt_v:
                continue
            par[nxt_v] = v
            stack.append(nxt_v)
    return ans
