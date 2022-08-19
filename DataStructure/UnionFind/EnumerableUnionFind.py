class EnumerableUnionFind:
    def __init__(self, n):
        self.next = [i for i in range(n)]
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
        root_x = self.root(x)
        root_y = self.root(y)
        if root_x == root_y:
            return False
        self.next[x], self.next[y] = self.next[y], self.next[x]
        if self.parent[root_x] > self.parent[root_y]:
            x, y = y, x
        self.parent[root_x] += self.parent[root_y]
        self.parent[root_y] = root_x
        self.cnt -= 1
        return True

    def same(self, x, y):
        return self.root(x) == self.root(y)

    def size(self, x):
        return -self.parent[self.root(x)]

    def count(self):
        return self.cnt

    def enumerate(self, x):
        res = []
        init_x = x
        while True:
            res.append(x)
            x = self.next[x]
            if x == init_x:
                break
        return res

    def groups(self):
        res = [[] for _ in range(self.n)]
        for i in range(self.n):
            res[self.root(i)].append(i)
        return [group for group in res if group]
