---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_2_C.test.py
    title: TestCase/AOJ/DSL_2_C.test.py
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
  code: "class KDTree2D:\n    def __init__(self, points):\n        self.points = [tuple(p)\
    \ for p in points]\n        self.n = len(points)\n        self.l = [-1] * self.n\n\
    \        self.r = [-1] * self.n\n        self.root = self._build(0, self.n, 0)\n\
    \n    def _build(self, l, r, depth):\n        if l >= r:\n            return -1\n\
    \        mid = (l + r) // 2\n        if depth % 2 == 0:\n            self.points[l:r]\
    \ = sorted(self.points[l:r], key=lambda x: x[0])\n        else:\n            self.points[l:r]\
    \ = sorted(self.points[l:r], key=lambda x: x[1])\n        self.l[mid] = self._build(l,\
    \ mid, depth + 1)\n        self.r[mid] = self._build(mid + 1, r, depth + 1)\n\
    \        return mid\n\n    def _find(self, xl, xr, yl, yr, depth, idx, ans):\n\
    \        if idx is None:\n            idx = self.root\n        x, y = self.points[idx]\n\
    \        if xl <= x < xr and yl <= y < yr:\n            ans.append(self.points[idx])\n\
    \        if depth % 2 == 0:\n            if self.l[idx] != -1 and xl <= x:\n \
    \               self._find(xl, xr, yl, yr, depth + 1, self.l[idx], ans)\n    \
    \        if self.r[idx] != -1 and x < xr:\n                self._find(xl, xr,\
    \ yl, yr, depth + 1, self.r[idx], ans)\n        else:\n            if self.l[idx]\
    \ != -1 and yl <= y:\n                self._find(xl, xr, yl, yr, depth + 1, self.l[idx],\
    \ ans)\n            if self.r[idx] != -1 and y < yr:\n                self._find(xl,\
    \ xr, yl, yr, depth + 1, self.r[idx], ans)\n\n    def find(self, xl, xr, yl, yr):\n\
    \        ans = []\n        idx = self.root\n        depth = 0\n        self._find(xl,\
    \ xr, yl, yr, depth, idx, ans)\n        return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/misc/KDTree2D.py
  requiredBy: []
  timestamp: '2021-02-07 18:49:02+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_2_C.test.py
documentation_of: DataStructure/misc/KDTree2D.py
layout: document
title: "\u4E8C\u6B21\u5143\u9818\u57DF\u63A2\u7D22 (kD-Tree)"
---
## 概要
kD-Tree: 二次元平面上の点集合から領域探索を行うデータ構造

## 使い方
`KDTree2D(points: Iterable[Tuple[int, int]])`  
二次元平面上の `n` 個の点の集合 `points` に対し、kD-Tree を構築する。計算量 $O(n \log^2 n)$

- `find(xl: int, xr: int, yl: int, yr: int) -> List[Tuple[int, int]]`  
矩形範囲 $\lbrack xl, xr) × \lbrack yl, yr)$ に含まれている点を列挙する。矩形内に含まれる点の数を `k` とすると、計算量 $O(\sqrt n + k)$
