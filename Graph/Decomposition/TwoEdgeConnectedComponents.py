from Graph.misc.LowLink import LowLink


class TwoEdgeConnectedComponents(LowLink):
    def build(self):
        super().build()
        self.labels = [-1] * self.n
        self.lb_cnt = 0
        for v in range(self.n):
            if self.labels[v] != -1:
                continue
            self.labels[v] = self.lb_cnt
            stack = [v]
            while stack:
                v = stack.pop()
                for nxt_v in self.graph[v]:
                    if self.ord[v] < self.low[nxt_v] or self.ord[nxt_v] < self.low[v]:
                        continue
                    if self.labels[nxt_v] != -1:
                        continue
                    self.labels[nxt_v] = self.lb_cnt
                    stack.append(nxt_v)
            self.lb_cnt += 1

    def groups(self):
        res = [[] for _ in range(self.lb_cnt)]
        for v, lb in enumerate(self.labels):
            res[lb].append(v)
        return res
