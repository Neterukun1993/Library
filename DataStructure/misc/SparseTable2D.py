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
            tbl = self.sp_tbl[lv_h][0]
            for i in range(self.h - dh * 2 + 1):
                for j in range(self.w):
                    data[i][j] = self.op(tbl[i][j], tbl[i + dh][j])
            self.sp_tbl[lv_h + 1].append(data)

        for lv_w in range(self.lg_w - 1):
            dw = 1 << lv_w
            data = [[0] * self.w for _ in range(self.h)]
            tbl = self.sp_tbl[0][lv_w]
            for i in range(self.h):
                for j in range(self.w - dw * 2 + 1):
                    data[i][j] = self.op(tbl[i][j], tbl[i][j + dw])
            self.sp_tbl[0].append(data)

        for lv_h in range(self.lg_h - 1):
            dh = 1 << lv_h
            for lv_w in range(self.lg_w - 1):
                dw = 1 << lv_w
                data = [[0] * self.w for i in range(self.h)]
                tbl = self.sp_tbl[lv_h][lv_w]
                for i in range(self.h - dh * 2 + 1):
                    for j in range(self.w - dw * 2 + 1):
                        data[i][j] = self.op(self.op(self.op(tbl[i][j], tbl[i][j + dw]), tbl[i + dh][j]), tbl[i + dh][j + dw])
                self.sp_tbl[lv_h + 1].append(data)

    def fold(self, hl, hr, wl, wr):
        lv_h = self.lg_tbl[hr - hl]
        lv_w = self.lg_tbl[wr - wl]
        tbl = self.sp_tbl[lv_h][lv_w]
        ul = tbl[hl][wl]
        ur = tbl[hl][wr - (1 << lv_w)]
        dl = tbl[hr - (1 << lv_h)][wl]
        dr = tbl[hr - (1 << lv_h)][wr - (1 << lv_w)]
        return self.op(self.op(self.op(ul, ur), dl), dr)
