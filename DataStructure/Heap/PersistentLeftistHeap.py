class LeftistHeap:
    E = None

    def __new__(cls, *args):
        if cls.E is None:
            cls.E = super().__new__(cls)
        return super().__new__(cls) if args else cls.E

    def __init__(self, rank=0, key=None, value=None, a=None, b=None):
        self.rank = rank
        self.key = key
        self.value = value
        self.a = a
        self.b = b

    def __bool__(self):
        return self is not LeftistHeap.E

    def __lt__(self, other):
        return self.key < other.key

    @staticmethod
    def _make(key, value, a, b):
        if a.rank >= b.rank:
            a, b = b, a
        return LeftistHeap(a.rank + 1, key, value, b, a)

    @staticmethod
    def merge(hl, hr):
        if not hl:
            return hr
        elif not hr:
            return hl
        elif hl.key <= hr.key:
            return LeftistHeap._make(hl.key, hl.value, hl.a,
                                     LeftistHeap.merge(hl.b, hr))
        else:
            return LeftistHeap._make(hr.key, hr.value, hr.a,
                                     LeftistHeap.merge(hl, hr.b))

    def insert(self, key, value):
        new = LeftistHeap(1, key, value, LeftistHeap.E, LeftistHeap.E)
        return LeftistHeap.merge(new, self)

    @property
    def find_min(self):
        if self is LeftistHeap.E:
            raise IndexError("find from empty heap")
        return self.key, self.value

    def delete_min(self):
        if self is LeftistHeap.E:
            raise IndexError("delete from empty heap")
        return self.merge(self.a, self.b)
