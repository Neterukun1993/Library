def dial(graph, start, max_w):
    INF = 10 ** 18
    n = len(graph)
    dist = [INF] * n
    dist[start] = 0
    stacks = [[] for i in range(max_w + 1)]
    stacks[0].append(start)
    for d in range(max_w * (n - 1) + 1):
        st = stacks[d % (max_w + 1)]
        while st:
            v = st.pop()
            if dist[v] < d:
                continue
            for nxt_v, cost in graph[v]:
                if dist[v] + cost < dist[nxt_v]:
                    dist[nxt_v] = dist[v] + cost
                    stacks[(d + cost) % (max_w + 1)].append(nxt_v)
    return dist
