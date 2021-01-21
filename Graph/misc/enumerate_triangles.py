def enumerate_triangles(edges, v_vals, MOD):
    n = len(v_vals)
    degs = [0] * n
    for u, v in edges:
        degs[u] += 1
        degs[v] += 1

    graph = [[] for i in range(n)]
    for u, v in edges:
        if v > u:
            u, v = v, u
        if degs[u] > degs[v]:
            u, v = v, u
        graph[u].append(v)

    cnt = 0
    res = 0
    flags = [False] * n

    # v -> nxt_v1, v -> nxt_v2 -> nxtnxt_v について nxt_v1 = nxtnxt_v 
    # 満たす頂点組を数え上げる
    for v in range(n):
        for nxt_v in graph[v]:
            flags[nxt_v] = True
        for nxt_v in graph[v]:
            for nxtnxt_v in graph[nxt_v]:
                if flags[nxtnxt_v]:
                    cnt += 1
                    res += v_vals[v] * v_vals[nxt_v] * v_vals[nxtnxt_v]
                    res %= MOD
        for nxt_v in graph[v]:
            flags[nxt_v] = False

    return cnt, res
