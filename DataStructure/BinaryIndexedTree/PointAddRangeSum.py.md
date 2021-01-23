---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure\BinaryIndexedTree\inversion_number.py
    title: DataStructure\BinaryIndexedTree\inversion_number.py
  - icon: ':heavy_check_mark:'
    path: DataStructure\Wavelet\PointAddRectangleSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u77E9\u5F62\u548C\u53D6\u5F97"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DSL_2_B.BIT.test.py
    title: TestCase\AOJ\DSL_2_B.BIT.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\GRL_5_D.test.py
    title: TestCase\AOJ\GRL_5_D.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\point_add_range_sum.test.py
    title: TestCase\LibraryChecker\point_add_range_sum.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\vertex_add_path_sum.test.py
    title: TestCase\LibraryChecker\vertex_add_path_sum.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\vertex_add_subtree_sum.test.py
    title: TestCase\LibraryChecker\vertex_add_subtree_sum.test.py
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
  code: "class BinaryIndexedTree:\r\n    def __init__(self, n):\r\n        self.size\
    \ = n\r\n        self.bit = [0] * (self.size + 1)\r\n\r\n    def build(self, array):\r\
    \n        for i, val in enumerate(array):\r\n            self.bit[i + 1] = val\r\
    \n        for i in range(1, self.size):\r\n            if i + (i & -i) > self.size:\r\
    \n                continue\r\n            self.bit[i + (i & -i)] += self.bit[i]\r\
    \n\r\n    def _sum(self, i):\r\n        s = 0\r\n        while i > 0:\r\n    \
    \        s += self.bit[i]\r\n            i -= i & -i\r\n        return s\r\n\r\
    \n    def add(self, i, val):\r\n        i += 1\r\n        while i <= self.size:\r\
    \n            self.bit[i] += val\r\n            i += i & -i\r\n\r\n    def sum(self,\
    \ l, r):\r\n        \"\"\"sum of values in range [l, r)\"\"\"\r\n        return\
    \ self._sum(r) - self._sum(l)\r\n\r\n    def bisect_left(self, val):\r\n     \
    \   \"\"\"minimum idx s.t. sum[0, idx) >= val\"\"\"\r\n        if val <= 0:\r\n\
    \            return 0\r\n        idx = 0\r\n        k = 1 << self.size.bit_length()\r\
    \n        while k:\r\n            if idx + k <= self.size and self.bit[idx + k]\
    \ < val:\r\n                val -= self.bit[idx + k]\r\n                idx +=\
    \ k\r\n            k >>= 1\r\n        return idx + 1\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\BinaryIndexedTree\PointAddRangeSum.py
  requiredBy:
  - DataStructure\BinaryIndexedTree\inversion_number.py
  - DataStructure\Wavelet\PointAddRectangleSum.py
  timestamp: '2021-01-02 01:05:58+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\DSL_2_B.BIT.test.py
  - TestCase\AOJ\GRL_5_D.test.py
  - TestCase\LibraryChecker\point_add_range_sum.test.py
  - TestCase\LibraryChecker\vertex_add_path_sum.test.py
  - TestCase\LibraryChecker\vertex_add_subtree_sum.test.py
documentation_of: DataStructure\BinaryIndexedTree\PointAddRangeSum.py
layout: document
title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
---
## 使い方
`BinaryIndexedTree(n: int)`  
長さ $n$ の Binary Indexed Tree を構築する。初期値はすべて $0$ である。計算量 $\mathrm{O}(n)$
- `build(array: List[Any]) -> None`  
Binary Indexed Tree を `array` で初期化する。計算量 $\mathrm{O}(n)$
- `add(i: int, val: Any) -> None`  
$i$ 番目の要素に `val` を加える。計算量 $\mathrm{O}(\log n)$
- `sum(l: int, r: int) -> Any`  
$\lbrack l, r)$ 番目の要素の総和を返す。計算量 $\mathrm{O}(\log n)$
- `bisect_left(val: Any) -> int`  
$\lbrack 0, r)$ 番目の要素の総和が `val` 以上となる最小の $r$ を返す。そのような $r$ が存在しない場合は $n + 1$ を返す。計算量 $\mathrm{O}(\log n)$
