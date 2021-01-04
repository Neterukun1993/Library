class SHNode:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.val = val


class SkewHeap:
    def __init__(self):
        self.root = None

    def _meld(self, a, b):
        if a is None:
            return b
        elif b is None:
            return a
        if b.val < a.val:
            a, b = b, a
        a.r = self._meld(a.r, b)
        a.l, a.r = a.r, a.l
        return a

    def push(self, val):
        nd = SHNode(val)
        self.root = self._meld(self.root, nd)

    def pop(self):
        rt = self.root
        self.root = self._meld(rt.l, rt.r)
        return rt.val

    def meld(self, other):
        sh = SkewHeap()
        sh.root = self._meld(self.root, other.root)
        return sh

    def empty(self):
        return self.root is None
