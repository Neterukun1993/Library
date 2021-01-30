from bisect import bisect_left


class SortedSetBIT:
    def __init__(self, cands):
        self.array = sorted(set(cands))
        self.comp = {val: i for i, val in enumerate(self.array)}
        self.size = len(self.array)
        self.cnt = 0
        self.bit = [0] * (self.size + 1)

    def __contains__(self, val):
        return self.count(val, val + 1) > 0

    def __len__(self):
        return self.cnt

    def _count(self, i):
        res = 0
        while i > 0:
            res += self.bit[i]
            i -= i & -i
        return res

    def add(self, val):
        if val in self:
            return False
        i = self.comp[val] + 1
        while i <= self.size:
            self.bit[i] += 1
            i += i & -i
        self.cnt += 1
        return True

    def remove(self, val):
        if val not in self:
            return False
        i = self.comp[val] + 1
        while i <= self.size:
            self.bit[i] -= 1
            i += i & -i
        self.cnt -= 1
        return True

    def count(self, vl, vr):
        l = bisect_left(self.array, vl)
        r = bisect_left(self.array, vr)
        return self._count(r) - self._count(l)

    def kth_smallest(self, k):
        if not(0 <= k < self.cnt):
            raise IndexError
        idx = 0
        k += 1
        d = 1 << self.size.bit_length()
        while d:
            if idx + d <= self.size and self.bit[idx + d] < k:
                k -= self.bit[idx + d]
                idx += d
            d >>= 1
        return self.array[idx]

    def kth_largest(self, k):
        return self.kth_smallest(self.cnt - k - 1)
