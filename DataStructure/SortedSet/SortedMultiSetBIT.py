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
