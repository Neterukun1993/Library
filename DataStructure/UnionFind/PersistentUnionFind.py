from DataStructure.misc.PersistentArray import (
    PersistentArray,
    init_persistent_array
)


class PersistentUnionFind:
    def __init__(self, n):
        if type(n) is int:
            self.parent = init_persistent_array([-1 for _ in range(n)])
        else:
            self.parent = n

    def root(self, x):
        px = self.parent.get(x)
        if px < 0:
            return x
        return self.root(px)

    def merge(self, x, y):
        x, y = self.root(x), self.root(y)
        if x == y:
            return self
        px = self.parent.get(x)
        py = self.parent.get(y)
        if px > py:
            x, y = y, x
        tmp = self.parent.set(y, x)
        return PersistentUnionFind(tmp.set(x, px + py))

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.parent.get(self.root(x))
