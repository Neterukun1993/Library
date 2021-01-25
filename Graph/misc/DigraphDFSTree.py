class DigraphDFSTree:
    def __init__(self, n):
        self.n = n
        self.digraph = [[] for _ in range(n)]
        self.dfstree = [[] for _ in range(n)]
        self.par = [-1] * n
        self.arrival = [-1] * n
        self.depature = [-1] * n
        self.roots = set()

    def add_edge(self, v, nxt_v):
        self.digraph[v].append(nxt_v)

    def build(self, root=None):
        k = 0
        idxs = [0] * self.n
        if root is not None:
            self.roots.add(v)
            self._dfs(v, idxs, k)
        else:
            for v in range(self.n):
                if self.arrival[v] == -1:
                    self.roots.add(v)
                    k = self._dfs(v, idxs, k)

    def _dfs(self, root, idxs, k):
        stack = [root]
        while stack:
            v = stack[-1]
            idx = idxs[v]
            if self.arrival[v] == -1:
                self.arrival[v] = k
                k += 1
            if idx < len(self.digraph[v]):
                nxt_v = self.digraph[v][idx]
                idxs[v] += 1
                if self.arrival[nxt_v] == -1:
                    self.dfstree[v].append(nxt_v)
                    self.par[nxt_v] = v
                    stack.append(nxt_v)
            else:
                self.depature[v] = k
                k += 1
                stack.pop()
        return k
