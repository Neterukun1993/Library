class MinCostFlow:
    def __init__(self, n):
        self.INF = 10 ** 9 + 7
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap, cost):
        fr_idx = len(self.graph[fr])
        to_idx = len(self.graph[to])
        if fr == to:
            to_idx += 1
        self.graph[fr].append([to, to_idx, cap, cost])
        self.graph[to].append([fr, fr_idx, 0, -cost])

    def min_cost_flow(self, s, t, flow) -> int:
        res = 0
        potential = [0] * self.n
        prv_v = [0] * self.n
        prv_e = [None] * self.n
        while flow > 0:
            # ポテンシャルを用いたダイクストラ法
            dist = [self.INF] * self.n
            dist[s] = 0
            q = [(0, s)]  # q = [(sからのコスト, 現在地)]
            while q:
                cost, fr = heapq.heappop(q)
                if dist[fr] < cost:
                    continue
                for edge in self.graph[fr]:
                    to, _, cap, cost = edge
                    p_diff = potential[fr] - potential[to]
                    if cap > 0 and dist[fr] + cost + p_diff < dist[to]:
                        dist[to] = dist[fr] + cost + p_diff
                        prv_v[to] = fr
                        prv_e[to] = edge
                        heapq.heappush(q, (dist[to], to))

            if dist[t] == self.INF:
                return -1
            for i in range(self.n):
                if dist[i] != self.INF:
                    potential[i] += dist[i]
            d = flow
            v = t
            while v != s:
                d = min(d, prv_e[v][2])
                v = prv_v[v]
            flow -= d
            res += potential[t] * d
            v = t
            while v != s:
                edge = prv_e[v]
                edge[2] -= d
                self.graph[edge[0]][edge[1]][2] += d
                v = prv_v[v]
        return res
