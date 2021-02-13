class Imos2D:
    def __init__(self, h, w):
        self.h = h
        self.w = w
        self.imos = [[0] * (self.w + 1) for _ in range(self.h + 1)]

    def __getitem__(self, i):
        return self.imos[i]

    def add(self, hl, hr, wl, wr, val):
        """add value in range [hl, hr) * [wl, wr)"""
        self.imos[hl][wl] += val
        self.imos[hr][wl] -= val
        self.imos[hl][wr] -= val
        self.imos[hr][wr] += val

    def build(self):
        for i in range(self.h):
            for j in range(self.w):
                self.imos[i][j + 1] += self.imos[i][j]
        for i in range(self.h):
            for j in range(self.w):
                self.imos[i + 1][j] += self.imos[i][j]
