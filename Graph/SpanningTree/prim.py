import heapq


def prim(graph):
    res = 0
    used = [False] * len(graph)
    hq = [(0, 0)]  # hq = [(辺のコスト, 現在地)]
    while hq:
        cost, v = heapq.heappop(hq)
        if used[v]:
            continue
        used[v] = True
        res += cost
        for nxt_v, cost in graph[v]:
            heapq.heappush(hq, (cost, nxt_v))
    return res
