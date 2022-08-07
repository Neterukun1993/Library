class BitVector:
    def __init__(self, n):
        # self.BLOCK_WIDTH = 32
        self.BLOCK_NUM = (n + 31) >> 5
        self.bit = [0] * self.BLOCK_NUM
        self.count = [0] * self.BLOCK_NUM

    def _popcount(self, x):
        x = x - ((x >> 1) & 0x55555555)
        x = (x & 0x33333333) + ((x >> 2) & 0x33333333)
        x = (x + (x >> 4)) & 0x0F0F0F0F
        x = x + (x >> 8)
        x = x + (x >> 16)
        return x & 0x0000007F

    def set(self, i):
        self.bit[i >> 5] |= 1 << (i & 31)

    def access(self, i):
        return (self.bit[i >> 5] >> (i & 31)) & 1

    def build(self):
        for i in range(self.BLOCK_NUM - 1):
            self.count[i + 1] = self.count[i] + self._popcount(self.bit[i])

    def rank(self, r, f):
        res = self.count[r >> 5] + self._popcount(self.bit[r >> 5] & ((1 << (r & 31)) - 1))
        return res if f else r - res
