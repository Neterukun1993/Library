---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DSL_2_E.test.py
    title: TestCase\AOJ\DSL_2_E.test.py
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
    \n                continue\r\n            self.bit[i] -= self.bit[i + (i & -i)]\r\
    \n\r\n    def __getitem__(self, i):\r\n        i = i + 1\r\n        s = 0\r\n\
    \        while i <= self.size:\r\n            s += self.bit[i]\r\n           \
    \ i += i & -i\r\n        return s\r\n\r\n    def _add(self, i, val):\r\n     \
    \   while i > 0:\r\n            self.bit[i] += val\r\n            i -= i & -i\r\
    \n\r\n    def add(self, l, r, val):\r\n        \"\"\"add value in range [l, r)\"\
    \"\"\r\n        self._add(r, val)\r\n        self._add(l, -val)\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\BinaryIndexedTree\RangeAddPointGet.py
  requiredBy: []
  timestamp: '2021-01-02 01:31:17+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\DSL_2_E.test.py
documentation_of: DataStructure\BinaryIndexedTree\RangeAddPointGet.py
layout: document
title: "\u533A\u9593\u52A0\u7B97\u30FB\u4E00\u70B9\u53D6\u5F97"
---
## 使い方
`BinaryIndexedTree(n: int)`  
長さ $n$ の Binary Indexed Tree を構築する。初期値はすべて $0$ である。計算量 $\mathrm{O}(n)$
- `build(array: List[Any]) -> None`  
Binary Indexed Tree を `array` で初期化する。計算量 $\mathrm{O}(n)$
- `__getitem__(i: int) -> Any`  
$i$ 番目の要素を返す。計算量 $\mathrm{O}(\log n)$
- `add(l: int, r: int, val: Any) -> None`  
$\lbrack l, r)$ 番目の要素それぞれに `val` を加える。計算量 $\mathrm{O}(\log n)$
