from DataStructure.UnionFind.UnionFind import UnionFind
from DataStructure.Heap.SkewHeap import SkewHeap


def directed_mst(n, edges, root):
    OFFSET = m = len(edges)
    from_ = [0] * n
    from_cost = [0] * n
    from_heap = [SkewHeap() for i in range(n)]

    uf = UnionFind(n)
    par_e = [-1] * m
    stem = [-1] * n
    used = [0] * n
    used[root] = 2
    idxs = []

    for idx, (fr, to, cost) in enumerate(edges):
        from_heap[to].push(cost * OFFSET + idx)

    res = 0
    for v in range(n):
        if used[v] != 0:
            continue
        processing = []
        chi_e = []
        cycle = 0
        while used[v] != 2:
            used[v] = 1
            processing.append(v)
            if from_heap[v].empty():
                return -1, [-1] * n
            from_cost[v], idx = divmod(from_heap[v].pop(), OFFSET)
            from_[v] = uf.root(edges[idx][0])
            if stem[v] == -1:
                stem[v] = idx
            if from_[v] == v:
                continue
            res += from_cost[v]
            idxs.append(idx)
            while cycle:
                par_e[chi_e.pop()] = idx
                cycle -= 1
            chi_e.append(idx)
            if used[from_[v]] == 1:
                p = v
                while True:
                    if not from_heap[p].empty():
                        from_heap[p].add(-from_cost[p] * OFFSET)
                    if p != v:
                        uf.merge(v, p)
                        from_heap[v].meld(from_heap[p])
                    p = uf.root(from_[p])
                    new_v = uf.root(v)
                    from_heap[new_v] = from_heap[v]
                    v = new_v
                    cycle += 1
                    if p == v:
                        break
            else:
                v = from_[v]
        for v in processing:
            used[v] = 2

    used_e = [False] * m
    par = [-1] * n
    for idx in reversed(idxs):
        if used_e[idx]:
            continue
        fr, to, cost = edges[idx]
        par[to] = fr
        x = stem[to]
        while x != idx:
            used_e[x] = True
            x = par_e[x]
    return res, par
