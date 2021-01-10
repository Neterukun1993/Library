def diameter(tree):
    def _dfs(start):
        dist = [-1] * n
        dist[start] = 0
        stack = [start]
        while stack:
            v = stack.pop()
            for nxt_v, cost in tree[v]:
                if dist[nxt_v] != -1:
                    continue
                dist[nxt_v] = dist[v] + cost
                stack.append(nxt_v)
        max_d = max(dist)
        return dist.index(max_d), max_d, dist

    n = len(tree)
    u, _, _ = _dfs(0)
    v, diam, dist = _dfs(u)
    path = [v]
    while v != u:
        for nxt_v, cost in tree[v]:
            if cost + dist[nxt_v] == dist[v]:
                path.append(nxt_v)
                v = nxt_v
                break
    return diam, path
