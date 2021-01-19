from misc.xorshift import xorshift32


rand32 = xorshift32()


class RMHNode:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.val = val


class RandomizedMeldableHeap:
    def __init__(self):
        self.root = None

    def _meld(self, a, b):
        if a is None: return b
        if b is None: return a
        if b.val < a.val: a, b = b, a
        if rand32() & 1:
            a.l = self._meld(a.l, b)
        else:
            a.r = self._meld(a.r, b)
        return a

    @ property
    def min(self):
        return self.root.val

    def push(self, val):
        nd = RMHNode(val)
        self.root = self._meld(self.root, nd)

    def pop(self):
        rt = self.root
        self.root = self._meld(rt.l, rt.r)
        return rt.val

    def meld(self, other):
        self.root = self._meld(self.root, other.root)

    def empty(self):
        return self.root is None
