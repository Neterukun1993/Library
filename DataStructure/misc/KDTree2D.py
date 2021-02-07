class KDTree2D:
    def __init__(self, points):
        self.points = [tuple(p) for p in points]
        self.n = len(points)
        self.l = [-1] * self.n
        self.r = [-1] * self.n
        self.root = self._build(0, self.n, 0)

    def _build(self, l, r, depth):
        if l >= r:
            return -1
        mid = (l + r) // 2
        if depth % 2 == 0:
            self.points[l:r] = sorted(self.points[l:r], key=lambda x: x[0])
        else:
            self.points[l:r] = sorted(self.points[l:r], key=lambda x: x[1])
        self.l[mid] = self._build(l, mid, depth + 1)
        self.r[mid] = self._build(mid + 1, r, depth + 1)
        return mid

    def _find(self, xl, xr, yl, yr, depth, idx, ans):
        if idx is None:
            idx = self.root
        x, y = self.points[idx]
        if xl <= x < xr and yl <= y < yr:
            ans.append(self.points[idx])
        if depth % 2 == 0:
            if self.l[idx] != -1 and xl <= x:
                self._find(xl, xr, yl, yr, depth + 1, self.l[idx], ans)
            if self.r[idx] != -1 and x < xr:
                self._find(xl, xr, yl, yr, depth + 1, self.r[idx], ans)
        else:
            if self.l[idx] != -1 and yl <= y:
                self._find(xl, xr, yl, yr, depth + 1, self.l[idx], ans)
            if self.r[idx] != -1 and y < yr:
                self._find(xl, xr, yl, yr, depth + 1, self.r[idx], ans)

    def find(self, xl, xr, yl, yr):
        ans = []
        idx = self.root
        depth = 0
        self._find(xl, xr, yl, yr, depth, idx, ans)
        return ans
