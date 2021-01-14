class DoublingLCA:
    def __init__(self, tree, root=None):
        self.n = len(tree)
        self.depth = [0] * self.n
        self.log_size = (self.n).bit_length()
        self.parent = [[-1] * self.n for i in range(self.log_size)]

        if root is None:
            for v in range(self.n):
                if self.parent[0][v] == -1:
                    self._dfs(v, tree)
        else:
            self._dfs(root, tree)

        for k in range(self.log_size - 1):
            for v in range(self.n):
                if self.parent[k][v] == -1:
                    self.parent[k + 1][v] = -1
                else:
                    self.parent[k + 1][v] = self.parent[k][self.parent[k][v]]

    def _dfs(self, rt, tree):
        stack = [(rt, -1)]
        while stack:
            v, par = stack.pop()
            for chi_v in tree[v]:
                if chi_v == par:
                    continue
                self.parent[0][chi_v] = v
                self.depth[chi_v] = self.depth[v] + 1
                stack.append((chi_v, v))

    def lca(self, u, v):
        if self.depth[u] > self.depth[v]:
            u, v = v, u
        for k in range(self.log_size):
            if ((self.depth[v] - self.depth[u]) >> k) & 1:
                v = self.parent[k][v]
        if u == v:
            return u
        for k in reversed(range(self.log_size)):
            if self.parent[k][u] != self.parent[k][v]:
                u = self.parent[k][u]
                v = self.parent[k][v]
        return self.parent[0][u]

    def distance(self, u, v):
        lca_uv = self.lca(u, v)
        if lca_uv == -1:
            return -1
        else:
            return self.depth[u] + self.depth[v] - 2 * self.depth[lca_uv]
