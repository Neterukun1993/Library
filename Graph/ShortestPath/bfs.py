from collections import deque


def bfs(graph, start):
    INF = 10 ** 18
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0
    que = deque([start])
    while que:
        v = que.popleft()
        for nxt_v in graph[v]:
            if dist[nxt_v] == INF:
                dist[nxt_v] = dist[v] + 1
                que.append(nxt_v)
    return dist
