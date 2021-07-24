from Graph.Tree.topological_sorted import topological_sorted


def dsu_on_tree(tree, root, add, sub, query):
    n = len(tree)
    tp_order, par = topological_sorted(tree, root)

    # 1.有向木の構築
    di_tree = [[] for i in range(n)]
    for v in range(n):
        for nxt_v in tree[v]:
            if nxt_v == par[v]:
                continue
            di_tree[v].append(nxt_v)

    # 2.部分木サイズの計算
    sub_size = [1] * n
    for v in tp_order[::-1]:
        for nxt_v in di_tree[v]:
            sub_size[v] += sub_size[nxt_v]

    # 3.有向木のDFS行きがけ順の構築
    di_tree = [sorted(tr, key=lambda v: sub_size[v]) for tr in di_tree]
    keeps = [0] * n
    for v in range(n):
        di_tree[v] = di_tree[v][:-1][::-1] + di_tree[v][-1:]
        for chi_v in di_tree[v][-1:]:
            keeps[chi_v] = 1
    tp_order, _ = topological_sorted(di_tree, root)

    # 部分木からの加算もしくは減算
    def calc(sub_root, is_add):
        stack = [sub_root]
        while stack:
            v = stack.pop()
            add(v) if is_add else sub(v)
            for chi_v in di_tree[v]:
                stack.append(chi_v)

    # 4.有向木のDFS帰りがけ順で頂点vの部分木クエリを処理
    for v in tp_order[::-1]:
        for chi_v in di_tree[v]:
            if keeps[chi_v] == 0:
                calc(chi_v, 1)
        add(v)
        # ここでクエリを実行する
        query(v)
        if keeps[v] == 0:
            calc(v, 0)
