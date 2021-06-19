class LazyBinaryTrieNode:
    def __init__(self):
        self.bit0 = None
        self.bit1 = None
        self.lazy_val = 0
        self.size = 0


class LazyBinaryTrie:
    def __init__(self, MAX_BIT_LENGTH=32):
        self.MAX_BIT_LENGTH = MAX_BIT_LENGTH
        self.root = LazyBinaryTrieNode()

    def __len__(self):
        return self.root.size

    def __contains__(self, val):
        return self._search(val)

    def _propagate(self, ptr, i):
        lazy_val = ptr.lazy_val
        if (lazy_val >> i) & 1: ptr.bit0, ptr.bit1 = ptr.bit1, ptr.bit0
        if ptr.bit0 is not None: ptr.bit0.lazy_val ^= lazy_val
        if ptr.bit1 is not None: ptr.bit1.lazy_val ^= lazy_val
        ptr.lazy_val = 0

    def _search(self, val):
        ptr = self.root
        for i in reversed(range(self.MAX_BIT_LENGTH)):
            self._propagate(ptr, i)
            if (val >> i) & 1: ptr = ptr.bit1
            else: ptr = ptr.bit0
            if ptr is None: return False
        return True

    def add(self, val):
        if self._search(val): return False
        ptr = self.root
        ptr.size += 1
        for i in reversed(range(self.MAX_BIT_LENGTH)):
            if (val >> i) & 1:
                if ptr.bit1 is None: ptr.bit1 = LazyBinaryTrieNode()
                ptr = ptr.bit1
            else:
                if ptr.bit0 is None: ptr.bit0 = LazyBinaryTrieNode()
                ptr = ptr.bit0
            ptr.size += 1
        return True

    def remove(self, val):
        if not self._search(val): return False
        ptr = self.root
        ptr.size -= 1
        for i in reversed(range(self.MAX_BIT_LENGTH)):
            if (val >> i) & 1:
                if ptr.bit1.size == 1:
                    ptr.bit1 = None
                    return True
                ptr = ptr.bit1
            else:
                if ptr.bit0.size == 1:
                    ptr.bit0 = None
                    return True
                ptr = ptr.bit0
            ptr.size -= 1
        return True

    def kth_smallest(self, k):
        ptr = self.root
        res = 0
        for i in reversed(range(self.MAX_BIT_LENGTH)):
            self._propagate(ptr, i)
            szl = ptr.bit0.size if ptr.bit0 is not None else 0
            if k < szl:
                ptr = ptr.bit0
            else:
                res |= 1 << i
                k -= szl
                ptr = ptr.bit1
        return res

    def kth_largest(self, k):
        return self.kth_smallest(self.root.size - k - 1)

    def bisect_left(self, lower):
        ptr = self.root
        idx = 0
        for i in reversed(range(self.MAX_BIT_LENGTH)):
            if ptr is None: return idx
            self._propagate(ptr, i)
            if (lower >> i) & 1 == 1:
                idx += ptr.bit0.size if ptr.bit0 is not None else 0
                ptr = ptr.bit1
            else:
                ptr = ptr.bit0
        return idx

    def bisect_right(self, upper):
        return self.bisect_left(upper + 1)

    def get_xor_min(self, val):
        ptr = self.root
        res = 0
        for i in reversed(range(self.MAX_BIT_LENGTH)):
            self._propagate(ptr, i)
            if (val >> i) & 1:
                if ptr.bit1 is not None: ptr = ptr.bit1
                else:
                    ptr = ptr.bit0
                    res |= 1 << i
            else:
                if ptr.bit0 is not None: ptr = ptr.bit0
                else:
                    ptr = ptr.bit1
                    res |= 1 << i
        return res

    def all_xor(self, val):
        self.root.lazy_val ^= val
