from misc.xorshift import xorshift32


class SLNode:
    def __init__(self, val, height):
        self.val = val
        self.next = [None] * height
        self.length = [0] * height


class SkipList:
    def __init__(self, MAX_HEIGHT=20):
        self.MAX_HEIGHT = MAX_HEIGHT
        self.LENGTH = 1 << MAX_HEIGHT
        self.sentinel_nd = SLNode(-1, self.MAX_HEIGHT)
        self.size = 0
        self.rand32 = xorshift32()

    def __getitem__(self, i):
        return self._find_nd(i).next[0].val

    def __setitem__(self, i, val):
        _find_nd(i).next[0] = val

    def _find_nd(self, i):
        nd = self.sentinel_nd
        idx = -1
        for r in reversed(range(self.MAX_HEIGHT)):
            while nd.next[r] is not None and idx + nd.length[r] < i:
                idx += nd.length[r]
                nd = nd.next[r]
        return nd

    def _pick_height(self):
        return self.MAX_HEIGHT - (self.rand32() & (self.LENGTH - 1)).bit_length() + 1

    def insert(self, i, val):
        if i > self.size:
            raise IndexError
        nd = self.sentinel_nd
        h = self._pick_height()
        new_nd = SLNode(val, h)
        idx = -1
        for r in reversed(range(self.MAX_HEIGHT)):
            while nd.next[r] is not None and idx + nd.length[r] < i:
                idx += nd.length[r]
                nd = nd.next[r]
            nd.length[r] += 1
            if r < h:
                new_nd.next[r] = nd.next[r]
                nd.next[r] = new_nd
                new_nd.length[r] = nd.length[r] - (i - idx)
                nd.length[r] = i - idx
        self.size += 1

    def delete(self, i):
        if i >= self.size:
            raise IndexError
        nd = self.sentinel_nd
        idx = -1
        for r in reversed(range(self.MAX_HEIGHT)):
            while nd.next[r] is not None and idx + nd.length[r] < i:
                idx += nd.length[r]
                nd = nd.next[r]
            nd.length[r] -= 1
            if idx + nd.length[r] + 1 == i and nd.next[r] is not None:
                val = nd.next[r].val
                nd.length[r] += nd.next[r].length[r]
                deleted = nd.next[r]
                nd.next[r] = nd.next[r].next[r]
        del deleted
        self.size -= 1

    def dump(self):
        res = []
        nd = self.sentinel_nd.next[0]
        while nd is not None:
            res.append(nd.val)
            nd = nd.next[0]
        return res
