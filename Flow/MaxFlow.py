class MaxFlow:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.pos = []

    def add_edge(self, fr, to, cap):
        assert(0 <= fr < self.n)
        assert(0 <= to < self.n)
        assert(0 <= cap)
        fr_idx = len(self.graph[fr])
        to_idx = len(self.graph[to])
        if fr == to:
            to_idx += 1
        self.pos.append([fr, fr_idx])
        self.graph[fr].append([to, to_idx, cap])
        self.graph[to].append([fr, fr_idx, 0])

    def get_edge(self, i):
        assert(0 <= i < len(self.pos))
        edge = self.graph[self.pos[i][0]][self.pos[i][1]]
        rev_edge = self.graph[edge[0]][edge[1]]
        return (self.pos[i][0], edge[0], edge[2] + rev_edge[2], rev_edge[2])

    def edges(self):
        return [self.get_edge(i) for i in range(len(self.pos))]

    def change_edge(self, i, new_cap, new_flow):
        assert(0 <= i < len(self.pos))
        assert(0 <= new_flow <= new_cap)
        edge = self.graph[self.pos[i][0]][self.pos[i][1]]
        rev_edge = self.graph[edge[0]][edge[1]]
        edge[2] = new_cap - new_flow
        rev_edge[2] = new_flow

    def max_flow(self, s, t, flow_limit):
        assert(0 <= s < self.n)
        assert(0 <= s < self.n)
        assert(s != t)

        def bfs():
            level[s] = 0
            q = [s]
            head = 0
            while head < len(q):
                v = q[head]
                head += 1
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
                        to, rev, _ = self.graph[v][itr[v]]
                        flow = min(flow, self.graph[to][rev][2])
                    for v in stack:
                        self.graph[v][itr[v]][2] += flow
                        to, rev, _ = self.graph[v][itr[v]]
                        self.graph[to][rev][2] -= flow
                    return flow
                lv = level[v]
                while itr[v] < len(self.graph[v]):
                    to, rev, _ = self.graph[v][itr[v]]
                    if lv <= level[to] or self.graph[to][rev][2] == 0:
                        itr[v] += 1
                        continue
                    stack.append(to)
                    break
                if itr[v] == len(self.graph[v]):
                    stack.pop()
                    level[v] = self.n
            return 0

        flow = 0
        while flow < flow_limit:
            level = [-1] * self.n
            bfs()
            if level[t] == -1:
                break
            itr = [0] * self.n
            while flow < flow_limit:
                f = dfs(flow_limit - flow)
                if f == 0:
                    break
                flow += f
        return flow

    def min_cut(self, s):
        assert(0 <= s < self.n)
        visited = [False] * self.n
        stack = [s]
        visited[s] = True
        while stack:
            v = stack.pop()
            for to, _, cap in self.graph[v]:
                if cap > 0 and not visited[to]:
                    visited[to] = True
                    stack.append(to)
        return visited
