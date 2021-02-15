from Graph.Tree.topological_sorted import topological_sorted


def centroid(tree):
    n = len(tree)
    tp_order, par = topological_sorted(tree)
    sub_size = [0] * n
    res = []
    for v in tp_order[::-1]:
        is_centroid = True
        sub_size[v] = 1
        for nxt_v in tree[v]:
            if nxt_v == par[v]:
                continue
            if sub_size[nxt_v] > n // 2:
                is_centroid = False
            sub_size[v] += sub_size[nxt_v]
        if is_centroid and n - sub_size[v] <= n // 2:
            res.append(v)
    return res
