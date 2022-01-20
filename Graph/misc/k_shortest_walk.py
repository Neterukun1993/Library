# from heapq import heappop, heappush
from standard_library.heapq import heappop, heappush
from DataStructure.Heap.PersistentLeftistHeap import LeftistHeap


# https://qiita.com/hotman78/items/42534a01c4bd05ed5e1e
def k_shortest_walk(n, edges, start, goal, k):
    INF = 10 ** 18
    graph = [[] for _ in range(n)]
    rev_graph = [[] for _ in range(n)]
    for i, (u, v, cost) in enumerate(edges):
        graph[u].append((v, cost, i))
        rev_graph[v].append((u, cost, i))

    potential = [INF] * n
    potential[goal] = 0
    parent = [-1] * n
    children = [[] for i in range(n)]
    idxs = [-1] * n

    que = [(0, goal)]
    while que:
        d, v = heappop(que)
        if potential[v] < d:
            continue
        for nxt_v, cost, idx in rev_graph[v]:
            if potential[v] + cost < potential[nxt_v]:
                potential[nxt_v] = potential[v] + cost
                parent[nxt_v] = v
                idxs[nxt_v] = idx
                heappush(que, (potential[nxt_v], nxt_v))

    for v in range(n):
        if parent[v] != -1:
            children[parent[v]].append(v)

    heap_g = [LeftistHeap() for _ in range(n)]
    que = [goal]
    iq = 0
    while iq < len(que):
        v = que[iq]
        iq += 1
        if parent[v] != -1:
            heap_g[v] = LeftistHeap.merge(heap_g[v], heap_g[parent[v]])
        for nxt_v, cost, idx in graph[v]:
            if idxs[v] != idx:
                heap_g[v] = heap_g[v].insert(
                    cost - potential[v] + potential[nxt_v], nxt_v)
        for nxt_v in children[v]:
            que.append(nxt_v)

    src = LeftistHeap().insert(potential[start], start)
    que = [(potential[start], src)]
    ans = []
    while que:
        val, hp = heappop(que)
        if val >= INF:
            break
        ans.append(val)
        if len(ans) == k:
            break
        if hp.a:
            heappush(que, (val + hp.a.find_min[0] - hp.find_min[0], hp.a))
        if hp.b:
            heappush(que, (val + hp.b.find_min[0] - hp.find_min[0], hp.b))
        to = hp.find_min[1]
        if heap_g[to]:
            heappush(que, (val + heap_g[to].find_min[0], heap_g[to]))

    for _ in range(len(ans), k):
        ans.append(-1)
    return ans
