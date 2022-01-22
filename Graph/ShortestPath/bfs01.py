# from collections import deque
from standard_library.collections import deque


def bfs01(graph, start):
    INF = 10 ** 18
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0
    que = deque([start])
    while que:
        v = que.popleft()
        for nxt_v, cost in graph[v]:
            d = dist[v] + cost
            if d < dist[nxt_v]:
                dist[nxt_v] = d
                if cost == 0:
                    que.appendleft(nxt_v)
                else:
                    que.append(nxt_v)
    return dist
