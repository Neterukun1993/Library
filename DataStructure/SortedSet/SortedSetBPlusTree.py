from bisect import bisect_left, insort


class BPlusTreeLeaf:
    def __init__(self, B_SIZE):
        self.B_SIZE = B_SIZE
        self.prev_node = None
        self.next_node = None
        self.keys = []

    def is_leaf(self):
        return True

    def split(self):
        if len(self.keys) != self.B_SIZE * 2:
            return None
        new = BPlusTreeLeaf(self.B_SIZE)
        new.keys, self.keys = self.keys[:self.B_SIZE], self.keys[self.B_SIZE:]
        if self.prev_node is not None:
            self.prev_node.next_node, new.prev_node = new, self.prev_node
        new.next_node, self.prev_node = self, new
        return new

    def key_pop(self):
        return self.keys[-1]


class BPlusTreeInnerNode:
    def __init__(self, B_SIZE):
        self.B_SIZE = B_SIZE
        self.keys = []
        self.children = []

    def is_leaf(self):
        return False

    def split(self):
        if len(self.keys) != self.B_SIZE * 2:
            return None
        new = BPlusTreeInnerNode(self.B_SIZE)
        new.keys, self.keys = self.keys[:self.B_SIZE], self.keys[self.B_SIZE:]
        new.children, self.children = (self.children[:self.B_SIZE],
                                       self.children[self.B_SIZE:])
        return new

    def key_pop(self):
        return self.keys.pop()

    def shift_lr(self, idx):
        ptrl, ptrr = self.children[idx], self.children[idx + 1]
        ptrr.keys.insert(0, ptrl.keys.pop())
        if ptrl.is_leaf():
            self.keys[idx] = ptrl.keys[-1]
        else:
            ptrr.children.insert(0, ptrl.children.pop())
            self.keys[idx], ptrr.keys[0] = ptrr.keys[0], self.keys[idx]

    def shift_rl(self, idx):
        ptrl, ptrr = self.children[idx], self.children[idx + 1]
        ptrl.keys.append(ptrr.keys.pop(0))
        if ptrl.is_leaf():
            self.keys[idx] = ptrl.keys[-1]
        else:
            ptrl.children.append(ptrr.children.pop(0))
            self.keys[idx], ptrl.keys[-1] = ptrl.keys[-1], self.keys[idx]

    def merge(self, idx):
        if self.children[idx].is_leaf():
            self.children[idx].keys += self.children[idx + 1].keys
            self.children[idx].next_node = self.children[idx + 1].next_node
            if self.children[idx + 1].next_node is not None:
                self.children[idx + 1].next_node.prev_node = self.children[idx]
        else:
            self.children[idx].keys += ([self.keys[idx]]
                                        + self.children[idx + 1].keys)
            self.children[idx].children += self.children[idx + 1].children
        del self.keys[idx], self.children[idx + 1]


class SortedSetBPlusTree:
    def __init__(self, B_SIZE=512):
        self.B_SIZE = B_SIZE
        self.root = BPlusTreeLeaf(self.B_SIZE)
        self.size = 0

    def __contains__(self, key):
        return self._search(key)

    def __len__(self):
        return self.size

    def __iter__(self):
        ptr = self.root
        while not ptr.is_leaf():
            ptr = ptr.children[0]
        while ptr is not None:
            for key in ptr.keys:
                yield key
            ptr = ptr.next_node

    def _search(self, key):
        ptr = self.root
        while not ptr.is_leaf():
            idx = bisect_left(ptr.keys, key)
            ptr = ptr.children[idx]
        idx = bisect_left(ptr.keys, key)
        return idx != len(ptr.keys) and ptr.keys[idx] == key

    def _add_rec(self, ptr, key):
        if ptr.is_leaf():
            insort(ptr.keys, key)
        else:
            idx = bisect_left(ptr.keys, key)
            p = self._add_rec(ptr.children[idx], key)
            if p is not None:
                ptr.keys.insert(idx, p.key_pop())
                ptr.children.insert(idx, p)
        return ptr.split()

    def _remove_rec(self, ptr, key):
        idx = bisect_left(ptr.keys, key)
        if ptr.is_leaf():
            if idx != len(ptr.keys) and ptr.keys[idx] == key:
                del ptr.keys[idx]
                return True
            return False
        elif self._remove_rec(ptr.children[idx], key):
            self._check_underflow(ptr, idx)
            return True
        return False

    def _check_underflow(self, ptr, idx):
        if len(ptr.children[idx].keys) >= self.B_SIZE - 1:
            pass
        elif idx == 0:
            if len(ptr.children[idx + 1].keys) > self.B_SIZE:
                ptr.shift_rl(idx)
            else:
                ptr.merge(idx)
        else:
            if len(ptr.children[idx - 1].keys) > self.B_SIZE:
                ptr.shift_lr(idx - 1)
            else:
                ptr.merge(idx - 1)

    def add(self, key):
        if key in self:
            return False
        ptrr = self.root
        ptrl = self._add_rec(self.root, key)
        if ptrl is not None:
            root = BPlusTreeInnerNode(self.B_SIZE)
            root.keys = [ptrl.key_pop()]
            root.children = [ptrl, ptrr]
            self.root = root
        self.size += 1
        return True

    def remove(self, key):
        removed = self._remove_rec(self.root, key)
        if not self.root.is_leaf() and len(self.root.children) == 1:
            self.root = self.root.children[0]
        self.size -= int(removed)
        return removed

    def iterate(self, keyl):
        ptr = self.root
        while not ptr.is_leaf():
            idx = bisect_left(ptr.keys, keyl)
            ptr = ptr.children[idx]
        for key in ptr.keys[bisect_left(ptr.keys, keyl):]:
            yield key
        ptr = ptr.next_node
        while ptr is not None:
            for key in ptr.keys:
                yield key
            ptr = ptr.next_node

    def prev_val(self, upper):
        ptr = self.root
        while not ptr.is_leaf():
            idx = bisect_left(ptr.keys, upper)
            ptr = ptr.children[idx]
        idx = bisect_left(ptr.keys, upper)
        if idx > 0:
            return ptr.keys[idx - 1]
        elif ptr.prev_node is not None:
            return ptr.prev_node.keys[-1]
        return None

    def next_val(self, lower):
        ptr = self.root
        while not ptr.is_leaf():
            idx = bisect_left(ptr.keys, lower)
            ptr = ptr.children[idx]
        idx = bisect_left(ptr.keys, lower)
        if idx < len(ptr.keys):
            return ptr.keys[idx]
        elif ptr.next_node is not None:
            return ptr.next_node.keys[0]
        return None
