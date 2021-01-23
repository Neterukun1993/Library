---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure\UnionFind\OfflineDynamicConnectivity.py
    title: Offline Dynamic Connectivity
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\persistent_unionfind.Undo.test.py
    title: TestCase\LibraryChecker\persistent_unionfind.Undo.test.py
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
  code: "class UnionFindUndo:\r\n    def __init__(self, n):\r\n        self.parent\
    \ = [-1] * n\r\n        self.history = []\r\n\r\n    def root(self, x):\r\n  \
    \      if self.parent[x] < 0:\r\n            return x\r\n        else:\r\n   \
    \         return self.root(self.parent[x])\r\n\r\n    def merge(self, x, y):\r\
    \n        x = self.root(x)\r\n        y = self.root(y)\r\n        self.history.append((x,\
    \ self.parent[x]))\r\n        self.history.append((y, self.parent[y]))\r\n   \
    \     if x == y:\r\n            return False\r\n        if self.parent[x] > self.parent[y]:\r\
    \n            x, y = y, x\r\n        self.parent[x] += self.parent[y]\r\n    \
    \    self.parent[y] = x\r\n        return True\r\n\r\n    def undo(self):\r\n\
    \        if not self.history:\r\n            return False\r\n        for _ in\
    \ range(2):\r\n            x, par_x = self.history.pop()\r\n            self.parent[x]\
    \ = par_x\r\n        return True\r\n\r\n    def same(self, x, y):\r\n        return\
    \ self.root(x) == self.root(y)\r\n\r\n    def size(self, x):\r\n        return\
    \ -self.parent[self.root(x)]\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\UnionFind\UnionFindUndo.py
  requiredBy:
  - DataStructure\UnionFind\OfflineDynamicConnectivity.py
  timestamp: '2021-01-03 22:00:08+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\LibraryChecker\persistent_unionfind.Undo.test.py
documentation_of: DataStructure\UnionFind\UnionFindUndo.py
layout: document
title: "\u5DFB\u304D\u623B\u3057\u53EF\u80FDUnion Find"
---
## 使い方
`UnionFind(n: int)`  
$x = 0, 1, 2, \dots, n - 1$ に対して要素 $x$ の代表元が $x$ となるように、 $n$ 個の素集合を構築する。計算量 $\mathrm{O}(n)$

- `root(x: int) -> int`  
要素 $x$ の代表元を返す。計算量 $\mathrm{O}(\log n)$

- `merge(x: int, y: int) -> bool`  
要素 $x$ を含む集合と要素 $y$ を含む集合を併合する。成功した場合は `True` を、失敗した場合（既に併合済みだった場合）は `False` を返す。計算量 $\mathrm{O}(\log n)$

- `undo() -> None`  
直前に実行した `merge` 操作を1回分巻き戻す。計算量 $\mathrm{O}(1)$

- `same(x: int, y: int) -> bool`  
要素 $x, y$ が同じ集合に属するかどうかを返す。計算量 $\mathrm{O}(\log n)$

- `size(x: int) -> int`  
要素 $x$ を含む集合の大きさを返す。計算量 $\mathrm{O}(\log n)$
