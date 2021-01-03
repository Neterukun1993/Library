class SlidingWindowAggregation:
    def __init__(self, op):
        self.op = op
        self.inque = []
        self.outque = []

    def __len__(self):
        return len(self.outque) + len(self.inque)

    def _trans(self):
        val, _ = self.inque.pop()
        self.outque.append((val, val))
        acc = val
        while self.inque:
            val, _ = self.inque.pop()
            acc = self.op(val, acc)
            self.outque.append((val, acc))

    def all_fold(self):
        if not self.inque:
            return self.outque[-1][1]
        if not self.outque:
            return self.inque[-1][1]
        return self.op(self.outque[-1][1], self.inque[-1][1])

    def append(self, val):
        if self.inque:
            self.inque.append((val, self.op(self.inque[-1][1], val)))
        else:
            self.inque.append((val, val))

    def popleft(self):
        if not self.outque:
            self._trans()
        val = self.outque.pop()
        return val[0]
