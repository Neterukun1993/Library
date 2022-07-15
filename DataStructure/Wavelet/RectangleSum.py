from DataStructure.Wavelet.BitVector import BitVector
from bisect import bisect_left


class RectangleSum:
    def __init__(self, ys, vals, MAXLOG=32):
        self.MAXLOG = MAXLOG
        self.n = len(vals)
        self.mat = []
        self.mid = []
        self.data = [[0] * (self.n + 1) for i in range(self.MAXLOG)]

        order = [i for i in range(self.n)]
        for d in reversed(range(self.MAXLOG)):
            vec = BitVector(self.n + 1)
            ls = []
            rs = []
            for i, od in enumerate(order):
                if ys[od] & (1 << d):
                    rs.append(od)
                    vec.set(i)
                else:
                    ls.append(od)
            vec.build()
            self.mat.append(vec)
            self.mid.append(len(ls))
            order = ls + rs
            for i, val in enumerate(order):
                self.data[- d - 1][i + 1] = self.data[- d - 1][i] + vals[val]

    def rect_sum(self, l, r, upper):
        res = 0
        for d in range(self.MAXLOG):
            if upper >> (self.MAXLOG - d - 1) & 1:
                res += self.data[d][self.mat[d].rank(r, 0)]
                res -= self.data[d][self.mat[d].rank(l, 0)]
                l = self.mat[d].rank(l, 1) + self.mid[d]
                r = self.mat[d].rank(r, 1) + self.mid[d]
            else:
                l = self.mat[d].rank(l, 0)
                r = self.mat[d].rank(r, 0)
        return res


class CompressedRectangleSum:
    def __init__(self, points):
        points = sorted(points)
        xs, ys, vals = zip(*points)
        self.xs = xs
        self.ys = sorted(set(ys))
        self.comp = {val: idx for idx, val in enumerate(self.ys)}
        ys = [self.comp[val] for val in ys]
        MAXLOG = len(self.ys).bit_length()
        self.mat = RectangleSum(ys, vals, MAXLOG)

    def rect_sum(self, l, r, lower, upper):
        l = bisect_left(self.xs, l)
        r = bisect_left(self.xs, r)
        lower = bisect_left(self.ys, lower)
        upper = bisect_left(self.ys, upper)
        return self.mat.rect_sum(l, r, upper) - self.mat.rect_sum(l, r, lower)
