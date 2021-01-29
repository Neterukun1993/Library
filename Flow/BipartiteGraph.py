from Flow.Dinic import Dinic


class BipartiteGraph:
    def __init__(self, na, nb):
        self.na = na
        self.nb = nb
        self.n = (na + nb + 2)
        self.s, self.t = self.n - 2, self.n - 1
        self.dc = Dinic(self.n)
        for va in range(na):
            self.dc.add_edge(self.s, va, 1)
        for vb in range(na, na + nb):
            self.dc.add_edge(vb, self.t, 1)

    def add_edge(self, ia, ib):
        self.dc.add_edge(ia, self.na + ib, 1)

    def maximum_matching(self):
        return self.dc.max_flow(self.s, self.t)

    def matching_edges(self):
        edges = []
        for ia in range(self.na):
            for ib, _, val in self.dc.graph[ia]:
                if ib == self.s:
                    continue
                if val == 0:
                    edges.append((ia, ib - self.na))
        return edges
