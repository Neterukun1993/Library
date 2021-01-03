class SparseTable:
    def __init__(self, array, op):
        self.n = len(array)
        self.row_size = self.n.bit_length()
        self.op = op

        self.log_tbl = [0] * (self.n + 1)
        for i in range(2, self.n + 1):
            self.log_tbl[i] = self.log_tbl[i // 2] + 1

        self.sp_tbl = [0] * (self.n * self.row_size)
        for i in range(self.n):
            self.sp_tbl[i] = array[i]
        for row in range(1, self.row_size):
            prv_row = row - 1
            for i in range(self.n - (1 << row) + 1):
                self.sp_tbl[row * self.n + i] = \
                self.op(self.sp_tbl[prv_row * self.n + i],
                        self.sp_tbl[prv_row * self.n + i + (1 << prv_row)])

    def fold(self, l, r):
        row = self.log_tbl[r - l]
        return self.op(self.sp_tbl[row * self.n + l],
                       self.sp_tbl[row * self.n + r - (1 << row)])
