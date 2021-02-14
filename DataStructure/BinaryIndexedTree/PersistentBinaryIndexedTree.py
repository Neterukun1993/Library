class PersistentBinaryIndexedTree:
    def __init__(self, n, root=None):
        self.root = root
        self.n = n
        self.size = 1 << n.bit_length()

    def build(self, array):
        n = len(array)
        bit = [[None, None, array[i - 1] if 0 <= i - 1 < n else 0] for i in range(self.size)]
        for i in range(1, self.size):
            if i + (i & -i) < self.size:
                bit[i + (i & -i)][2] += bit[i][2]
        bit[0] = tuple(bit[0])
        for k in range(self.size.bit_length() - 1):
            for i in range(1 << k, self.size, 1 << (k + 1)):
                if k == 0:
                    bit[i] = tuple(bit[i])
                else:
                    l, r = i - (1 << (k - 1)), i + (1 << (k - 1))
                    bit[i][0], bit[i][1] = bit[l], bit[r]
                    bit[i] = tuple(bit[i])
        self.root = bit[self.size >> 1]

    def _sum(self, i):
        s = 0
        nd = self.root
        idx = self.size >> 1
        for h in reversed(range(self.size.bit_length() - 2)):
            if i < idx:
                nd = nd[0]
                idx -= 1 << h
            else:
                s += nd[2]
                nd = nd[1]
                idx += 1 << h
        if i >= idx:
            s += nd[2]
        return s

    def _add_rec(self, i, idx, diff, val, nd):
        if i == idx:
            return (nd[0], nd[1], nd[2] + val)
        elif i < idx:
            ndl = self._add_rec(i, idx - diff, diff >> 1, val, nd[0])
            if idx - (idx & (-idx)) < i:
                return (ndl, nd[1], nd[2] + val)
            return (ndl, nd[1], nd[2])
        else:
            ndr = self._add_rec(i, idx + diff, diff >> 1, val, nd[1])
            return (nd[0], ndr, nd[2])

    def sum(self, l, r):
        return self._sum(r) - self._sum(l)

    def add(self, i, val):
        i += 1
        idx = self.size >> 1
        root = self._add_rec(i, idx, idx >> 1, val, self.root)
        return PersistentBinaryIndexedTree(self.n, root)
