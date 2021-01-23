class RollingHash2D:
    def __init__(self, matrix):
        self.h = len(matrix)
        self.w = len(matrix[0])
        self.BASEh = 1234
        self.BASEw = 5678
        self.MASK30 = (1 << 30) - 1
        self.MASK31 = (1 << 31) - 1
        self.MASK61 = self.MOD = (1 << 61) - 1
        self.hash = [[0] * (self.w + 1) for _ in range(self.h + 1)]
        self.ph = [1] * (self.h + 1)
        self.pw = [1] * (self.w + 1)
        for i in range(self.h):
            self.ph[i + 1] = self.calc_mod(self.mul(self.ph[i], self.BASEh))
        for i in range(self.w):
            self.pw[i + 1] = self.calc_mod(self.mul(self.pw[i], self.BASEw))

        for i in range(self.h):
            for j in range(self.w):
                res = self.mul(self.hash[i + 1][j], self.BASEw)
                res += self.mul(self.hash[i][j + 1], self.BASEh)
                res -= self.mul(self.hash[i][j], self.BASEw * self.BASEh)
                self.hash[i + 1][j + 1] = self.calc_mod(res + ord(matrix[i][j]))

    def calc_mod(self, x):
        xu = x >> 61
        xd = x & self.MASK61
        x = xu + xd
        if x >= self.MOD:
            x -= self.MOD
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

    def get_hash(self, hl, hr, wl, wr):
        p, q = self.pw[wr - wl], self.ph[hr - hl]
        res = self.hash[hr][wr]
        res -= self.mul(self.hash[hr][wl], p)
        res -= self.mul(self.hash[hl][wr], q)
        res += self.mul(self.hash[hl][wl], self.mul(p, q))
        return self.calc_mod(res)
