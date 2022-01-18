from DataStructure.UnionFind.UnionFind import UnionFind


class UndirectedEulerian:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for i in range(n)]
        self.deg = [0] * n
        self.uf = UnionFind(n)

    def add_edge(self, u, v):
        u_idx = len(self.graph[u])
        v_idx = len(self.graph[v])
        if u == v:
            v_idx += 1
        self.graph[u].append((v, v_idx))
        self.graph[v].append((u, u_idx))
        self.deg[u] += 1
        self.deg[v] += 1
        self.uf.merge(u, v)

    def is_eulerian(self):
        if self.uf.count() != 1:
            # グラフが非連結なときは False を返す
            return False
        return all(self.deg[v] % 2 == 0 for v in range(self.n))

    def is_semi_eulerian(self):
        if self.uf.count() != 1:
            # グラフが非連結なときは False を返す
            return False, -1, -1
        s = [v for v in range(self.n) if self.deg[v] % 2 == 1]
        if len(s) == 2:
            return True, s[0], s[1]
        return False, -1, -1

    def euler_path(self, start):
        path = []
        semi, s, t = self.is_semi_eulerian()
        if self.is_eulerian() or s == start or t == start:
            idxs = [0] * self.n
            used = [[False] * len(self.graph[v]) for v in range(self.n)]
            stack = [start]
            while stack:
                v = stack[-1]
                if idxs[v] == len(self.graph[v]):
                    path.append(v)
                    stack.pop()
                else:
                    idx = idxs[v]
                    nxt_v, nxt_idx = self.graph[v][idx]
                    if not used[v][idx]:
                        used[v][idx] = True
                        used[nxt_v][nxt_idx] = True
                        stack.append(nxt_v)
                    idxs[v] += 1
            return True, path
        else:
            return False, path
