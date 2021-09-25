---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/misc/PersistentArray.py
    title: "\u6C38\u7D9A\u914D\u5217"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/persistent_unionfind.test.py
    title: TestCase/LibraryChecker/persistent_unionfind.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.misc.PersistentArray import (\n    PersistentArray,\n\
    \    init_persistent_array\n)\n\n\nclass PersistentUnionFind:\n    def __init__(self,\
    \ n):\n        if type(n) is int:\n            self.parent = init_persistent_array([-1\
    \ for _ in range(n)])\n        else:\n            self.parent = n\n\n    def root(self,\
    \ x):\n        px = self.parent.get(x)\n        if px < 0:\n            return\
    \ x\n        return self.root(px)\n\n    def merge(self, x, y):\n        x, y\
    \ = self.root(x), self.root(y)\n        if x == y:\n            return self\n\
    \        px = self.parent.get(x)\n        py = self.parent.get(y)\n        if\
    \ px > py:\n            x, y = y, x\n        tmp = self.parent.set(y, x)\n   \
    \     return PersistentUnionFind(tmp.set(x, px + py))\n\n    def same(self, x,\
    \ y):\n        return self.root(x) == self.root(y)\n\n    def size(self, x):\n\
    \        return -self.parent.get(self.root(x))\n"
  dependsOn:
  - DataStructure/misc/PersistentArray.py
  isVerificationFile: false
  path: DataStructure/UnionFind/PersistentUnionFind.py
  requiredBy: []
  timestamp: '2021-07-18 20:19:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/persistent_unionfind.test.py
documentation_of: DataStructure/UnionFind/PersistentUnionFind.py
layout: document
title: "\u6C38\u7D9A Union Find"
---

## 概要
永続化された素集合データ構造。つまり、`merge` 前後のバージョンを常に保持し、全バージョンに対する `same`、`size` が可能である。

## 使い方
`PersistentUnionFind(n: int)`  
$x = 0, 1, 2, \dots, n - 1$ に対して要素 $x$ の代表元が $x$ となるように、$n$ 個の素集合を構築する。計算量 $O(n \log n)$

- `root(x: int) -> int`  
要素 $x$ の代表元を返す。算量 $O(\log n)$

- `merge(x: int, y: int) -> PersistentUnionFind`  
要素 $x$ を含む集合と要素 $y$ を含む集合を併合したときの `PersistentUnionFind` を返す。計算量 $O(\log n)$

- `same(x: int, y: int) -> bool`  
要素 $x$ と要素 $y$ が同じ集合に属するかどうかを返す。計算量 $O(\log n)$

- `size(x: int) -> int`  
集合の個数を返す。計算量 $O(\log n)$
