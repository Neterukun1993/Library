class PHNode:
    def __init__(self, val):
        self.val = val
        self.chi = []


class ParingHeap:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root is None

    def top(self):
        return self.root.val

    def push(self, val):
        self.root = self.merge(self.root, PHNode(val))

    def pop(self):
        val = self.root.val
        self.root = self.merge_pairs(self.root.chi)
        return val

    def merge(self, nd1, nd2):
        if nd1 is None:
            return nd2
        elif nd2 is None:
            return nd1
        if nd1.val > nd2.val:
            nd1, nd2 = nd2, nd1
        nd1.chi.append(nd2)
        return nd1

    def merge_pairs(self, ndlist):
        newlist = []
        for i in range(len(ndlist) // 2):
            newlist.append(self.merge(ndlist[i * 2], ndlist[i * 2 + 1]))
        if len(ndlist) % 2 == 0:
            nd = None
        else:
            nd = ndlist[-1]
        for other in newlist:
            nd = self.merge(nd, other)
        return nd
