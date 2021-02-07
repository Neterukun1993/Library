from bisect import bisect_left, bisect_right, insort


class BTreeNode:
    def __init__(self, B_SIZE):
        self.B_SIZE = B_SIZE
        self.keys = []
        self.children = []

    def split(self):
        if len(self.keys) != self.B_SIZE * 2:
            return None
        ptr = BTreeNode(self.B_SIZE)
        ptr.keys, self.keys = self.keys[:self.B_SIZE], self.keys[self.B_SIZE:]
        ptr.children, self.children = self.children[:self.B_SIZE], self.children[self.B_SIZE:]
        return ptr

    def shift_lr(self, idx):
        ptrl, ptrr = self.children[idx], self.children[idx + 1]
        ptrr.keys.insert(0, ptrl.keys[-1])
        del ptrl.keys[-1]
        if ptrl.children:
            ptrr.children.insert(0, ptrl.children[-1])
            del ptrl.children[-1]
        self.keys[idx], ptrr.keys[0] = ptrr.keys[0], self.keys[idx]

    def shift_rl(self, idx):
        ptrl, ptrr = self.children[idx], self.children[idx + 1]
        ptrl.keys.append(ptrr.keys[0])
        del ptrr.keys[0]
        if ptrr.children:
            ptrl.children.append(ptrr.children[0])
            del ptrr.children[0]
        self.keys[idx], ptrl.keys[-1] = ptrl.keys[-1], self.keys[idx]

    def merge(self, idx):
        self.children[idx].keys += [self.keys[idx]] + self.children[idx + 1].keys
        self.children[idx].children += self.children[idx + 1].children
        del self.keys[idx], self.children[idx + 1]
        assert(len(self.keys) + 1 == len(self.children))


class SortedSetBTree:
    def __init__(self, B_SIZE=512):
        self.B_SIZE = B_SIZE
        self.root = BTreeNode(self.B_SIZE)
        self.size = 0

    def __contains__(self, key):
        return self._search(key)

    def __len__(self):
        return self.size

    def __iter__(self):
        return self._generate_rec(self.root)

    def _search(self, key):
        ptr = self.root
        while True:
            idx = bisect_left(ptr.keys, key)
            if idx != len(ptr.keys) and ptr.keys[idx] == key:
                return True
            if not ptr.children:
                return False
            ptr = ptr.children[idx]

    def _generate_rec(self, ptr):
        for idx, chi in enumerate(ptr.children):
            yield from self._generate_rec(chi)
            if idx < len(ptr.keys):
                yield ptr.keys[idx]
        if not ptr.children:
            for key in ptr.keys:
                yield key

    def _generate_rec_vl(self, ptr, vl, f):
        idxl = 0 if f else bisect_left(ptr.keys, vl)
        for idx, chi in enumerate(ptr.children[idxl:], idxl):
            if idx == idxl:
                yield from self._generate_rec_vl(chi, vl, f | False)
            else:
                yield from self._generate_rec_vl(chi, vl, True)
            if idx < len(ptr.keys):
                yield ptr.keys[idx]
        if not ptr.children:
            for key in ptr.keys[idxl:]:
                yield key

    def _add_rec(self, ptr, key):
        if not ptr.children:
            insort(ptr.keys, key)
        else:
            i = bisect_right(ptr.keys, key)
            p = self._add_rec(ptr.children[i], key)
            if p is not None:
                ptr.keys.insert(i, p.keys.pop())
                ptr.children.insert(i, p)
        return ptr.split()

    def _remove_rec(self, ptr, key):
        idx = bisect_left(ptr.keys, key)
        if idx != len(ptr.keys) and ptr.keys[idx] == key:
            if not ptr.children:
                del ptr.keys[idx]
            else:
                ptr.keys[idx] = self._remove_smallest(ptr.children[idx + 1])
                self._check_underflow(ptr, idx + 1)
            return True
        elif ptr.children and self._remove_rec(ptr.children[idx], key):
            self._check_underflow(ptr, idx)
            return True
        return False

    def _remove_smallest(self, ptr):
        if not ptr.children:
            res = ptr.keys[0]
            del ptr.keys[0]
            return res
        res = self._remove_smallest(ptr.children[0])
        self._check_underflow(ptr, 0)
        return res

    def _check_underflow(self, ptr, idx):
        if len(ptr.children[idx].keys) >= self.B_SIZE - 1:
            return
        elif idx == 0:
            if len(ptr.children[idx + 1].keys) > self.B_SIZE: ptr.shift_rl(idx)
            else: ptr.merge(idx)
        else:
            if len(ptr.children[idx - 1].keys) > self.B_SIZE: ptr.shift_lr(idx - 1)
            else: ptr.merge(idx - 1)

    def add(self, key):
        if key in self:
            return True
        ptr = self.root
        p = self._add_rec(ptr, key)
        if p is not None:
            root = BTreeNode(self.B_SIZE)
            root.keys = [p.keys.pop()]
            root.children = [p, self.root]
            self.root = root
        self.size += 1
        return True

    def remove(self, key):
        flag = self._remove_rec(self.root, key)
        if len(self.root.children) == 1:
            self.root = self.root.children[0]
        if flag: self.size -= 1
        return flag

    def iterate(self, vl):
        return self._generate_rec_vl(self.root, vl, False)
