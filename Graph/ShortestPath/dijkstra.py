import heapq


def dijkstra(start, graph):
    INF = 10 ** 18
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0
    q = [(0, start)]  # q = [(startからの距離, 現在地)]
    while q:
        d, v = heapq.heappop(q)
        if dist[v] < d:
            continue
        for nxt_v, cost in graph[v]:
            if dist[v] + cost < dist[nxt_v]:
                dist[nxt_v] = dist[v] + cost
                heapq.heappush(q, (dist[nxt_v], nxt_v))
    return dist
