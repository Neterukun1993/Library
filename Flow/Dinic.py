from collections import deque


class Dinic:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add_edge(self, fr, to, cap):
        fr_idx = len(self.graph[fr])
        to_idx = len(self.graph[to])
        if fr == to:
            to_idx += 1
        self.graph[fr].append([to, to_idx, cap])
        self.graph[to].append([fr, fr_idx, 0])

    def max_flow(self, s, t):
        def bfs():
            level[s] = 0
            q = deque([s])
            while q:
                v = q.popleft()
                for to, rev, cap in self.graph[v]:
                    if cap == 0 or level[to] >= 0:
                        continue
                    level[to] = level[v] + 1
                    if to == t:
                        return
                    q.append(to)

        def dfs(up):
            stack = [t]
            while stack:
                v = stack[-1]
                if v == s:
                    stack.pop()
                    flow = up
                    for v in stack:
                        to, rev, cap = self.graph[v][itr[v]]
                        flow = min(flow, self.graph[to][rev][2])
                    for v in stack:
                        self.graph[v][itr[v]][2] += flow
                        to, rev, cap = self.graph[v][itr[v]]
                        self.graph[to][rev][2] -= flow
                    return flow
                lv = level[v]
                while itr[v] < len(self.graph[v]):
                    to, rev, cap = self.graph[v][itr[v]]
                    if lv <= level[to] or self.graph[to][rev][2] == 0:
                        itr[v] += 1
                        continue
                    stack.append(to)
                    break
                if itr[v] == len(self.graph[v]):
                    stack.pop()
                    level[v] = self.n
            return 0

        limit = 10 ** 9 + 7
        flow = 0
        while flow < limit:
            level = [-1] * self.n
            bfs()
            if level[t] == -1:
                break
            itr = [0] * self.n
            while flow < limit:
                f = dfs(limit - flow)
                if f == 0:
                    break
                flow += f
        return flow
