def topological_sorted(digraph):
    def dfs(v):
        if not visited[v]:
            for nxt_v in digraph[v]:
                dfs(nxt_v)
            visited[v] = True
            tp_order.append(v)

    n = len(digraph)
    visited = [False] * n
    tp_order = []
    for v in range(n):
        dfs(v)

    return tp_order[::-1]
