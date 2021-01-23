---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\0560.BIT.test.py
    title: TestCase\AOJ\0560.BIT.test.py
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
  code: "class BinaryIndexedTree:\r\n    def __init__(self, h, w):\r\n        self.h\
    \ = h\r\n        self.w = w\r\n        self.bit = [[0] * (self.w + 1) for _ in\
    \ range(self.h + 1)]\r\n\r\n    def add(self, i, j, val):\r\n        hi, wj =\
    \ i, j\r\n        i = hi + 1\r\n        while i <= self.h:\r\n            j =\
    \ wj + 1\r\n            while j <= self.w:\r\n                self.bit[i][j] +=\
    \ val\r\n                j += j & -j\r\n            i += i & -i\r\n\r\n    def\
    \ _sum(self, i, j):\r\n        s, hi, wj = 0, i, j\r\n        i = hi\r\n     \
    \   while i > 0:\r\n            j = wj\r\n            while j > 0:\r\n       \
    \         s += self.bit[i][j]\r\n                j -= j & -j\r\n            i\
    \ -= i & -i\r\n        return s\r\n\r\n    def sum(self, hl, hr, wl, wr):\r\n\
    \        \"\"\"sum of values in range [hl, hr) * [wl, wr)\"\"\"\r\n        return\
    \ self._sum(hr, wr) - self._sum(hl, wr) \\\r\n               - self._sum(hr, wl)\
    \ + self._sum(hl, wl)\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\BinaryIndexedTree\PointAddRangeSum2D.py
  requiredBy: []
  timestamp: '2021-01-02 15:25:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\0560.BIT.test.py
documentation_of: DataStructure\BinaryIndexedTree\PointAddRangeSum2D.py
layout: document
title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u77E9\u5F62\u548C\u53D6\u5F97"
---
## 使い方
`BinaryIndexedTree(h: int, w: int)`  
大きさが $h × w$ の二次元 Binary Indexed Tree を構築する。初期値はすべて $0$ である。計算量 $\mathrm{O}(hw)$
- `add(i: int, j: int, val: Any) -> None`  
$(i, j)$ 番目の要素に `val` を加える。計算量 $\mathrm{O}(\log h\log w)$
- `sum(hl: int, hr: int, wl: int, wr: int) -> Any`  
矩形範囲 $\lbrack hl, hr) × \lbrack wl, wr)$ の要素の総和を返す。計算量 $\mathrm{O}(\log h\log w)$
