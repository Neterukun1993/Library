import math


class ScapegoatNode:
    def __init__(self, key):
        self.key = key
        self.sz = 1
        self.l, self.r, self.p = None, None, None

    def update(self):
        self.sz = 1
        if self.l is not None: self.sz += self.l.sz
        if self.r is not None: self.sz += self.r.sz


class SortedSetScapegoatTree:
    def __init__(self):
        self.root = None
        self.size = 0
        self.q = 0

    def __contains__(self, key):
        return self._search(key)

    def __len__(self):
        return self.size

    def __iter__(self):
        def dfs(nd):
            if nd.l is not None: yield from dfs(nd.l)
            yield nd.key
            if nd.r is not None: yield from dfs(nd.r)

        if self.root is not None:
            yield from dfs(self.root)

    def _log32q(self):
        return math.log(self.q, 1.5)

    def _pack_into_array(self, subroot):
        def dfs(nd):
            if nd.l is not None: dfs(nd.l)
            res.append(nd)
            if nd.r is not None: dfs(nd.r)

        res = []
        dfs(subroot)
        return res

    def _rebuild(self, subroot):
        def rec_build(l, r):
            if l == r: return None
            mid = (l + r) // 2
            ndl = rec_build(l, mid)
            ndr = rec_build(mid + 1, r)
            array[mid].l = ndl
            array[mid].r = ndr
            if ndl is not None: ndl.p = array[mid]
            if ndr is not None: ndr.p = array[mid]
            array[mid].update()
            return array[mid]

        array = self._pack_into_array(subroot)
        p = subroot.p

        if p is None:
            self.root = rec_build(0, len(array))
            self.root.p = None
        elif p.r == subroot:
            p.r = rec_build(0, len(array))
            p.r.p = p
        else:
            p.l = rec_build(0, len(array))
            p.l.p = p

    def _search(self, key):
        nd = self.root
        while nd is not None:
            if nd.key < key: nd = nd.r
            elif nd.key > key: nd = nd.l
            else: return True
        return False

    def add(self, key):
        if self.root is None:
            self.root = ScapegoatNode(key)
            self.size += 1
            self.q += 1
            return True

        nd = self.root
        depth = 0
        while nd is not None:
            depth += 1
            if nd.key < key:
                if nd.r is None:
                    nd.r = ScapegoatNode(key)
                    nd.r.p = nd
                    break
                nd = nd.r
            elif nd.key > key:
                if nd.l is None:
                    nd.l = ScapegoatNode(key)
                    nd.l.p = nd
                    break
                nd = nd.l
            else: return False

        self.size += 1
        self.q += 1
        if depth > self._log32q():
            while 3 * nd.sz <= 2 * nd.p.sz:
                nd = nd.p
            self._rebuild(nd.p)
        return True

    def remove(self, key):
        if self.root is None: return False

        nd = self.root
        while nd is not None:
            if nd.key < key: nd = nd.r
            elif nd.key > key: nd = nd.l
            else: break
        else: return False

        self.size -= 1
        if nd.l is not None and nd.r is not None:
            min_nd = nd.r
            while min_nd.l is not None:
                min_nd = min_nd.l
            nd.key = min_nd.key
            nd = min_nd

        chi_nd = nd.r if nd.r is not None else nd.l
        if nd is self.root:
            self.root = chi_nd
            if self.root is not None: self.root.p = None
        elif nd.p.r is nd:
            nd.p.r = chi_nd
            if chi_nd is not None: chi_nd.p = nd.p
        else:
            nd.p.l = chi_nd
            if chi_nd is not None: chi_nd.p = nd.p

        if 2 * self.size < self.q:
            if self.root is not None:
                self._rebuild(self.root)
            self.q = self.size
        return True

    def iterate(self, lower):
        def dfs(nd):
            if nd.l is not None and (nd.key > lower): yield from dfs(nd.l)
            if nd.key >= lower: yield nd.key
            if nd.r is not None: yield from dfs(nd.r)

        if self.root is not None:
            yield from dfs(self.root)
