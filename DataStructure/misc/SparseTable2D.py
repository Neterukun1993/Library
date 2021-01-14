class SparseTable2D:
    def __init__(self, matrix, op):
        self.h = len(matrix)
        self.w = len(matrix[0])
        self.op = op
        self.lg_h = self.h.bit_length()
        self.lg_w = self.w.bit_length()

        self.lg_tbl = [0] * (max(self.h, self.w) + 1)
        for i in range(2, len(self.lg_tbl)):
            self.lg_tbl[i] = self.lg_tbl[i // 2] + 1

        self.sp_tbl = [[] * self.lg_w for _ in range(self.lg_h)]
        self.sp_tbl[0].append(matrix)

        for lv_h in range(self.lg_h - 1):
            dh = 1 << lv_h
            data = [[0] * self.w for _ in range(self.h)]
            for i in range(self.h - dh * 2 + 1):
                for j in range(self.w):
                    u = self.sp_tbl[lv_h][0][i][j]
                    d = self.sp_tbl[lv_h][0][i + dh][j]
                    data[i][j] = self.op(u, d)
            self.sp_tbl[lv_h + 1].append(data)

        for lv_w in range(self.lg_w - 1):
            dw = 1 << lv_w
            data = [[0] * self.w for _ in range(self.h)]
            for i in range(self.h):
                for j in range(self.w - dw * 2 + 1):
                    l = self.sp_tbl[0][lv_w][i][j]
                    r = self.sp_tbl[0][lv_w][i][j + dw]
                    data[i][j] = self.op(l, r)
            self.sp_tbl[0].append(data)

        for lv_h in range(self.lg_h - 1):
            dh = 1 << lv_h
            for lv_w in range(self.lg_w - 1):
                dw = 1 << lv_w
                data = [[0] * self.w for i in range(self.h)]
                for i in range(self.h - dh * 2 + 1):
                    for j in range(self.w - dw * 2 + 1):
                        ul = self.sp_tbl[lv_h][lv_w][i][j]
                        ur = self.sp_tbl[lv_h][lv_w][i][j + dw]
                        dl = self.sp_tbl[lv_h][lv_w][i + dh][j]
                        dr = self.sp_tbl[lv_h][lv_w][i + dh][j + dw]
                        data[i][j] = self.op(self.op(self.op(ul, ur), dl), dr)
                self.sp_tbl[lv_h + 1].append(data)

    def fold(self, hl, hr, wl, wr):
        lv_h = self.lg_tbl[hr - hl]
        lv_w = self.lg_tbl[wr - wl]
        ul = self.sp_tbl[lv_h][lv_w][hl][wl]
        ur = self.sp_tbl[lv_h][lv_w][hl][wr - (1 << lv_w)]
        dl = self.sp_tbl[lv_h][lv_w][hr - (1 << lv_h)][wl]
        dr = self.sp_tbl[lv_h][lv_w][hr - (1 << lv_h)][wr - (1 << lv_w)]
        return self.op(self.op(self.op(ul, ur), dl), dr)
