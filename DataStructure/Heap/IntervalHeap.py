class IntervalHeap:
    def __init__(self):
        self.hp = []

    @property
    def min(self):
        return self.hp[0]

    @property
    def max(self):
        if len(self) == 1:
            return self.hp[0]
        return self.hp[1]

    def __len__(self):
        return len(self.hp)

    def push(self, val):
        self.hp.append(val)
        k = len(self) - 1
        self._heap_up(k)

    def pop_min(self):
        if len(self) == 0:
            raise IndexError('pop from empty list')
        if len(self) < 2:
            return self.hp.pop()
        self.hp[0], self.hp[-1] = self.hp[-1], self.hp[0]
        res = self.hp.pop()
        k = self._heap_down(0)
        self._heap_up(k)
        return res

    def pop_max(self):
        if len(self) == 0:
            raise IndexError('pop from empty list')
        if len(self) < 3:
            return self.hp.pop()
        self.hp[1], self.hp[-1] = self.hp[-1], self.hp[1]
        res = self.hp.pop()
        k = self._heap_down(1)
        self._heap_up(k)
        return res

    def _heap_down(self, k):
        if k & 1:
            while 2 * k + 1 < len(self):
                chi_k = 2 * k + 3
                if len(self) <= chi_k or self.hp[chi_k - 2] > self.hp[chi_k]:
                    chi_k -= 2
                if chi_k < len(self) and self.hp[k] < self.hp[chi_k]:
                    self.hp[k], self.hp[chi_k] = self.hp[chi_k], self.hp[k]
                    k = chi_k
                else:
                    break
        else:
            while 2 * k + 2 < len(self):
                chi_k = 2 * k + 4
                if len(self) <= chi_k or self.hp[chi_k - 2] < self.hp[chi_k]:
                    chi_k -= 2
                if chi_k < len(self) and self.hp[k] > self.hp[chi_k]:
                    self.hp[k], self.hp[chi_k] = self.hp[chi_k], self.hp[k]
                    k = chi_k
                else:
                    break
        return k

    def _heap_up(self, k):
        if k | 1 < len(self) and self.hp[k & ~1] > self.hp[k | 1]:
            self.hp[k & ~1], self.hp[k | 1] = self.hp[k | 1], self.hp[k & ~1]
            k ^= 1
        while k != 0:
            par_k = ((k >> 1) - 1) & ~1
            if self.hp[par_k] <= self.hp[k]:
                break
            self.hp[par_k], self.hp[k] = self.hp[k], self.hp[par_k]
            k = par_k
        while k != 1:
            par_k = (((k >> 1) - 1) & ~1) | 1
            if self.hp[par_k] >= self.hp[k]:
                break
            self.hp[par_k], self.hp[k] = self.hp[k], self.hp[par_k]
            k = par_k
        return k
