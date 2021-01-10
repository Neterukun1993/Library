def rerooting(n, edges, unit, merge, addnode):
    root = 0
    tree = [[] for i in range(n)]
    idxs = [[] for i in range(n)]
    for u, v in edges:
        idxs[u].append(len(tree[v]))
        idxs[v].append(len(tree[u]))
        tree[u].append(v)
        tree[v].append(u)
    sub = [[unit] * len(tree[v]) for v in range(n)]
    noderes = [unit] * n

    # topological sort
    tp_order = []
    par = [-1] * n
    stack = [root]
    while stack:
        v = stack.pop()
        tp_order.append(v)
        for nxt_v in tree[v]:
            if nxt_v == par[v]:
                continue
            par[nxt_v] = v
            stack.append(nxt_v)

    # tree DP
    for v in reversed(tp_order[1:]):
        res = unit
        par_idx = -1
        for idx, nxt_v in enumerate(tree[v]):
            if nxt_v == par[v]:
                par_idx = idx
                continue
            res = merge(res, sub[v][idx])
        sub[par[v]][idxs[v][par_idx]] = addnode(res, v)

    # rerooting DP
    for v in tp_order:
        acc_back = [unit] * len(tree[v])
        for i in reversed(range(1, len(acc_back))):
            acc_back[i - 1] = merge(sub[v][i], acc_back[i])
        acc_front = unit
        for idx, nxt_v in enumerate(tree[v]):
            res = addnode(merge(acc_front, acc_back[idx]), v)
            sub[nxt_v][idxs[v][idx]] = res
            acc_front = merge(acc_front, sub[v][idx])
        noderes[v] = addnode(acc_front, v)
    return noderes
