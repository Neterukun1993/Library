from DataStructure.BinaryIndexedTree.PointAddRangeSum import BinaryIndexedTree
from Graph.Tree.EulerTour import EulerTour


class EulerTourPathQuery(EulerTour):
    def __init__(self, tree):
        super().__init__(tree, root=0)
        self.n = len(tree)
        self.bit = BinaryIndexedTree(2 * self.n)

    def build(self, vals):
        array = [0] * (2 * self.n)
        for i, idx in enumerate(self.begin):
            array[idx] = vals[i]
        for i, idx in enumerate(self.end):
            array[idx] = -vals[i]
        self.bit.build(array)

    def add(self, v, val):
        self.bit.add(self.begin[v], val)
        self.bit.add(self.end[v], -val)

    def vertex_path_sum(self, u, v):
        lca_uv = self.lca(u, v)
        res = self.bit.sum(self.begin[lca_uv], self.begin[u] + 1) \
            + self.bit.sum(self.begin[lca_uv] + 1, self.begin[v] + 1)
        return res

    def edge_path_sum(self, u, v):
        lca_uv = self.lca(u, v)
        res = self.bit.sum(self.begin[lca_uv] + 1, self.begin[u] + 1) \
            + self.bit.sum(self.begin[lca_uv] + 1, self.begin[v] + 1)
        return res
