from bisect import bisect_left


class PartiallyPersistentUnionFind:
    def __init__(self, n):
        self.INF = 10 ** 9
        self.parent = [-1] * n
        self.time = [self.INF] * n
        self.size = [[(-1, -1)] for i in range(n)]

    def root(self, t, x):
        while self.time[x] <= t:
            x = self.parent[x]
        return x

    def merge(self, t, x, y):
        x = self.root(t, x)
        y = self.root(t, y)
        if x == y:
            return False
        if self.parent[x] > self.parent[y]:
            x, y = y, x
        self.parent[x] += self.parent[y]
        self.size[x].append((t, self.parent[x]))
        self.parent[y] = x
        self.time[y] = t
        return True

    def same(self, t, x, y):
        return self.root(t, x) == self.root(t, y)

    def size(self, t, x):
        x = self.root(t, x)
        idx = bisect_left(self.size[x], (t, self.INF)) - 1
        return -self.size[x][idx][1]
