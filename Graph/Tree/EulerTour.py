class EulerTour:
    def __init__(self, tree, root):
        self.n = len(tree)
        self.tree = tree
        self.par = [-1] * self.n
        self.begin = [-1] * self.n
        self.end = [-1] * self.n
        self.walk_order = []

        self._traversal(root)
        self._build_lca()

    def _traversal(self, rt):
        stack = [rt, 0]
        self.begin[rt] = len(self.walk_order)
        self.walk_order.append(rt)
        while stack:
            v, idx = stack[-2:]
            if idx < len(self.tree[v]):
                nxt_v = self.tree[v][idx]
                stack[-1] += 1
                if nxt_v == self.par[v]:
                    continue
                self.begin[nxt_v] = len(self.walk_order)
                self.walk_order.append(nxt_v)
                self.par[nxt_v] = v
                stack.append(nxt_v)
                stack.append(0)
            else:
                self.end[v] = len(self.walk_order)
                if self.par[v] != -1:
                    self.walk_order.append(self.par[v])
                stack.pop()
                stack.pop()

    def _build_lca(self):
        self.depth = self.walk_order[:]
        d = 0
        for i, (prv_v, v) in enumerate(zip(self.walk_order, self.walk_order[1:])):
            if self.par[v] == -1: d = 0
            elif self.par[v] == prv_v: d += 1
            else: d -= 1
            self.depth[i + 1] = (d << 32) + v
        self._build_rmq()

    def _build_rmq(self):
        size = len(self.depth)
        lg_size = size.bit_length()
        self.lg = [0] * (size + 1)
        for i in range(2, size + 1):
            self.lg[i] = self.lg[i // 2] + 1

        self.tbl = [[0] * size for _ in range(lg_size)]
        tbl = self.tbl
        for i, val in enumerate(self.depth):
            tbl[0][i] = val
        for k in range(lg_size - 1):
            for i in range(size - (1 << k + 1) + 1):
                tbl[k + 1][i] = min(tbl[k][i], tbl[k][i + (1 << k)])

    def _min_query(self, l, r):
        k = self.lg[r - l]
        return min(self.tbl[k][l], self.tbl[k][r - (1 << k)])

    def lca(self, u, v):
        if self.begin[u] > self.begin[v]:
            u, v = v, u
        l, r = self.begin[u], self.begin[v] + 1
        lca_uv = self._min_query(l, r) & ((1 << 32) - 1)
        return lca_uv

    def distance(self, u, v):
        lca_uv = self.lca(u, v)
        return self.depth[u] + self.depth[v] - 2 * self.depth[lca_uv]
