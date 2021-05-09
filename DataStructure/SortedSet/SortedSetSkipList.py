from misc.xorshift import xorshift32


class SLSSNode:
    Nil = None

    def __init__(self, val, height):
        self.val = val
        self.next = [self.Nil] * height


class SortedSetSkipList:
    MAX_HEIGHT = 20
    LENGTH = 1 << MAX_HEIGHT
    INF = 1 << 64
    Nil = SLSSNode(INF, MAX_HEIGHT)
    SLSSNode.Nil = Nil
    Nil.next = [Nil] * MAX_HEIGHT

    def __init__(self, MAX_HEIGHT=20):
        self.sentinel_nd = SLSSNode(-self.INF, self.MAX_HEIGHT)
        self.size = 0
        self.rand32 = xorshift32()

    def __contains__(self, key):
        return self._search(key)

    def __len__(self):
        return self.size

    def __iter__(self):
        nd = self.sentinel_nd
        while nd.next[0].val != self.INF:
            yield nd.next[0].val
            nd = nd.next[0]

    def _pick_height(self):
        return self.MAX_HEIGHT - (self.rand32() & (self.LENGTH - 1)).bit_length() + 1

    def _search(self, val):
        nd = self.sentinel_nd
        for r in reversed(range(self.MAX_HEIGHT)):
            while nd.next[r].val < val:
                nd = nd.next[r]
        if nd.next[r].val == val:
            return True
        return False

    def add(self, val):
        nd = self.sentinel_nd
        stack = []

        h = self._pick_height()
        for r in reversed(range(self.MAX_HEIGHT)):
            while nd.next[r].val < val:
                nd = nd.next[r]
            if nd.next[r].val == val:
                return False
            elif r < h:
                stack.append(nd)

        nd = SLSSNode(val, h)
        for r, st_nd in enumerate(reversed(stack)):
            nd.next[r] = st_nd.next[r]
            st_nd.next[r] = nd
        self.size += 1
        return True

    def remove(self, val):
        del_nd = self.Nil
        nd = self.sentinel_nd
        for r in reversed(range(self.MAX_HEIGHT)):
            while nd.next[r].val < val:
                nd = nd.next[r]
            if nd.next[r].val == val:
                del_nd = nd.next[r]
                nd.next[r] = nd.next[r].next[r]
        if del_nd is self.Nil:
            return False
        self.size -= 1
        return True

    def iterate(self, lower):
        nd = self.sentinel_nd
        for r in reversed(range(self.MAX_HEIGHT)):
            while nd.next[r].val < lower:
                nd = nd.next[r]
        while nd.next[0].val != self.INF:
            yield nd.next[0].val
            nd = nd.next[0]

    def next_val(self, lower):
        nd = self.sentinel_nd
        for r in reversed(range(self.MAX_HEIGHT)):
            while nd.next[r].val < lower:
                nd = nd.next[r]
        return None if nd.next[r].val == self.INF else nd.next[r].val

    def prev_val(self, upper):
        nd = self.sentinel_nd
        for r in reversed(range(self.MAX_HEIGHT)):
            while nd.next[r].val < upper:
                nd = nd.next[r]
        return None if nd.val == -self.INF else nd.val
