from bisect import bisect_left, bisect_right, insort
from DataStructure.SortedSet.SortedSetBTree import BTreeNode, SortedSetBTree


class SortedMultiSetBTree(SortedSetBTree):
    def __init__(self, B_SIZE=512):
        super().__init__(B_SIZE)

    def add(self, key):
        ptr = self.root
        p = self._add_rec(ptr, key)
        if p is not None:
            root = BTreeNode(self.B_SIZE)
            root.keys = [p.keys.pop()]
            root.children = [p, self.root]
            self.root = root
        self.size += 1
        return True
