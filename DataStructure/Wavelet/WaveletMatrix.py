from DataStructure.Wavelet.BitVector import BitVector
from bisect import bisect_left


class WaveletMatrix:
    def __init__(self, array, MAXLOG=32):
        self.MAXLOG = MAXLOG
        self.n = len(array)
        self.mat = []
        self.mid = []

        for d in reversed(range(self.MAXLOG)):
            vec = BitVector(self.n + 1)
            ls = []
            rs = []
            for i, val in enumerate(array):
                if (val >> d) & 1:
                    rs.append(val)
                    vec.set(i)
                else:
                    ls.append(val)
            vec.build()
            self.mat.append(vec)
            self.mid.append(len(ls))
            array = ls + rs

    def access(self, i):
        res = 0
        for d in range(self.MAXLOG):
            res <<= 1
            if self.mat[d][i]:
                res |= 1
                i = self.mat[d].rank(i, 1) + self.mid[d]
            else:
                i = self.mat[d].rank(i, 0)
        return res

    def rank(self, l, r, val):
        for d in range(self.MAXLOG):
            if val >> (self.MAXLOG - d - 1) & 1:
                l = self.mat[d].rank(l, 1) + self.mid[d]
                r = self.mat[d].rank(r, 1) + self.mid[d]
            else:
                l = self.mat[d].rank(l, 0)
                r = self.mat[d].rank(r, 0)
        return r - l

    def quantile(self, l, r, k):
        res = 0
        for d in range(self.MAXLOG):
            res <<= 1
            cntl, cntr = self.mat[d].rank(l, 0), self.mat[d].rank(r, 0)
            if k >= cntr - cntl:
                l = self.mat[d].rank(l, 1) + self.mid[d]
                r = self.mat[d].rank(r, 1) + self.mid[d]
                res |= 1
                k -= cntr - cntl
            else:
                l = cntl
                r = cntr
        return res

    def kth_smallest(self, l, r, k):
        return self.quantile(l, r, k)

    def kth_largest(self, l, r, k):
        return self.quantile(l, r, r - l - k - 1)

    def range_freq(self, l, r, upper):
        res = 0
        for d in range(self.MAXLOG):
            if upper >> (self.MAXLOG - d - 1) & 1:
                res += self.mat[d].rank(r, 0) - self.mat[d].rank(l, 0)
                l = self.mat[d].rank(l, 1) + self.mid[d]
                r = self.mat[d].rank(r, 1) + self.mid[d]
            else:
                l = self.mat[d].rank(l, 0)
                r = self.mat[d].rank(r, 0)
        return res

    def prev_val(self, l, r, upper):
        cnt = self.range_freq(l, r, upper)
        return None if cnt == 0 else self.kth_smallest(l, r, cnt - 1)

    def next_val(self, l, r, lower):
        cnt = self.range_freq(l, r, lower)
        return None if cnt == r - l else self.kth_smallest(l, r, cnt)


class CompressedWaveletMatrix:
    def __init__(self, array):
        self.vals = sorted(set(array))
        self.comp = {val: idx for idx, val in enumerate(self.vals)}
        array = [self.comp[val] for val in array]
        MAXLOG = len(self.vals).bit_length()
        self.wm = WaveletMatrix(array, MAXLOG)

    def access(self, i):
        return self.vals[self.wm.access(i)]

    def rank(self, l, r, val):
        return self.wm.rank(l, r, self.comp[val]) if val in self.comp else 0

    def kth_smallest(self, l, r, k):
        return self.vals[self.wm.kth_smallest(l, r, k)]

    def kth_largest(self, l, r, k):
        return self.vals[self.wm.kth_largest(l, r, k)]

    def range_freq(self, l, r, upper):
        upper = bisect_left(self.vals, upper)
        return self.wm.range_freq(l, r, upper)

    def prev_val(self, l, r, upper):
        upper = bisect_left(self.vals, upper)
        res = self.wm.prev_val(l, r, upper)
        return None if res is None else self.vals[res]

    def next_val(self, l, r, lower):
        lower = bisect_left(self.vals, lower)
        res = self.wm.next_val(l, r, lower)
        return None if res is None else self.vals[res]
