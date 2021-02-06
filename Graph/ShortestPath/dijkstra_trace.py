import heapq


def dijkstra(start, graph):
    INF = 10 ** 18
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0
    parent = [-1] * n
    q = [(0, start)]  # q = [(startからの距離, 現在地)]
    while q:
        d, v = heapq.heappop(q)
        if dist[v] < d:
            continue
        for nxt_v, cost in graph[v]:
            if dist[v] + cost < dist[nxt_v]:
                dist[nxt_v] = dist[v] + cost
                parent[nxt_v] = v
                heapq.heappush(q, (dist[nxt_v], nxt_v))
    return dist, parent


def trace_route(goal, parent):
    if parent[goal] == -1:
        return []
    path = []
    v = goal
    while v != -1:
        path.append(v)
        v = parent[v]
    return path[::-1]
