from misc.xorshift import xorshift32


class SortedSetTreap:
    def __init__(self):
        self.root = -1
        self.pow_sz = 1
        self.rand32 = xorshift32()
        self.stack = array("i", [0])
        self.l = array("i", [-1])
        self.r = array("i", [-1])
        self.p = array("i", [-1])
        self.pris = array("I", [self.rand32()])
        self.keys = [0]

    def __contains__(self, key):
        return self._search(key)

    def __iter__(self):
        def dfs(nd):
            if self.l[nd] != -1:
                yield from dfs(self.l[nd])
            yield self.keys[nd]
            if self.r[nd] != -1:
                yield from dfs(self.r[nd])
        if self.root != -1:
            yield from dfs(self.root)

    def _new_node(self, key):
        if self.stack:
            nd = self.stack.pop()
            self.keys[nd] = key
            return nd
        else:
            self.stack = array("i", [nd for nd in range(self.pow_sz, self.pow_sz << 1)])
            self.l += array("i", [-1] * self.pow_sz)
            self.r += array("i", [-1] * self.pow_sz)
            self.p += array("i", [-1] * self.pow_sz)
            self.pris += array("I", [self.rand32() for _ in range(self.pow_sz)])
            self.keys += [0] * self.pow_sz
            self.pow_sz <<= 1
            return self._new_node(key)

    def _search(self, key):
        nd = self.root
        while nd != -1:
            if key < self.keys[nd]: nd = self.l[nd]
            elif key > self.keys[nd]: nd = self.r[nd]
            else: return True
        return False

    def add(self, key):
        if self.root == -1:
            self.root = self._new_node(key)
            return True

        nd = self.root
        while True:
            if key < self.keys[nd]:
                if self.l[nd] == -1:
                    self.l[nd] = self._new_node(key)
                    self.p[self.l[nd]] = nd
                    nd = self.l[nd]
                    break
                nd = self.l[nd]
            elif key > self.keys[nd]:
                if self.r[nd] == -1:
                    self.r[nd] = self._new_node(key)
                    self.p[self.r[nd]] = nd
                    nd = self.r[nd]
                    break
                nd = self.r[nd]
            else:
                return False

        while self.p[nd] != -1 and self.pris[self.p[nd]] > self.pris[nd]:
            if self.r[self.p[nd]] == nd: self._rotl(self.p[nd])
            else: self._rotr(self.p[nd])
        return True

    def _rotl(self, nd):
        pv = self.r[nd]
        self.p[pv] = self.p[nd]
        if self.p[pv] != -1:
            if self.l[self.p[pv]] == nd: self.l[self.p[pv]] = pv
            else: self.r[self.p[pv]] = pv
        self.r[nd] = self.l[pv]
        if self.r[nd] != -1: self.p[self.r[nd]] = nd
        self.p[nd] = pv
        self.l[pv] = nd
        if nd == self.root: self.root = pv

    def _rotr(self, nd):
        pv = self.l[nd]
        self.p[pv] = self.p[nd]
        if self.p[pv] != -1:
            if self.r[self.p[pv]] == nd: self.r[self.p[pv]] = pv
            else: self.l[self.p[pv]] = pv
        self.l[nd] = self.r[pv]
        if self.l[nd] != -1: self.p[self.l[nd]] = nd
        self.p[nd] = pv
        self.r[pv] = nd
        if nd == self.root: self.root = pv

    def remove(self, key):
        if self.root == -1: return False

        nd = self.root
        while True:
            if nd == -1: return False
            elif key < self.keys[nd]: nd = self.l[nd]
            elif key > self.keys[nd]: nd = self.r[nd]
            else: break

        while self.l[nd] != -1 or self.r[nd] != -1:
            if self.l[nd] == -1: self._rotl(nd)
            elif self.r[nd] == -1: self._rotr(nd)
            elif self.pris[self.l[nd]] < self.pris[self.r[nd]]: self._rotr(nd)
            else: self._rotl(nd)

        if nd == self.root: self.root = -1
        elif self.l[self.p[nd]] == nd: self.l[self.p[nd]] = -1
        else: self.r[self.p[nd]] = -1
        self.stack.append(nd)
        return True

    def iterate(self, lower):
        def dfs(nd):
            if self.l[nd] != -1 and (self.keys[nd] > lower):
                yield from dfs(self.l[nd])
            if self.keys[nd] >= lower:
                yield self.keys[nd]
            if self.r[nd] != -1:
                yield from dfs(self.r[nd])
        if self.root != -1:
            yield from dfs(self.root)

    def next_val(self, lower):
        ret = None
        nd = self.root
        while nd != -1:
            if self.keys[nd] >= lower:
                ret = self.keys[nd]
                nd = self.l[nd]
            else: nd = self.r[nd]
        return ret

    def prev_val(self, upper):
        ret = None
        nd = self.root
        while nd != -1:
            if self.keys[nd] < upper:
                ret = self.keys[nd]
                nd = self.r[nd]
            else: nd = self.l[nd]
        return ret
