class PersistentArray:
    LOG = 4
    MASK = (1 << LOG) - 1

    def __init__(self,):
        self.val = None
        self.ch = [None] * (1 << self.LOG)

    def set(self, i, val):
        pa = PersistentArray()
        pa.val = self.val
        pa.ch = self.ch[:]
        if i == 0:
            pa.val = val
        else:
            pa.ch[i & self.MASK] = pa.ch[i & self.MASK].set(i >> self.LOG, val)
        return pa

    def get(self, i):
        pa = self
        while i != 0:
            pa = pa.ch[i & self.MASK]
            i = i >> self.LOG
        return pa.val


def init_persistent_array(array):
    LOG = 4
    MASK = (1 << LOG) - 1

    def init_set(i, val, pa):
        if pa is None:
            pa = PersistentArray()
        if i == 0:
            pa.val = val
        else:
            pa.ch[i & MASK] = init_set(i >> LOG, val, pa.ch[i & MASK])
        return pa

    pa = None
    for i, val in enumerate(array):
        pa = init_set(i, val, pa)
    return pa
