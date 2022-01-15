import sys
sys.setrecursionlimit(10 ** 6)


# https://snuke.hatenablog.com/entry/2019/05/07/013609
class BipartiteMatching:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.graph = [[] for i in range(n)]
        self.p = [-1] * n
        self.q = [-1] * m

    def add_edge(self, u, v):
        assert(0 <= u <= self.n)
        assert(0 <= v <= self.m)
        self.graph[u].append(v)

    def maximum_matching(self):
        def dfs(v):
            # 非再帰に書き直したい
            if used[v]:
                return False
            used[v] = True
            for u in self.graph[v]:
                if self.q[u] == -1 or dfs(self.q[u]):
                    self.q[u] = v
                    self.p[v] = u
                    return True
            return False

        res = 0
        used = [False] * self.n
        update = True
        while update:
            update = False
            for v in range(self.n):
                if self.p[v] == -1 and dfs(v):
                    update = True
                    res += 1
            if update:
                used = [False] * self.n
        return res

    def matching_edges(self):
        edges = []
        for v in range(self.n):
            if self.p[v] != -1:
                edges.append((v, self.p[v]))
        return edges
