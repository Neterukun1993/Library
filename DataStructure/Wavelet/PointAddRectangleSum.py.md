---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\BinaryIndexedTree\PointAddRangeSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
  - icon: ':warning:'
    path: DataStructure\Wavelet\BitVector.py
    title: "\u30D3\u30C3\u30C8\u30D9\u30AF\u30C8\u30EB"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\point_add_rectangle_sum.test.py
    title: TestCase\LibraryChecker\point_add_rectangle_sum.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.Wavelet.BitVector import BitVector\r\nfrom DataStructure.BinaryIndexedTree.PointAddRangeSum\
    \ import BinaryIndexedTree\r\nfrom bisect import bisect_left\r\n\r\n\r\nclass\
    \ PointAddRectangleSum:\r\n    def __init__(self, ys, vals, MAXLOG=32):\r\n  \
    \      self.MAXLOG = MAXLOG\r\n        self.n = len(ys)\r\n        self.ys = ys\r\
    \n        self.mat = []\r\n        self.mid = []\r\n        self.data = []\r\n\
    \r\n        order = [i for i in range(self.n)]\r\n        for d in reversed(range(self.MAXLOG)):\r\
    \n            vec = BitVector(self.n + 1)\r\n            ls = []\r\n         \
    \   rs = []\r\n            for i, od in enumerate(order):\r\n                if\
    \ (ys[od] >> d) & 1:\r\n                    rs.append(od)\r\n                \
    \    vec.set(i)\r\n                else:\r\n                    ls.append(od)\r\
    \n            vec.build()\r\n            self.mat.append(vec)\r\n            self.mid.append(len(ls))\r\
    \n            order = ls + rs\r\n            self.data.append(BinaryIndexedTree(self.n))\r\
    \n            self.data[-1].build([vals[od] for od in order])\r\n\r\n    def point_add(self,\
    \ k, val):\r\n        y = self.ys[k]\r\n        for d in range(self.MAXLOG):\r\
    \n            if y >> (self.MAXLOG - d - 1) & 1:\r\n                k = self.mat[d].rank(k,\
    \ 1) + self.mid[d]\r\n            else:\r\n                k = self.mat[d].rank(k,\
    \ 0)\r\n            self.data[d].add(k, val)\r\n\r\n    def rect_sum(self, l,\
    \ r, upper):\r\n        res = 0\r\n        for d in range(self.MAXLOG):\r\n  \
    \          if upper >> (self.MAXLOG - d - 1) & 1:\r\n                res += self.data[d].sum(self.mat[d].rank(l,\
    \ 0), self.mat[d].rank(r, 0))\r\n                l = self.mat[d].rank(l, 1) +\
    \ self.mid[d]\r\n                r = self.mat[d].rank(r, 1) + self.mid[d]\r\n\
    \            else:\r\n                l = self.mat[d].rank(l, 0)\r\n         \
    \       r = self.mat[d].rank(r, 0)\r\n        return res\r\n\r\n\r\nclass CompressedPointAddRectangleSum:\r\
    \n    def __init__(self, points):\r\n        points = sorted(points)\r\n     \
    \   xs, ys, vals = zip(*points)\r\n        self.xs = xs\r\n        self.ys = sorted(set(ys))\r\
    \n        self.idxs = {(x, y): idx for idx, (x, y, _) in enumerate(points)}\r\n\
    \        self.comp = {val: idx for idx, val in enumerate(self.ys)}\r\n       \
    \ ys = [self.comp[val] for val in ys]\r\n        MAXLOG = len(self.ys).bit_length()\r\
    \n        self.mat = PointAddRectangleSum(ys, vals, MAXLOG)\r\n\r\n    def _rect_sum(self,\
    \ l, r, upper):\r\n        l = bisect_left(self.xs, l)\r\n        r = bisect_left(self.xs,\
    \ r)\r\n        upper = bisect_left(self.ys, upper)\r\n        return self.mat.rect_sum(l,\
    \ r, upper)\r\n\r\n    def rect_sum(self, l, r, lower, upper):\r\n        return\
    \ self._rect_sum(l, r, upper) - self._rect_sum(l, r, lower)\r\n\r\n    def point_add(self,\
    \ x, y, val):\r\n        if (x, y) not in self.idxs:\r\n            raise KeyError(f'point(x={x},\
    \ y={y}) must be pre-given as an argument')\r\n        idx = self.idxs[x, y]\r\
    \n        self.mat.point_add(idx, val)\r\n"
  dependsOn:
  - DataStructure\Wavelet\BitVector.py
  - DataStructure\BinaryIndexedTree\PointAddRangeSum.py
  isVerificationFile: false
  path: DataStructure\Wavelet\PointAddRectangleSum.py
  requiredBy: []
  timestamp: '2021-01-12 04:24:03+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\LibraryChecker\point_add_rectangle_sum.test.py
documentation_of: DataStructure\Wavelet\PointAddRectangleSum.py
layout: document
title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u77E9\u5F62\u548C\u53D6\u5F97"
---
