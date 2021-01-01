class AccumulateSum2D:
    def __init__(self, matrix):
        self.h = len(matrix)
        self.w = len(matrix[0])
        self.cumsum = [[0] * (self.w + 1) for _ in range(self.h + 1)]

        for i in range(self.h):
            for j in range(self.w):
                self.cumsum[i + 1][j + 1] = self.cumsum[i + 1][j] + matrix[i][j]
        for i in range(self.h):
            for j in range(self.w):
                self.cumsum[i + 1][j + 1] += self.cumsum[i][j + 1]

    def sum(self, hl, hr, wl, wr):
        """sum of values in range [hl, hr) * [wl, wr)"""
        return (self.cumsum[hr][wr] + self.cumsum[hl][wl]
                - self.cumsum[hr][wl] - self.cumsum[hl][wr])
