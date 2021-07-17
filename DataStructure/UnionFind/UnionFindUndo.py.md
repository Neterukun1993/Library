---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure/UnionFind/OfflineDynamicConnectivity.py
    title: Offline Dynamic Connectivity
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/persistent_unionfind.Undo.test.py
    title: TestCase/LibraryChecker/persistent_unionfind.Undo.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class UnionFindUndo:\n    def __init__(self, n):\n        self.parent = [-1]\
    \ * n\n        self.history = []\n\n    def root(self, x):\n        if self.parent[x]\
    \ < 0:\n            return x\n        else:\n            return self.root(self.parent[x])\n\
    \n    def merge(self, x, y):\n        x = self.root(x)\n        y = self.root(y)\n\
    \        self.history.append((x, self.parent[x]))\n        self.history.append((y,\
    \ self.parent[y]))\n        if x == y:\n            return False\n        if self.parent[x]\
    \ > self.parent[y]:\n            x, y = y, x\n        self.parent[x] += self.parent[y]\n\
    \        self.parent[y] = x\n        return True\n\n    def undo(self):\n    \
    \    if not self.history:\n            return False\n        for _ in range(2):\n\
    \            x, par_x = self.history.pop()\n            self.parent[x] = par_x\n\
    \        return True\n\n    def same(self, x, y):\n        return self.root(x)\
    \ == self.root(y)\n\n    def size(self, x):\n        return -self.parent[self.root(x)]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/UnionFind/UnionFindUndo.py
  requiredBy:
  - DataStructure/UnionFind/OfflineDynamicConnectivity.py
  timestamp: '2021-01-03 22:00:08+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/persistent_unionfind.Undo.test.py
documentation_of: DataStructure/UnionFind/UnionFindUndo.py
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
