class ULLNode:
    MAX_SIZE = 4096

    def __init__(self):
        self.next = None
        self.list = []

    def is_full(self):
        return len(self.list) == self.MAX_SIZE


class UnrolledLinkedList:
    def __init__(self):
        self.size = 0
        self.root = ULLNode()

    def __getitem__(self, i):
        nd, i = self._find_node(i)
        return nd.list[i]

    def __setitem__(self, i, val):
        nd, i = self._find_node(i)
        nd.list[i] = val

    def __len__(self):
        return self.size

    def _find_node(self, i):
        nd = self.root
        while i >= len(nd.list):
            i -= len(nd.list)
            nd = nd.next
        return nd, i

    def insert(self, i, val):
        nd, i = self._find_node(i - 1)
        nd.list.insert(i + 1, val)
        self.size += 1
        if nd.is_full():
            new = ULLNode()
            new.next = nd.next
            nd.next = new
            nd.list, new.list = nd.list[:len(nd.list) // 2], nd.list[len(nd.list) // 2:]

    def delete(self, i):
        nd, i = self._find_node(i)
        del nd.list[i]
        self.size -= 1

    def dump(self):
        res = []
        nd = self.root
        while nd is not None:
            for val in nd.list:
                res.append(val)
            nd = nd.next
        return res
