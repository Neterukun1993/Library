def topological_sorted(tree, root=None):
    n = len(tree)
    par = [-1] * n
    tp_order = []
    for v in range(n):
        if par[v] != -1 or (root is not None and v != root):
            continue
        stack = [v]
        while stack:
            v = stack.pop()
            tp_order.append(v)
            for nxt_v in tree[v]:
                if nxt_v == par[v]:
                    continue
                par[nxt_v] = v
                stack.append(nxt_v)
    return tp_order, par
