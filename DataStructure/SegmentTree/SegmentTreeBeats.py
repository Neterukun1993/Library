class SegmentTreeBeats:
    def __init__(self, n, INF=10**18):
        self.MAX = INF
        self.MIN = -INF
        self.size = 1 << (n - 1).bit_length()
        sz = self.size * 2 - 1
        self.sum_ = [0] * sz
        self.max_v = [self.MIN] * sz
        self.min_v = [self.MAX] * sz
        self.max_c = [1] * sz
        self.min_c = [1] * sz
        self.smax_v = [self.MIN] * sz
        self.smin_v = [self.MAX] * sz
        self.lz_add = [0] * sz

    def build(self, array):
        for i, val in enumerate(array, self.size - 1):
            self.sum_[i] = self.min_v[i] = self.max_v[i] = val
        for i in range(self.size - 2, -1, -1):
            self.update(i)

    def update(self, i):
        if i >= self.size - 1: return
        i1, i2 = i * 2 + 1, i * 2 + 2
        self.sum_[i] = self.sum_[i1] + self.sum_[i2]
        self.max_v[i] = max(self.max_v[i1], self.max_v[i2])
        if self.max_v[i1] > self.max_v[i2]:
            self.max_c[i] = self.max_c[i1]
            self.smax_v[i] = max(self.smax_v[i1], self.max_v[i2])
        elif self.max_v[i1] < self.max_v[i2]:
            self.max_c[i] = self.max_c[i2]
            self.smax_v[i] = max(self.max_v[i1], self.smax_v[i2])
        else:
            self.max_c[i] = self.max_c[i1] + self.max_c[i2]
            self.smax_v[i] = max(self.smax_v[i1], self.smax_v[i2])

        self.min_v[i] = min(self.min_v[i1], self.min_v[i2])
        if self.min_v[i1] < self.min_v[i2]:
            self.min_c[i] = self.min_c[i1]
            self.smin_v[i] = min(self.smin_v[i1], self.min_v[i2])
        elif self.min_v[i1] > self.min_v[i2]:
            self.min_c[i] = self.min_c[i2]
            self.smin_v[i] = min(self.min_v[i1], self.smin_v[i2])
        else:
            self.min_c[i] = self.min_c[i1] + self.min_c[i2]
            self.smin_v[i] = min(self.smin_v[i1], self.smin_v[i2])

    def push(self, i, l, r):
        i1, i2 = i * 2 + 1, i * 2 + 2
        if self.lz_add[i] != 0:
            self.sum_[i] += self.lz_add[i] * (r - l)
            self.min_v[i] += self.lz_add[i]
            self.smin_v[i] += self.lz_add[i]
            self.max_v[i] += self.lz_add[i]
            self.smax_v[i] += self.lz_add[i]
            if i < self.size - 1:
                self.lz_add[i1] += self.lz_add[i]
                self.lz_add[i2] += self.lz_add[i]
            self.lz_add[i] = 0
        if i < self.size - 1:
            if self.max_v[i] < self.max_v[i1] + self.lz_add[i1]:
                self.chmin_at(i1, self.max_v[i] - self.lz_add[i1], l, (l + r) // 2)
            if self.max_v[i] < self.max_v[i2] + self.lz_add[i2]:
                self.chmin_at(i2, self.max_v[i] - self.lz_add[i2], (l + r) // 2, r)
            if self.min_v[i] > self.min_v[i1] + self.lz_add[i1]:
                self.chmax_at(i1, self.min_v[i] - self.lz_add[i1], l, (l + r) // 2)
            if self.min_v[i] > self.min_v[i2] + self.lz_add[i2]:
                self.chmax_at(i2, self.min_v[i] - self.lz_add[i2], (l + r) // 2, r)

    def chmin_at(self, i, x, l, r):
        if self.max_v[i] == self.min_v[i]:
            self.sum_[i] = x * (r - l)
            self.max_v[i] = self.min_v[i] = x
        elif self.max_v[i] == self.smin_v[i]:
            self.sum_[i] += (x - self.max_v[i]) * self.max_c[i]
            self.max_v[i] = self.smin_v[i] = x
        else:
            self.sum_[i] += (x - self.max_v[i]) * self.max_c[i]
            self.max_v[i] = x

    def chmax_at(self, i, x, l, r):
        if self.max_v[i] == self.min_v[i]:
            self.sum_[i] = x * (r - l)
            self.max_v[i] = self.min_v[i] = x
        elif self.min_v[i] == self.smax_v[i]:
            self.sum_[i] += (x - self.min_v[i]) * self.min_c[i]
            self.min_v[i] = self.smax_v[i] = x
        else:
            self.sum_[i] += (x - self.min_v[i]) * self.min_c[i]
            self.min_v[i] = x

    def range_chmin(self, a, b, x, i=0, l=0, r=-1):
        if r == -1: r = self.size
        self.push(i, l, r)
        if r <= a or b <= l or self.max_v[i] <= x: return
        if a <= l and r <= b and self.smax_v[i] < x:
            self.chmin_at(i, x, l, r)
            self.push(i, l, r)
            return
        self.range_chmin(a, b, x, i * 2 + 1, l, (l + r) // 2)
        self.range_chmin(a, b, x, i * 2 + 2, (l + r) // 2, r)
        self.update(i)

    def range_chmax(self, a, b, x, i=0, l=0, r=-1):
        if r == -1: r = self.size
        self.push(i, l, r)
        if r <= a or b <= l or self.min_v[i] >= x: return
        if a <= l and r <= b and self.smin_v[i] > x:
            self.chmax_at(i, x, l, r)
            self.push(i, l, r)
            return
        self.range_chmax(a, b, x, i * 2 + 1, l, (l + r) // 2)
        self.range_chmax(a, b, x, i * 2 + 2, (l + r) // 2, r)
        self.update(i)

    def range_add(self, a, b, x, i=0, l=0, r=-1):
        if r == -1: r = self.size
        self.push(i, l, r)
        if r <= a or b <= l: return
        if a <= l and r <= b:
            self.lz_add[i] += x
            self.push(i, l, r)
            return
        self.range_add(a, b, x, i * 2 + 1, l, (l + r) // 2)
        self.range_add(a, b, x, i * 2 + 2, (l + r) // 2, r)
        self.update(i)

    def fold_min(self, a, b, i=0, l=0, r=-1):
        if r == -1: r = self.size
        self.push(i, l, r)
        if r <= a or b <= l: return self.MAX
        if a <= l and r <= b: return self.min_v[i]
        vl = self.fold_min(a, b, i * 2 + 1, l, (l + r) // 2)
        vr = self.fold_min(a, b, i * 2 + 2, (l + r) // 2, r)
        return min(vl, vr)

    def fold_max(self, a, b, i=0, l=0, r=-1):
        if r == -1: r = self.size
        self.push(i, l, r)
        if r <= a or b <= l: return self.MIN
        if a <= l and r <= b: return self.max_v[i]
        vl = self.fold_max(a, b, i * 2 + 1, l, (l + r) // 2)
        vr = self.fold_max(a, b, i * 2 + 2, (l + r) // 2, r)
        return max(vl, vr)

    def fold_sum(self, a, b, i=0, l=0, r=-1):
        if r == -1: r = self.size
        self.push(i, l, r)
        if r <= a or b <= l: return 0
        if a <= l and r <= b: return self.sum_[i]
        vl = self.fold_sum(a, b, i * 2 + 1, l, (l + r) // 2)
        vr = self.fold_sum(a, b, i * 2 + 2, (l + r) // 2, r)
        return vl + vr
