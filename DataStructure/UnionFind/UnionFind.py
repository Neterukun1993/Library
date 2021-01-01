class UnionFind:
    def __init__(self, n):
        self.parent = [-1] * n
        self.n = n
        self.cnt = n

    def root(self, x):
        if self.parent[x] < 0:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def merge(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x == y:
            return False
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.cnt -= 1
        return True

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.parent[self.root(x)]

    def count(self):
        return self.cnt

    def groups(self):
        res = [[] for _ in range(self.n)]
        for i in range(self.n):
            res[self.root(i)].append(i)
        return [group for group in res if group]
