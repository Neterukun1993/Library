class LowLink:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.dfstree = [[] for _ in range(n)]
        self.par = [-1] * n
        self.ord = [-1] * n
        self.low = [-1] * n
        self.articulations = []
        self.bridges = []
        self.roots = set()

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def build(self):
        k = 0
        self.edge_cnt = {}
        for v in range(self.n):
            for nxt_v in self.graph[v]:
                self.edge_cnt[v, nxt_v] = self.edge_cnt.get((v, nxt_v), 0) + 1
        idxs = [0] * self.n
        arts = [False] * self.n
        for v in range(self.n):
            if self.ord[v] == -1:
                self.roots.add(v)
                k = self._dfs(v, idxs, arts, k)

    def _dfs(self, root, idxs, arts, k):
        stack = [root]
        while stack:
            v = stack[-1]
            if v < 0:
                v = ~v
                par_v = self.par[v]
                self.low[par_v] = min(self.low[par_v], self.low[v])
                arts[par_v] |= (self.par[par_v] != -1 and self.ord[par_v] <= self.low[v])
                if self.ord[par_v] < self.low[v]:
                    self.bridges.append((par_v, v))
                stack.pop()
                continue
            idx = idxs[v]
            if self.ord[v] == -1:
                self.ord[v] = self.low[v] = k
                k += 1
            if idx < len(self.graph[v]):
                nxt_v = self.graph[v][idx]
                idxs[v] += 1
                if nxt_v == self.par[v] and self.edge_cnt[v, nxt_v] == 1:
                    continue 
                elif self.ord[nxt_v] == -1:
                    self.dfstree[v].append(nxt_v)
                    self.dfstree[nxt_v].append(v)
                    self.par[nxt_v] = v
                    stack.append(~nxt_v)
                    stack.append(nxt_v)
                else:
                    self.low[v] = min(self.low[v], self.ord[nxt_v])
            else:
                arts[v] |= (root == v and len(self.dfstree[v]) >= 2)
                if arts[v]:
                    self.articulations.append(v)
                stack.pop()
        return k

    def enumerate_articulations(self):
        for v in self.articulations:
            yield v

    def enumerate_bridges(self):
        for u, v in self.bridges:
            yield u, v
