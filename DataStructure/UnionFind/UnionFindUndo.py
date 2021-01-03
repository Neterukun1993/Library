class UnionFindUndo:
    def __init__(self, n):
        self.parent = [-1] * n
        self.history = []

    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            return self.root(self.parent[x])

    def merge(self, x, y):
        x = self.root(x)
        y = self.root(y)
        self.history.append((x, self.parent[x]))
        self.history.append((y, self.parent[y]))
        if x == y:
            return False
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        return True

    def undo(self):
        if not self.history:
            return False
        for _ in range(2):
            x, par_x = self.history.pop()
            self.parent[x] = par_x
        return True

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.parent[self.root(x)]
