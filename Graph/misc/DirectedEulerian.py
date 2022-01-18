from DataStructure.UnionFind.UnionFind import UnionFind


class DirectedEulerian:
    def __init__(self, n):
        self.n = n
        self.digraph = [[] for i in range(n)]
        self.diff = [0] * n   # diff = outdeg - indeg
        self.uf = UnionFind(n)

    def add_edge(self, fr, to):
        self.digraph[fr].append(to)
        self.diff[fr] += 1
        self.diff[to] -= 1
        self.uf.merge(fr, to)

    def is_eulerian(self):
        if self.uf.count() != 1:
            # グラフが非連結なときは False を返す
            return False
        return all(self.diff[v] == 0 for v in range(self.n))

    def is_semi_eulerian(self):
        if self.uf.count() != 1:
            # グラフが非連結なときは False を返す
            return False, -1, -1
        s = [v for v in range(self.n) if self.diff[v] == 1]
        t = [v for v in range(self.n) if self.diff[v] == -1]
        if len(s) == 1 and len(t) == 1:
            return True, s[0], t[0]
        return False, -1, -1

    def euler_path(self, start):
        path = []
        if self.is_eulerian() or self.is_semi_eulerian()[0]:
            idxs = [0] * self.n
            stack = [start]
            while stack:
                v = stack[-1]
                if idxs[v] == len(self.digraph[v]):
                    path.append(v)
                    stack.pop()
                else:
                    nxt_v = self.digraph[v][idxs[v]]
                    stack.append(nxt_v)
                    idxs[v] += 1
            return True, path
        return False, path
