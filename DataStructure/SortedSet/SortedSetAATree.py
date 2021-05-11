class AANode:
    Nil = None

    def __init__(self, key):
        self.key = key
        self.lv = 1
        self.l, self.r, self.p = self.Nil, self.Nil, self.Nil

    def skew(self):
        if self.l.lv == self.lv:
            pv = self._rotr()
            return pv
        return self

    def split(self):
        if self.r.r.lv == self.lv:
            pv = self._rotl()
            pv.lv += 1
            return pv
        return self

    def skew_split(self):
        pv = self
        if pv.l.lv == pv.lv:
            pv = pv._rotr()
        if pv.r.r.lv == pv.lv:
            pv = pv._rotl()
            pv.lv += 1
        return pv

    def _rotl(self):
        pv = self.r
        pv.p = self.p
        if pv.p is not self.Nil:
            if pv.p.l is self: pv.p.l = pv
            else: pv.p.r = pv
        self.r = pv.l
        if self.r is not self.Nil: self.r.p = self
        self.p = pv
        pv.l = self
        return pv

    def _rotr(self):
        pv = self.l
        pv.p = self.p
        if pv.p is not self.Nil:
            if pv.p.r is self: pv.p.r = pv
            else: pv.p.l = pv
        self.l = pv.r
        if self.l is not self.Nil: self.l.p = self
        self.p = pv
        pv.r = self
        return pv


class SortedSetAATree:
    Nil = AANode(-1)
    AANode.Nil = Nil
    Nil.lv = 0
    Nil.l, Nil.r, Nil.p = Nil, Nil, Nil

    def __init__(self):
        self.root = self.Nil
        self.size = 0

    def __contains__(self, key):
        return self._search(key)

    def __len__(self):
        return self.size

    def __iter__(self):
        def dfs(nd):
            if nd.l is not self.Nil:
                yield from dfs(nd.l)
            yield nd.key
            if nd.r is not self.Nil:
                yield from dfs(nd.r)
        if self.root is not self.Nil:
            yield from dfs(self.root)

    def _search(self, key):
        nd = self.root
        while nd is not self.Nil:
            if nd.key < key: nd = nd.r
            elif nd.key > key: nd = nd.l
            else: return True
        return False

    def _balance_del(self, nd):
        while nd is not self.Nil:
            if nd.l.lv < nd.lv - 1 or nd.r.lv < nd.lv - 1:
                nd.lv -= 1
                if nd.r.lv > nd.lv:
                    nd.r.lv = nd.lv
                nd = nd.skew()
                nd.r = nd.r.skew()
                nd.r.r = nd.r.r.skew()
                nd = nd.split()
                nd.r = nd.r.split()
            self.root = nd
            nd = nd.p

    def add(self, key):
        if self.root is self.Nil:
            self.root = AANode(key)
            self.size += 1
            return True

        nd = self.root
        while nd is not self.Nil:
            if nd.key < key:
                if nd.r is self.Nil:
                    nd.r = AANode(key)
                    self.size += 1
                    nd.r.p = nd
                    if nd.lv + 1 == nd.p.lv:
                        return True
                    break
                nd = nd.r
            elif nd.key > key:
                if nd.l is self.Nil:
                    nd.l = AANode(key)
                    self.size += 1
                    nd.l.p = nd
                    break
                nd = nd.l
            else: return False

        while nd is not self.Nil:
            nd = nd.skew_split()
            self.root = nd
            nd = nd.p
        return True

    def remove(self, key):
        if self.root is self.Nil: return False

        nd = self.root
        while nd is not self.Nil:
            if nd.key < key: nd = nd.r
            elif nd.key > key: nd = nd.l
            else: break
        else: return False

        self.size -= 1
        if nd.l is not self.Nil and nd.r is not self.Nil:
            min_nd = nd.r
            while min_nd.l is not self.Nil:
                min_nd = min_nd.l
            nd.key = min_nd.key
            nd = min_nd

        chi_nd = nd.r if nd.r is not self.Nil else nd.l
        if nd is self.root:
            self.root = chi_nd
            if self.root is not self.Nil: self.root.p = self.Nil
            return True
        elif nd.p.r is nd:
            nd.p.r = chi_nd
            if chi_nd is not self.Nil: chi_nd.p = nd.p
        else:
            nd.p.l = chi_nd
            if chi_nd is not self.Nil: chi_nd.p = nd.p
        self._balance_del(nd.p)
        return True

    def iterate(self, lower):
        def dfs(nd):
            if nd.l is not self.Nil and (nd.key > lower):
                yield from dfs(nd.l)
            if nd.key >= lower:
                yield nd.key
            if nd.r is not self.Nil:
                yield from dfs(nd.r)
        if self.root is not self.Nil:
            yield from dfs(self.root)

    def next_key(self, lower):
        nd = self.root
        ret = None
        while nd is not self.Nil:
            if nd.key >= lower:
                ret = nd.key
                nd = nd.l
            else: nd = nd.r
        return ret

    def prev_key(self, upper):
        nd = self.root
        ret = None
        while nd is not self.Nil:
            if nd.key < upper:
                ret = nd.key
                nd = nd.r
            else: nd = nd.l
        return ret
