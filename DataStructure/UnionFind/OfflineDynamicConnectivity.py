from DataStructure.UnionFind.UnionFindUndo import UnionFindUndo


class OfflineDynamicConnectivity:
    def __init__(self, q, questions, n):
        self.q = q
        self.questions = questions
        self.n = n
        self.add_time = {}
        self.exist = {}
        self.pend = []

        self.size = 2 ** ((q - 1).bit_length())
        self.node = [[] for _ in range(2 * self.size)]
        self.uf = UnionFindUndo(n)

    def insert(self, t, u, v):
        """insert (u, v) edge at time t"""
        if u > v:
            u, v = v, u
        uv = u * self.n + v
        self.add_time[uv] = t
        self.exist[uv] = True

    def erase(self, t, u, v):
        """erase (u, v) edge at time t"""
        if u > v:
            u, v = v, u
        uv = u * self.n + v
        self.exist[uv] = False
        self.pend.append((self.add_time[uv], t, uv))

    def construct(self):
        """construct query on Segment Tree"""
        for uv in self.exist:
            if self.exist[uv]:
                self.pend.append((self.add_time[uv], self.q, uv))
        for l, r, uv in self.pend:
            self._add(l, r, uv)

    def run(self):
        """run queries and get results"""
        self.res = []
        self._dfs()
        return self.res

    def _add(self, l, r, uv):
        """add (u, v) edge in [l, r) of Segment Tree"""
        l, r = l + self.size, r + self.size
        while l < r:
            if l & 1:
                self.node[l].append(uv)
                l += 1
            if r & 1:
                r -= 1
                self.node[r].append(uv)
            l, r = l >> 1, r >> 1

    def _dfs(self, k=1):
        """DFS on Segment Tree"""
        if k >= self.size + self.q:
            return
        for uv in self.node[k]:  # pre-process
            u, v = divmod(uv, self.n)
            self.uf.merge(u, v)

        if k >= self.size:
            self.res.append(self.uf.same(*self.questions[k - self.size]))
        else:
            self._dfs(2 * k)
            self._dfs(2 * k + 1)

        for _ in range(len(self.node[k])):  # post-process
            self.uf.undo()
