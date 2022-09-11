class FoldableDeque:
    def __init__(self, op):
        self.op = op
        self.front = []
        self.back = []

    def __len__(self):
        return len(self.front) + len(self.back)

    def _trans(self):
        half = len(self) // 2
        if len(self.front) == 0:
            stack = []
            while self:
                stack.append(self.back.pop()[0])
            for i in range(half, len(stack)):
                self.append(stack[i])
            for i in reversed(range(0, half)):
                self.appendleft(stack[i])
        else:
            stack = []
            while self:
                stack.append(self.front.pop()[0])
            for i in range(half, len(stack)):
                self.appendleft(stack[i])
            for i in reversed(range(0, half)):
                self.append(stack[i])

    def fold_all(self):
        if not self.front:
            return self.back[-1][1]
        if not self.back:
            return self.front[-1][1]
        return self.op(self.back[-1][1], self.front[-1][1])

    def append(self, val):
        if self.front:
            self.front.append((val, self.op(self.front[-1][1], val)))
        else:
            self.front.append((val, val))

    def appendleft(self, val):
        if self.back:
            self.back.append((val, self.op(val, self.back[-1][1])))
        else:
            self.back.append((val, val))

    def pop(self):
        if not self.front:
            self._trans()
        val = self.front.pop()
        return val[0]

    def popleft(self):
        if not self.back:
            self._trans()
        val = self.back.pop()
        return val[0]
