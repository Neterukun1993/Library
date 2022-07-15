from DataStructure.Wavelet.BitVector import BitVector
from DataStructure.BinaryIndexedTree.PointAddRangeSum import BinaryIndexedTree
from bisect import bisect_left


class PointAddRectangleSum:
    def __init__(self, ys, vals, MAXLOG=32):
        self.MAXLOG = MAXLOG
        self.n = len(ys)
        self.ys = ys
        self.mat = []
        self.mid = []
        self.data = []

        order = [i for i in range(self.n)]
        for d in reversed(range(self.MAXLOG)):
            vec = BitVector(self.n + 1)
            ls = []
            rs = []
            for i, od in enumerate(order):
                if (ys[od] >> d) & 1:
                    rs.append(od)
                    vec.set(i)
                else:
                    ls.append(od)
            vec.build()
            self.mat.append(vec)
            self.mid.append(len(ls))
            order = ls + rs
            self.data.append(BinaryIndexedTree(self.n))
            self.data[-1].build([vals[od] for od in order])

    def point_add(self, k, val):
        y = self.ys[k]
        for d in range(self.MAXLOG):
            if y >> (self.MAXLOG - d - 1) & 1:
                k = self.mat[d].rank(k, 1) + self.mid[d]
            else:
                k = self.mat[d].rank(k, 0)
            self.data[d].add(k, val)

    def rect_sum(self, l, r, upper):
        res = 0
        for d in range(self.MAXLOG):
            if upper >> (self.MAXLOG - d - 1) & 1:
                res += self.data[d].sum(self.mat[d].rank(l, 0), self.mat[d].rank(r, 0))
                l = self.mat[d].rank(l, 1) + self.mid[d]
                r = self.mat[d].rank(r, 1) + self.mid[d]
            else:
                l = self.mat[d].rank(l, 0)
                r = self.mat[d].rank(r, 0)
        return res


class CompressedPointAddRectangleSum:
    def __init__(self, points):
        points = sorted(points)
        xs, ys, vals = zip(*points)
        self.xs = xs
        self.ys = sorted(set(ys))
        self.idxs = {(x, y): idx for idx, (x, y, _) in enumerate(points)}
        self.comp = {val: idx for idx, val in enumerate(self.ys)}
        ys = [self.comp[val] for val in ys]
        MAXLOG = len(self.ys).bit_length()
        self.mat = PointAddRectangleSum(ys, vals, MAXLOG)

    def rect_sum(self, l, r, lower, upper):
        l = bisect_left(self.xs, l)
        r = bisect_left(self.xs, r)
        lower = bisect_left(self.ys, lower)
        upper = bisect_left(self.ys, upper)
        return self.mat.rect_sum(l, r, upper) - self.mat.rect_sum(l, r, lower)

    def point_add(self, x, y, val):
        if (x, y) not in self.idxs:
            raise KeyError(f'point(x={x}, y={y}) must be pre-given as an argument')
        idx = self.idxs[x, y]
        self.mat.point_add(idx, val)
