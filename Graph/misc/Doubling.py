class Doubling:
    def __init__(self, permutation, power=64):
        self.n = len(permutation)
        self.perm = permutation
        self.power = power
        self._build()

    def _build(self):
        self.next = [[0] * self.n for i in range(self.power)]
        for v in range(self.n):
            self.next[0][v] = self.perm[v]
        for k in range(self.power - 1):
            for v in range(self.n):
                self.next[k + 1][v] = self.next[k][self.next[k][v]]

    def dest(self, v, times):
        for k in range(self.power):
            if (times >> k) & 1:
                v = self.next[k][v]
        return v

    def build_path(self, values, op=max, e=-10**18):
        self.op = op
        self.e = e
        self.data = [[e] * self.n for i in range(self.power)]
        for v in range(self.n):
            self.data[0][v] = self.op(self.e, values[v])
        for k in range(self.power - 1):
            for v in range(self.n):
                self.data[k + 1][v] = self.op(self.data[k][v],
                                              self.data[k][self.next[k][v]])

    def fold(self, v, times):
        res = self.e
        for k in range(self.power):
            if (times >> k) & 1:
                res = self.op(res, self.data[k][v])
                v = self.next[k][v]
        return res

    def max_times(self, v, f):
        res = self.e
        times = 0
        for k in reversed(range(self.power)):
            if f(self.op(res, self.data[k][v])):
                res = self.op(res, self.data[k][v])
                times += 1 << k
                v = self.next[k][v]
        return times
