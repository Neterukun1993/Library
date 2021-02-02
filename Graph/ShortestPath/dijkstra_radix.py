from DataStructure.Heap.RadixHeap import RadixHeap


def dijkstra(start, graph, LIMIT=1<<64):
    INF = 10 ** 18
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0
    rh = RadixHeap(LIMIT)
    rh.push(0, start)
    while rh:
        d, v = rh.pop()
        if dist[v] < d:
            continue
        for nxt_v, cost in graph[v]:
            if dist[v] + cost < dist[nxt_v]:
                dist[nxt_v] = dist[v] + cost
                rh.push(dist[nxt_v], nxt_v)
    return dist
