class AVLNode:
    def __init__(self, key):
        self.key = key
        self.h = 1
        self.l, self.r, self.p = None, None, None

    def rotl(self):
        nd = self.r
        nd.p = self.p
        if nd.p is not None:
            if nd.p.l is self: nd.p.l = nd
            else: nd.p.r = nd
        self.r = nd.l
        if self.r is not None: self.r.p = self
        self.p = nd
        nd.l = self
        self.h = self.get_h()
        nd.h = nd.get_h()
        return nd

    def rotr(self):
        nd = self.l
        nd.p = self.p
        if nd.p is not None:
            if nd.p.r is self: nd.p.r = nd
            else: nd.p.l = nd
        self.l = nd.r
        if self.l is not None: self.l.p = self
        self.p = nd
        nd.r = self
        self.h = self.get_h()
        nd.h = nd.get_h()
        return nd

    def get_h(self):
        lh = self.l.h if self.l is not None else 0
        rh = self.r.h if self.r is not None else 0
        return max(lh, rh) + 1

    def get_bf(self):
        lh = self.l.h if self.l is not None else 0
        rh = self.r.h if self.r is not None else 0
        return lh - rh


class SortedSetAVLTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __contains__(self, key):
        return self._search(key)

    def __len__(self):
        return self.size

    def __iter__(self):
        def dfs(nd):
            if nd.l is not None:
                yield from dfs(nd.l)
            yield nd.key
            if nd.r is not None:
                yield from dfs(nd.r)
        if self.root is not None:
            yield from dfs(self.root)

    def _search(self, key):
        nd = self.root
        while nd is not None:
            if nd.key < key: nd = nd.r
            elif nd.key > key: nd = nd.l
            else: return True
        return False

    def _balance_add(self, nd):
        chi_bf = 0
        while True:
            nd.h, bf = nd.get_h(), nd.get_bf()
            if bf > 1:
                if chi_bf < 0: nd.l = nd.l.rotl()
                pv = nd.rotr()
                if pv.p is None: self.root = pv
                return
            elif bf < -1:
                if chi_bf > 0: nd.r = nd.r.rotr()
                pv = nd.rotl()
                if pv.p is None: self.root = pv
                return
            elif bf == 0 or nd.p is None: return
            nd = nd.p
            chi_bf = bf

    def _balance_rem(self, nd):
        while True:
            pv = None
            nd.h, bf = nd.get_h(), nd.get_bf()
            if bf > 1:
                if nd.l.get_bf() < 0: nd.l = nd.l.rotl()
                pv = nd.rotr()
            elif bf < -1:
                if nd.r.get_bf() > 0: nd.r = nd.r.rotr()
                pv = nd.rotl()
            elif bf != 0: return

            if pv is not None:
                if pv.p is None:
                    self.root = pv
                    return
                if pv.get_bf() != 0: return
            else: pv = nd
            if pv.p is None: return
            else: nd = pv.p

    def add(self, key):
        if self.root is None:
            self.root = AVLNode(key)
            self.size += 1
            return True

        nd = self.root
        while nd is not None:
            if nd.key < key:
                if nd.r is None:
                    nd.r = AVLNode(key)
                    nd.r.p = nd
                    break
                nd = nd.r
            elif nd.key > key:
                if nd.l is None:
                    nd.l = AVLNode(key)
                    nd.l.p = nd
                    break
                nd = nd.l
            else: return False
        self.size += 1
        self._balance_add(nd)
        return True

    def remove(self, key):
        if self.root is None:
            return False

        nd = self.root
        while nd is not None:
            if nd.key < key: nd = nd.r
            elif nd.key > key: nd = nd.l
            else: break
        else: return False

        self.size -= 1
        if nd.l is not None and nd.r is not None:
            max_nd = nd.l
            while max_nd.r is not None:
                max_nd = max_nd.r
            nd.key = max_nd.key
            nd = max_nd

        chi_nd = nd.r if nd.r is not None else nd.l
        if nd is self.root:
            self.root = chi_nd
            if self.root is not None: self.root.p = None
            return True
        elif nd.p.r is nd:
            nd.p.r = chi_nd
            if chi_nd is not None: chi_nd.p = nd.p
        else:
            nd.p.l = chi_nd
            if chi_nd is not None: chi_nd.p = nd.p
        self._balance_rem(nd.p)
        return True

    def iterate(self, lower):
        def dfs(nd):
            if nd.l is not None and (nd.key > lower):
                yield from dfs(nd.l)
            if nd.key >= lower:
                yield nd.key
            if nd.r is not None:
                yield from dfs(nd.r)
        if self.root is not None:
            yield from dfs(self.root)

    def next_val(self, lower):
        nd = self.root
        ret = None
        while nd is not None:
            if nd.key >= lower:
                ret = nd.key
                nd = nd.l
            else: nd = nd.r
        return ret

    def prev_val(self, upper):
        nd = self.root
        ret = None
        while nd is not None:
            if nd.key < upper:
                ret = nd.key
                nd = nd.r
            else: nd = nd.l
        return ret
