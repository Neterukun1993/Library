class DisjointSparseTable:
    def __init__(self, array, op):
        self.n = len(array)
        self.op = op
        self.row_size = self.n.bit_length()
        self.log_tbl = [0] * (1 << self.row_size)
        for i in range(2, 1 << self.row_size):
            self.log_tbl[i] = self.log_tbl[i // 2] + 1

        self.sp_tbl = [[0] * self.n for _ in range(self.row_size)]
        for i, val in enumerate(array):
            self.sp_tbl[0][i] = val
        for row in range(1, self.row_size):
            shift = 1 << row
            l = 0
            while l < self.n:
                mid = l + shift
                t = min(mid, self.n)
                self.sp_tbl[row][t - 1] = array[t - 1]
                for k in reversed(range(l, t - 1)):
                    self.sp_tbl[row][k] = self.op(array[k], self.sp_tbl[row][k + 1])
                if len(array) <= t:
                    break
                r = min(mid, self.n)
                self.sp_tbl[row][t] = array[t]
                for k in range(t + 1, r):
                    self.sp_tbl[row][k] = self.op(self.sp_tbl[row][k - 1], array[k])
                l = mid + shift

    def fold(self, l, r):
        r -= 1
        if l == r:
            return self.sp_tbl[0][l]
        p = self.log_tbl[l ^ r]
        return self.op(self.sp_tbl[p][l], self.sp_tbl[p][r])
