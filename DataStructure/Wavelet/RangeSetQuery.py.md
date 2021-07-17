---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: DataStructure/Wavelet/BitVector.py
    title: "\u30D3\u30C3\u30C8\u30D9\u30AF\u30C8\u30EB"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.Wavelet.BitVector import BitVector\nfrom bisect import\
    \ bisect_left\n\n\nclass _InnerRangeSetQuery:\n    def __init__(self, ys, MAXLOG=32):\n\
    \        self.MAXLOG = MAXLOG\n        self.n = len(ys)\n        self.mat = []\n\
    \        self.mid = []\n\n        order = [i for i in range(self.n)]\n       \
    \ for d in reversed(range(self.MAXLOG)):\n            vec = BitVector(self.n +\
    \ 1)\n            ls = []\n            rs = []\n            for i, od in enumerate(order):\n\
    \                if ys[od] & (1 << d):\n                    rs.append(od)\n  \
    \                  vec.set(i)\n                else:\n                    ls.append(od)\n\
    \            vec.build()\n            self.mat.append(vec)\n            self.mid.append(len(ls))\n\
    \            order = ls + rs\n\n    def _rect_sum(self, l, r, upper):\n      \
    \  res = 0\n        for d in range(self.MAXLOG):\n            if upper >> (self.MAXLOG\
    \ - d - 1) & 1:\n                res += self.mat[d].rank(r, 0)\n             \
    \   res -= self.mat[d].rank(l, 0)\n                l = self.mat[d].rank(l, 1)\
    \ + self.mid[d]\n                r = self.mat[d].rank(r, 1) + self.mid[d]\n  \
    \          else:\n                l = self.mat[d].rank(l, 0)\n               \
    \ r = self.mat[d].rank(r, 0)\n        return res\n\n\nclass RangeSetQuery:\n \
    \   def __init__(self, array):\n        limit = len(array)\n        idxs = {}\n\
    \        points = []\n        for i, val in enumerate(c):\n            if val\
    \ in idxs:\n                points.append((idxs[val], i))\n            idxs[val]\
    \ = i\n        points.append((limit, limit))\n\n        xs, ys = zip(*sorted(points))\n\
    \        self.xs = xs\n        self.ys = sorted(set(ys))\n        comp = {val:\
    \ idx for idx, val in enumerate(self.ys)}\n        MAXLOG = len(self.ys).bit_length()\n\
    \        self.mat = _InnerRangeSetQuery([comp[val] for val in ys], MAXLOG)\n\n\
    \    def query(self, l, r):\n        width = r - l\n        lower = bisect_left(self.ys,\
    \ l)\n        upper = bisect_left(self.ys, r)\n        l = bisect_left(self.xs,\
    \ l)\n        r = bisect_left(self.xs, r)\n        return width - (self.mat._rect_sum(l,\
    \ r, upper)\n                        + self.mat._rect_sum(l, r, lower))\n"
  dependsOn:
  - DataStructure/Wavelet/BitVector.py
  isVerificationFile: false
  path: DataStructure/Wavelet/RangeSetQuery.py
  requiredBy: []
  timestamp: '2021-07-18 02:14:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/Wavelet/RangeSetQuery.py
layout: document
title: "\u7A2E\u985E\u6570\u53D6\u5F97"
---

## 使い方
`RangeSetQuery(array: Sequence[int])`
長さ $n$ の配列 `array` から Wavelet Matrix を構築する。計算量 $O(n \log n)$

- `query(l, r) -> int`  
範囲 $\lbrack l, r)$ に含まれる要素の種類数を返す。計算量 $O(\log n)$
