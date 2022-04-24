---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_1_B.test.py
    title: TestCase/AOJ/DSL_1_B.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class UnionFindWithPotential:\n    def __init__(self, n):\n        self.parent\
    \ = [-1] * n\n        self.pot = [0] * n\n        self.cnt = n\n        self.INF\
    \ = 10 ** 18\n\n    def root(self, x):\n        if self.parent[x] < 0:\n     \
    \       return x\n        rt = self.root(self.parent[x])\n        self.pot[x]\
    \ += self.pot[self.parent[x]]\n        self.parent[x] = rt\n        return rt\n\
    \n    def merge(self, x, y, potential):\n        \"\"\"merge x and y in pot[x]\
    \ = pot[y] + potential\"\"\"\n        root_x = self.root(x)\n        root_y =\
    \ self.root(y)\n        if root_x == root_y:\n            return False\n     \
    \   if self.parent[root_x] < self.parent[root_y]:\n            self.parent[root_x]\
    \ += self.parent[root_y]\n            self.parent[root_y] = root_x\n         \
    \   self.pot[root_y] = -potential + self.pot[x] - self.pot[y]\n        else:\n\
    \            self.parent[root_y] += self.parent[root_x]\n            self.parent[root_x]\
    \ = root_y\n            self.pot[root_x] = potential - self.pot[x] + self.pot[y]\n\
    \        self.cnt -= 1\n        return True\n\n    def same(self, x, y):\n   \
    \     return self.root(x) == self.root(y)\n\n    def diff(self, x, y):\n     \
    \   \"\"\"get x's potential on a reference point y\"\"\"\n        if not self.same(x,\
    \ y):\n            # potential is not defined between x and y\n            return\
    \ self.INF\n        return self.pot[x] - self.pot[y]\n\n    def size(self, x):\n\
    \        return -self.parent[self.root(x)]\n\n    def count(self):\n        return\
    \ self.cnt\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/UnionFind/UnionFindWithPotential.py
  requiredBy: []
  timestamp: '2021-01-02 02:52:46+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_1_B.test.py
documentation_of: DataStructure/UnionFind/UnionFindWithPotential.py
layout: document
title: "\u30DD\u30C6\u30F3\u30B7\u30E3\u30EB\u4ED8\u304D Union Find"
---

## 概要
素集合を管理するデータ構造。同じ素集合に属する $2$ つの要素間のポテンシャルも同時に管理する。

## 使い方
`UnionFindWithPotential(n: int)`  
$x = 0, 1, 2, \dots, n - 1$ に対して要素 $x$ の代表元が $x$ となるように、$n$ 個の素集合を構築する。各要素間のポテンシャルは未定義 (つまり `INF`) とする。計算量 $O(n)$

- `root(x: int) -> int`  
要素 $x$ の代表元を返す。計算量 $\mathrm{amortized}\ O(\alpha (n))$

- `merge(x: int, y: int, potential: int) -> bool`  
要素 $x$ を含む集合と要素 $y$ を含む集合を併合する。要素 $x$ のポテンシャルは要素 $y$ よりも `potential` ほど高い。併合に成功した場合は `True` を、失敗した場合（既に併合済みだった場合）は `False` を返す。計算量 $\mathrm{amortized}\ O(\alpha (n))$

- `same(x: int, y: int) -> bool`  
要素 $x$ と要素 $y$ が同じ集合に属するかどうかを返す。計算量 $\mathrm{amortized}\ O(\alpha (n))$

- `diff(x: int, y: int) -> int`  
要素 $x$ と要素 $y$ のポテンシャル差を返す。ポテンシャルが未定義 (つまり要素 $x$ と要素 $y$ が同じ集合に属していない場合) は `INF` を返す。$\mathrm{amortized}\ O(\alpha (n))$

- `size(x: int) -> int`  
要素 $x$ を含む集合の大きさを返す。計算量 $\mathrm{amortized}\ O(\alpha (n))$

- `count() -> int`  
集合の個数を返す。計算量 $O(1)$
