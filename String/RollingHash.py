class RollingHash:
    def __init__(self, string):
        self.n = len(string)
        self.BASE = 1234
        self.MASK30 = (1 << 30) - 1
        self.MASK31 = (1 << 31) - 1
        self.MASK61 = (1 << 61) - 1
        self.MOD = self.MASK61
        self.hash = [0] * (self.n + 1)
        self.pow = [1] * (self.n + 1)

        for i, char in enumerate(string):
            self.hash[i + 1] = self.calc_mod(self.mul(self.hash[i], self.BASE)
                                             + ord(char))
            self.pow[i + 1] = self.calc_mod(self.mul(self.pow[i], self.BASE))

    def calc_mod(self, x):
        xu = x >> 61
        xd = x & self.MASK61
        x = xu + xd
        if x >= self.MOD:
            x -= MASK61
        return x

    def mul(self, a, b):
        au = a >> 31
        ad = a & self.MASK31
        bu = b >> 31
        bd = b & self.MASK31
        mid = ad * bu + au * bd
        midu = mid >> 30
        midd = mid & self.MASK30
        return self.calc_mod(au * bu * 2 + midu + (midd << 31) + ad * bd)

    def get_hash(self, l, r):
        res = self.calc_mod(self.hash[r]
                            - self.mul(self.hash[l], self.pow[r - l]))
        return res

    def merge(self, h1, h2, length2):
        return self.calc_mod(self.mul(h1, self.pow[length2]) + h2)

    def get_lcp(self, l1, r1, l2, r2):
        ng = min(r1 - l1, r2 - l2) + 1
        ok = 0
        while abs(ok - ng) > 1:
            mid = (ok + ng) // 2
            if self.get_hash(l1, l1 + mid) == self.get_hash(l2, l2 + mid):
                ok = mid
            else:
                ng = mid
        return ok
