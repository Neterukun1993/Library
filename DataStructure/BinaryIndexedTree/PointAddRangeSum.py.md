---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure/BinaryIndexedTree/inversion_number.py
    title: "\u8EE2\u5012\u6570"
  - icon: ':heavy_check_mark:'
    path: DataStructure/Wavelet/PointAddRectangleSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u77E9\u5F62\u548C\u53D6\u5F97"
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/EulerTourPathQuery.py
    title: "\u30AA\u30A4\u30E9\u30FC\u30C4\u30A2\u30FC (\u30D1\u30B9\u306B\u5BFE\u3059\
      \u308B\u30AF\u30A8\u30EA)"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_2_B.BIT.test.py
    title: TestCase/AOJ/DSL_2_B.BIT.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_5_D.test.py
    title: TestCase/AOJ/GRL_5_D.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/point_add_range_sum.test.py
    title: TestCase/LibraryChecker/point_add_range_sum.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/vertex_add_path_sum.test.py
    title: TestCase/LibraryChecker/vertex_add_path_sum.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/vertex_add_subtree_sum.test.py
    title: TestCase/LibraryChecker/vertex_add_subtree_sum.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BinaryIndexedTree:\n    def __init__(self, n):\n        self.size =\
    \ n\n        self.bit = [0] * (self.size + 1)\n\n    def build(self, array):\n\
    \        for i, val in enumerate(array):\n            self.bit[i + 1] = val\n\
    \        for i in range(1, self.size):\n            if i + (i & -i) > self.size:\n\
    \                continue\n            self.bit[i + (i & -i)] += self.bit[i]\n\
    \n    def _sum(self, i):\n        s = 0\n        while i > 0:\n            s +=\
    \ self.bit[i]\n            i -= i & -i\n        return s\n\n    def add(self,\
    \ i, val):\n        i += 1\n        while i <= self.size:\n            self.bit[i]\
    \ += val\n            i += i & -i\n\n    def sum(self, l, r):\n        \"\"\"\
    sum of values in range [l, r)\"\"\"\n        return self._sum(r) - self._sum(l)\n\
    \n    def bisect_left(self, val):\n        \"\"\"minimum idx s.t. sum[0, idx)\
    \ >= val\"\"\"\n        if val <= 0:\n            return 0\n        idx = 0\n\
    \        k = 1 << self.size.bit_length()\n        while k:\n            if idx\
    \ + k <= self.size and self.bit[idx + k] < val:\n                val -= self.bit[idx\
    \ + k]\n                idx += k\n            k >>= 1\n        return idx + 1\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/BinaryIndexedTree/PointAddRangeSum.py
  requiredBy:
  - Graph/Tree/EulerTourPathQuery.py
  - DataStructure/Wavelet/PointAddRectangleSum.py
  - DataStructure/BinaryIndexedTree/inversion_number.py
  timestamp: '2021-01-02 01:05:58+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/vertex_add_path_sum.test.py
  - TestCase/LibraryChecker/vertex_add_subtree_sum.test.py
  - TestCase/LibraryChecker/point_add_range_sum.test.py
  - TestCase/AOJ/DSL_2_B.BIT.test.py
  - TestCase/AOJ/GRL_5_D.test.py
documentation_of: DataStructure/BinaryIndexedTree/PointAddRangeSum.py
layout: document
title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
---

## 使い方
`BinaryIndexedTree(n: int)`  
長さ `n` の Binary Indexed Tree を構築する。初期値はすべて `0` である。計算量 $O(n)$

- `build(array: Sequence[int]) -> None`  
Binary Indexed Tree を `array` で初期化する。計算量 $O(n)$

- `add(i: int, val: int) -> None`  
`i` 番目の要素に `val` を加える。計算量 $O(\log n)$

- `sum(l: int, r: int) -> int`  
$\lbrack l, r)$ 番目の要素の総和を返す。計算量 $O(\log n)$

- `bisect_left(val: int) -> int`  
$\lbrack 0, r)$ 番目の要素の総和が `val` 以上となる最小の $r$ を返す。そのような $r$ が存在しない場合は `n + 1` を返す。計算量 $O(\log n)$
