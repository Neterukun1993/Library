class SHNode:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.val = val
        self.add = 0

    def lazy_propagate(self):
        if self.l is not None: self.l.add += self.add
        if self.r is not None: self.r.add += self.add
        self.val += self.add
        self.add = 0


class SkewHeap:
    def __init__(self):
        self.root = None

    def _meld(self, a, b):
        if a is None: return b
        if b is None: return a
        if b.val + b.add < a.val + a.add: a, b = b, a
        a.lazy_propagate()
        a.r = self._meld(a.r, b)
        a.l, a.r = a.r, a.l
        return a

    @ property
    def min(self):
        self.root.lazy_propagate()
        return self.root.val

    def push(self, val):
        nd = SHNode(val)
        self.root = self._meld(self.root, nd)

    def pop(self):
        rt = self.root
        rt.lazy_propagate()
        self.root = self._meld(rt.l, rt.r)
        return rt.val

    def meld(self, other):
        self.root = self._meld(self.root, other.root)

    def add(self, val):
        self.root.add += val

    def empty(self):
        return self.root is None
