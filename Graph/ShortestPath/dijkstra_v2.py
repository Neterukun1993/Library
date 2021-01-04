def dijkstra_v2(start, matrix):
    INF = 10 ** 18
    n = len(matrix)
    used = [False] * n
    dist = [INF] * n
    dist[start] = 0
    while True:
        v = -1
        for u in range(n):
            if not used[u] and (v == -1 or dist[u] < dist[v]):
                v = u
        if v == -1:
            break
        used[v] = True
        for nxt_v in range(n):
            dist[nxt_v] = min(dist[nxt_v], dist[v] + matrix[v][nxt_v])
    return dist
