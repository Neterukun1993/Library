from DataStructure.Wavelet.BitVector import BitVector
from bisect import bisect_left


class _InnerRangeSetQuery:
    def __init__(self, ys, MAXLOG=32):
        self.MAXLOG = MAXLOG
        self.n = len(ys)
        self.mat = []
        self.mid = []

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

    def _rect_sum(self, l, r, upper):
        res = 0
        for d in range(self.MAXLOG):
            if upper >> (self.MAXLOG - d - 1) & 1:
                res += self.mat[d].rank(r, 0)
                res -= self.mat[d].rank(l, 0)
                l = self.mat[d].rank(l, 1) + self.mid[d]
                r = self.mat[d].rank(r, 1) + self.mid[d]
            else:
                l = self.mat[d].rank(l, 0)
                r = self.mat[d].rank(r, 0)
        return res


class RangeSetQuery:
    def __init__(self, array):
        limit = len(array)
        idxs = {}
        points = []
        for i, val in enumerate(c):
            if val in idxs:
                points.append((idxs[val], i))
            idxs[val] = i
        points.append((limit, limit))

        xs, ys = zip(*sorted(points))
        self.xs = xs
        self.ys = sorted(set(ys))
        comp = {val: idx for idx, val in enumerate(self.ys)}
        MAXLOG = len(self.ys).bit_length()
        self.mat = _InnerRangeSetQuery([comp[val] for val in ys], MAXLOG)

    def query(self, l, r):
        width = r - l
        lower = bisect_left(self.ys, l)
        upper = bisect_left(self.ys, r)
        l = bisect_left(self.xs, l)
        r = bisect_left(self.xs, r)
        return width - (self.mat._rect_sum(l, r, upper)
                        + self.mat._rect_sum(l, r, lower))
