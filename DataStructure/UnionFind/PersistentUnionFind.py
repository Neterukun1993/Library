from DataStructure.misc.PersistentArray import PersistentArray


class PersistentUnionFind:
    def __init__(self, n):
        self.parent = PersistentArray()
        self.rt = self.parent.build([-1] * n)

    def root(self, x, t):
        px = self.parent.get(x, t)
        if px < 0:
            return x
        return self.root(px, t)

    def merge(self, x, y, t):
        x, y = self.root(x, t), self.root(y, t)
        if x == y:
            return t
        px = self.parent.get(x, t)
        py = self.parent.get(y, t)
        if px > py:
            x, y = y, x
        tmp = self.parent.set(y, x, t)
        return self.parent.set(x, px + py, tmp)

    def same(self, x, y, t):
        return self.root(x, t) == self.root(y, t)

    def size(self, x, t):
        return -self.parent.get(self.root(x, t), t)
