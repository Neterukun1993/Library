class HLDecomposition:
    def __init__(self, tree):
        self.tree = tree
        self.n = len(tree)
        self.par = [-1] * self.n
        self.size = [1] * self.n
        self.depth = [0] * self.n
        self.preorder = [0] * self.n
        self.head = [i for i in range(self.n)]
        self.k = 0

        for v in range(self.n):
            if self.par[v] == -1:
                self._dfs_pre(v)
                self._dfs_hld(v)

    def __getitem__(self, v):
        return self.preorder[v]

    def _dfs_pre(self, v):
        tree = self.tree
        stack = [v]
        order = [v]
        while stack:
            v = stack.pop()
            for chi_v in tree[v]:
                if chi_v == self.par[v]:
                    continue
                self.par[chi_v] = v
                self.depth[chi_v] = self.depth[v] + 1
                stack.append(chi_v)
                order.append(chi_v)

        for v in reversed(order):
            tree_v = tree[v]
            if len(tree_v) and tree_v[0] == self.par[v]:
                tree_v[0], tree_v[-1] = tree_v[-1], tree_v[0]
            for idx, chi_v in enumerate(tree_v):
                if chi_v == self.par[v]:
                    continue
                self.size[v] += self.size[chi_v]
                if self.size[chi_v] > self.size[tree_v[0]]:
                    tree_v[idx], tree_v[0] = tree_v[0], tree_v[idx]

    def _dfs_hld(self, v):
        stack = [v]
        while stack:
            v = stack.pop()
            self.preorder[v] = self.k
            self.k += 1
            if len(self.tree[v]) == 0:
                continue
            top = self.tree[v][0]
            for chi_v in reversed(self.tree[v]):
                if chi_v == self.par[v]:
                    continue
                if chi_v == top:
                    self.head[chi_v] = self.head[v]
                else:
                    self.head[chi_v] = chi_v
                stack.append(chi_v)

    def lca(self, u, v):
        while u != -1 and v != -1:
            if self.preorder[u] > self.preorder[v]:
                u, v = v, u
            if self.head[u] == self.head[v]:
                return u
            v = self.par[self.head[v]]
        return -1

    def distance(self, u, v):
        lca_uv = self.lca(u, v)
        if lca_uv == -1:
            return -1
        else:
            return self.depth[u] + self.depth[v] - 2 * self.depth[lca_uv]

    def range_vertex_path(self, u, v):
        while True:
            if self.preorder[u] > self.preorder[v]:
                u, v = v, u
            l = max(self.preorder[self.head[v]], self.preorder[u])
            r = self.preorder[v]
            yield l, r + 1
            if self.head[u] != self.head[v]:
                v = self.par[self.head[v]]
            else:
                return

    def range_edge_path(self, u, v):
        while True:
            if self.preorder[u] > self.preorder[v]:
                u, v = v, u
            if self.head[u] != self.head[v]:
                yield self.preorder[self.head[v]], self.preorder[v] + 1
                v = self.par[self.head[v]]
            else:
                if u != v:
                    yield self.preorder[u] + 1, self.preorder[v] + 1
                break

    def range_subtree(self, u):
        return self.preorder[u], self.preorder[u] + self.size[u]
