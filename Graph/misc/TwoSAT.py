from Graph.Decomposition.SCC_Tarjan import StronglyConnectedComponents


class TwoSAT:
    def __init__(self, n):
        self.n = n
        self.scc = StronglyConnectedComponents(2 * n)
        self.ans = [False] * self.n

    def add_clause(self, i, f, j, g):
        self.scc.add_edge(2 * i + int(not f), 2 * j + int(g))
        self.scc.add_edge(2 * j + int(not g), 2 * i + int(f))

    def satisfy(self):
        self.scc.build()
        for i in range(self.n):
            if self.scc.labels[2 * i] == self.scc.labels[2 * i + 1]:
                return False
            self.ans[i] = self.scc.labels[2 * i] < self.scc.labels[2 * i + 1]
        return True

    def answer(self):
        return self.ans
