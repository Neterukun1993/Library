---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/line_add_get_min.test.py
    title: TestCase/LibraryChecker/line_add_get_min.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/segment_add_get_min.test.py
    title: TestCase/LibraryChecker/segment_add_get_min.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from bisect import bisect_left\n\n\nclass LiChaoTree:\n    def __init__(self,\
    \ xs, INF=10**18):\n        self.INF = INF\n        xs = sorted(list(set(xs)))\n\
    \        n = len(xs)\n        self.size = 1 << (n - 1).bit_length()\n        self.comp_xs\
    \ = {x: ind for ind, x in enumerate(xs)}\n        self.xs = xs + [self.INF] *\
    \ (self.size - n)\n        self.data = [None] * (self.size + self.size)\n\n  \
    \  def update(self, line, k, l, r):\n        while True:\n            if self.data[k]\
    \ is None:\n                self.data[k] = line\n                return\n    \
    \        mid = (l + r) >> 1\n            lx, mx, rx = self.xs[l], self.xs[mid],\
    \ self.xs[r - 1]\n            lu = self.f(line, lx) < self.f(self.data[k], lx)\n\
    \            mu = self.f(line, mx) < self.f(self.data[k], mx)\n            ru\
    \ = self.f(line, rx) < self.f(self.data[k], rx)\n            if lu and ru:\n \
    \               self.data[k] = line\n                return\n            if not\
    \ lu and not ru:\n                return\n            if mu:\n               \
    \ self.data[k], line = line, self.data[k]\n            if lu != mu:\n        \
    \        r, k = mid, k << 1\n            else:\n                l, k = mid, k\
    \ << 1 | 1\n\n    def add_line(self, line):\n        self.update(line, 1, 0, self.size)\n\
    \n    def add_seg(self, line, l, r):\n        l = bisect_left(self.xs, l)\n  \
    \      r = bisect_left(self.xs, r)\n        l0, r0 = l + self.size, r + self.size\n\
    \        size = 1\n        while l0 < r0:\n            if l0 & 1:\n          \
    \      self.update(line, l0, l, l + size)\n                l0 += 1\n         \
    \       l += size\n            if r0 & 1:\n                r0 -= 1\n         \
    \       r -= size\n                self.update(line, r0, r, r + size)\n      \
    \      l0 >>= 1\n            r0 >>= 1\n            size <<= 1\n\n    def f(self,\
    \ line, x):\n        a, b = line\n        return a * x + b\n\n    def min(self,\
    \ x):\n        k = self.comp_xs[x] + self.size\n        res = self.INF\n     \
    \   while k > 0:\n            if self.data[k] is not None:\n                res\
    \ = min(res, self.f(self.data[k], x))\n            k >>= 1\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SegmentTree/LiChaoTree.py
  requiredBy: []
  timestamp: '2021-01-03 06:18:12+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/line_add_get_min.test.py
  - TestCase/LibraryChecker/segment_add_get_min.test.py
documentation_of: DataStructure/SegmentTree/LiChaoTree.py
layout: document
title: Li-Chao Tree
---
## 使い方
`LiChaoTree(xs: Iterable[int], INF=10**18)`  
`xs` の要素を `min` クエリにおける $x$ 座標として使用可能な、空の直線 (線分) 集合を構築する。計算量 $O(n \log n)$

- `add_line(line: Tuple[int, int]) -> None`  
集合に (傾き, 切片) で表される直線 `line` を追加する。計算量 $O(\log n)$

- `add_seg(line: Tuple[int, int], l: int, r: int) -> None`  
集合に (傾き, 切片) で表される線分 `line` (ただし $x \in [l,r)$) を追加する。計算量 $O(\log ^2 n)$

- `min(x: int) -> int`  
$x$ 座標が `x` のときの、$y$ 座標の最小値を返す。そのような $y$ 座標が存在しない場合は `INF` を返す。`x` が `xs` の要素でない場合は例外 `KeyError` が発生するので注意。計算量 $O(\log n)$
