---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: DataStructure/Wavelet/BitVector.py
    title: "\u30D3\u30C3\u30C8\u30D9\u30AF\u30C8\u30EB"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/rectangle_sum.WaveletMatrix.test.py
    title: TestCase/LibraryChecker/rectangle_sum.WaveletMatrix.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.Wavelet.BitVector import BitVector\nfrom bisect import\
    \ bisect_left\n\n\nclass RectangleSum:\n    def __init__(self, ys, vals, MAXLOG=32):\n\
    \        self.MAXLOG = MAXLOG\n        self.n = len(vals)\n        self.mat =\
    \ []\n        self.mid = []\n        self.data = [[0] * (self.n + 1) for i in\
    \ range(self.MAXLOG)]\n\n        order = [i for i in range(self.n)]\n        for\
    \ d in reversed(range(self.MAXLOG)):\n            vec = BitVector(self.n + 1)\n\
    \            ls = []\n            rs = []\n            for i, od in enumerate(order):\n\
    \                if ys[od] & (1 << d):\n                    rs.append(od)\n  \
    \                  vec.set(i)\n                else:\n                    ls.append(od)\n\
    \            vec.build()\n            self.mat.append(vec)\n            self.mid.append(len(ls))\n\
    \            order = ls + rs\n            for i, val in enumerate(order):\n  \
    \              self.data[- d - 1][i + 1] = self.data[- d - 1][i] + vals[val]\n\
    \n    def rect_sum(self, l, r, upper):\n        res = 0\n        for d in range(self.MAXLOG):\n\
    \            if upper >> (self.MAXLOG - d - 1) & 1:\n                res += self.data[d][self.mat[d].rank(r,\
    \ 0)]\n                res -= self.data[d][self.mat[d].rank(l, 0)]\n         \
    \       l = self.mat[d].rank(l, 1) + self.mid[d]\n                r = self.mat[d].rank(r,\
    \ 1) + self.mid[d]\n            else:\n                l = self.mat[d].rank(l,\
    \ 0)\n                r = self.mat[d].rank(r, 0)\n        return res\n\n\nclass\
    \ CompressedRectangleSum:\n    def __init__(self, points):\n        points = sorted(points)\n\
    \        xs, ys, vals = zip(*points)\n        self.xs = xs\n        self.ys =\
    \ sorted(set(ys))\n        self.comp = {val: idx for idx, val in enumerate(self.ys)}\n\
    \        ys = [self.comp[val] for val in ys]\n        MAXLOG = len(self.ys).bit_length()\n\
    \        self.mat = RectangleSum(ys, vals, MAXLOG)\n\n    def rect_sum(self, l,\
    \ r, lower, upper):\n        l = bisect_left(self.xs, l)\n        r = bisect_left(self.xs,\
    \ r)\n        lower = bisect_left(self.ys, lower)\n        upper = bisect_left(self.ys,\
    \ upper)\n        return self.mat.rect_sum(l, r, upper) - self.mat.rect_sum(l,\
    \ r, lower)\n"
  dependsOn:
  - DataStructure/Wavelet/BitVector.py
  isVerificationFile: false
  path: DataStructure/Wavelet/RectangleSum.py
  requiredBy: []
  timestamp: '2022-08-07 15:04:38+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/rectangle_sum.WaveletMatrix.test.py
documentation_of: DataStructure/Wavelet/RectangleSum.py
layout: document
title: "\u77E9\u5F62\u548C\u53D6\u5F97"
---
## 概要
二次元平面上の $n$ 個の重み付き点に対して、前計算を $O(n \log n)$ で行い、矩形範囲内の重み総和クエリに $O(\log n)$ で答えるデータ構造。内部では累積和を保持した Wavelet Matrix を構築する。

## 使い方
`CompressedRectangleSum(points: Iterable[Tuple[int, int, int]])`  
二次元平面上の $n$ 個の重み付き点 `points` から Wavelet Matrix を構築する。各点は ($x$ 座標, $y$ 座標, 重み) で与えられる。計算量 $O(n \log n)$

- `rect_sum(l: int, r: int, lower: int, upper: int) -> int`  
矩形範囲 $\lbrack l, r) × \lbrack lower, upper)$ に含まれる点の重みの総和を返す。計算量 $O(\log n)$
