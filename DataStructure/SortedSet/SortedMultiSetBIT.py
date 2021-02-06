from DataStructure.SortedSet.SortedSetBIT import SortedSetBIT


class SortedMultiSetBIT(SortedSetBIT):
    def __init__(self, cands):
        super().__init__(cands)

    def add(self, val):
        i = self.comp[val] + 1
        while i <= self.size:
            self.bit[i] += 1
            i += i & -i
        self.cnt += 1
        return True

    def all_remove(self, val):
        if val not in self:
            return False
        i = self.comp[val] + 1
        cnt = self._count(i) - self._count(i - 1)
        while i <= self.size:
            self.bit[i] -= cnt
            i += i & -i
        self.cnt -= cnt
        return True

    def all_dump(self):
        res = self.bit[:]
        for i in reversed(range(1, self.size)):
            if i + (i & -i) > self.size:
                continue
            res[i + (i & -i)] -= res[i]
        return [(self.array[i], cnt) for i, cnt in enumerate(res[1:]) if cnt]
