def bellman_ford(start, graph):
    INF = 10 ** 18
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0
    for _ in range(n):
        update = False
        for v, edges in enumerate(graph):
            for nxt_v, cost in edges:
                if dist[v] != INF and dist[nxt_v] > dist[v] + cost:
                    dist[nxt_v] = dist[v] + cost
                    update = True
        if not update:
            break
    else:
        return True, dist  # startから辿り着ける負閉路が存在
    return False, dist  # startから辿り着ける負閉路が存在しない
