class SparseTable2D:
    def __init__(self, matrix, op):
        h = len(matrix)
        w = len(matrix[0])
        self.op = op
        lg_h = h.bit_length()
        lg_w = w.bit_length()

        self.lg_tbl = [0] * (max(h, w) + 1)
        for i in range(2, len(self.lg_tbl)):
            self.lg_tbl[i] = self.lg_tbl[i // 2] + 1

        self.sp_tbl = [[] * lg_w for _ in range(lg_h)]
        self.sp_tbl[0].append(matrix)

        for lv_h in range(lg_h - 1):
            dh = 1 << lv_h
            data = [[0] * w for _ in range(h - dh * 2 + 1)]
            tbl = self.sp_tbl[lv_h][0]
            for i in range(h - dh * 2 + 1):
                for j in range(w):
                    data[i][j] = op(tbl[i][j], tbl[i + dh][j])
            self.sp_tbl[lv_h + 1].append(data)

        for lv_w in range(lg_w - 1):
            dw = 1 << lv_w
            data = [[0] * (w - dw * 2 + 1) for _ in range(h)]
            tbl = self.sp_tbl[0][lv_w]
            for i in range(h):
                for j in range(w - dw * 2 + 1):
                    data[i][j] = op(tbl[i][j], tbl[i][j + dw])
            self.sp_tbl[0].append(data)

        for lv_h in range(lg_h - 1):
            dh = 1 << lv_h
            for lv_w in range(lg_w - 1):
                dw = 1 << lv_w
                data = [[0] * (w - dw * 2 + 1) for _ in range(h - dh * 2 + 1)]
                tbl = self.sp_tbl[lv_h][lv_w]
                for i in range(h - dh * 2 + 1):
                    for j in range(w - dw * 2 + 1):
                        # 二項演算ではない
                        data[i][j] = op(tbl[i][j], tbl[i][j + dw], tbl[i + dh][j], tbl[i + dh][j + dw])
                self.sp_tbl[lv_h + 1].append(data)

    def fold(self, hl, hr, wl, wr):
        lv_h = self.lg_tbl[hr - hl]
        lv_w = self.lg_tbl[wr - wl]
        tbl = self.sp_tbl[lv_h][lv_w]
        ul = tbl[hl][wl]
        ur = tbl[hl][wr - (1 << lv_w)]
        dl = tbl[hr - (1 << lv_h)][wl]
        dr = tbl[hr - (1 << lv_h)][wr - (1 << lv_w)]
        return self.op(ul, ur, dl, dr)  # 二項演算ではない
