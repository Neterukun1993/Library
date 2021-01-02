class PersistentArrayNode:
    def __init__(self, LOG):
        self.val = None
        self.ch = [None] * (1 << LOG)


class PersistentArray:
    def __init__(self, LOG=4):
        self.LOG = LOG
        self.MASK = (1 << LOG) - 1

    def build(self, array):
        rt = None
        for i, val in enumerate(array):
            rt = self.init_set(i, val, rt)
        return rt
 
    def init_set(self, i, val, t):
        if t is None:
            t = PersistentArrayNode(self.LOG)
        if i == 0:
            t.val = val
        else:
            t.ch[i & self.MASK] = self.init_set(i >> self.LOG, val, t.ch[i & self.MASK])
        return t

    def set(self, i, val, t):
        ret = PersistentArrayNode(self.LOG)
        if t is not None:
            ret.ch = t.ch[:]
            ret.val = t.val
        if i == 0:
            ret.val = val
        else:
            ret.ch[i & self.MASK] = self.set(i >> self.LOG, val, ret.ch[i & self.MASK])
        return ret

    def get(self, i, t):
        if i == 0:
            return t.val
        else:
            return self.get(i >> self.LOG, t.ch[i & self.MASK])
