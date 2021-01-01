class UnionFindWithPotential:
    def __init__(self, n):
        self.parent = [-1] * n
        self.pot = [0] * n
        self.cnt = n
        self.INF = 10 ** 18

    def root(self, x):
        if self.parent[x] < 0:
            return x
        rt = self.root(self.parent[x])
        self.pot[x] += self.pot[self.parent[x]]
        self.parent[x] = rt
        return rt

    def merge(self, x, y, potential):
        """merge x and y in pot[x] = pot[y] + potential"""
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return False
        if self.parent[root_x] < self.parent[root_y]:
            self.parent[root_x] += self.parent[root_y]
            self.parent[root_y] = root_x
            self.pot[root_y] = -potential + self.pot[x] - self.pot[y]
        else:
            self.parent[root_y] += self.parent[root_x]
            self.parent[root_x] = root_y
            self.pot[root_x] = potential - self.pot[x] + self.pot[y]
        self.cnt -= 1
        return True

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def diff(self, x, y):
        """get x's potential on a reference point y"""
        if not self.same(x, y):
            # potential is not defined between x and y
            return self.INF
        return self.pot[x] - self.pot[y]

    def size(self, x):
        return -self.parent[self.root(x)]

    def count(self):
        return self.cnt
