---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_1_A.EnumerableUnionFind.test.py
    title: TestCase/AOJ/DSL_1_A.EnumerableUnionFind.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/EnumerableUnionFind.unittest.test.py
    title: TestCase/unittest/EnumerableUnionFind.unittest.test.py
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
  code: "class EnumerableUnionFind:\n    def __init__(self, n):\n        self.next\
    \ = [i for i in range(n)]\n        self.parent = [-1] * n\n        self.n = n\n\
    \        self.cnt = n\n\n    def root(self, x):\n        if self.parent[x] < 0:\n\
    \            return x\n        else:\n            self.parent[x] = self.root(self.parent[x])\n\
    \            return self.parent[x]\n\n    def merge(self, x, y):\n        root_x\
    \ = self.root(x)\n        root_y = self.root(y)\n        if root_x == root_y:\n\
    \            return False\n        self.next[x], self.next[y] = self.next[y],\
    \ self.next[x]\n        if self.parent[root_x] > self.parent[root_y]:\n      \
    \      x, y = y, x\n        self.parent[root_x] += self.parent[root_y]\n     \
    \   self.parent[root_y] = root_x\n        self.cnt -= 1\n        return True\n\
    \n    def same(self, x, y):\n        return self.root(x) == self.root(y)\n\n \
    \   def size(self, x):\n        return -self.parent[self.root(x)]\n\n    def count(self):\n\
    \        return self.cnt\n\n    def enumerate(self, x):\n        res = []\n  \
    \      init_x = x\n        while True:\n            res.append(x)\n          \
    \  x = self.next[x]\n            if x == init_x:\n                break\n    \
    \    return res\n\n    def groups(self):\n        res = [[] for _ in range(self.n)]\n\
    \        for i in range(self.n):\n            res[self.root(i)].append(i)\n  \
    \      return [group for group in res if group]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/UnionFind/EnumerableUnionFind.py
  requiredBy: []
  timestamp: '2022-08-20 05:25:06+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/unittest/EnumerableUnionFind.unittest.test.py
  - TestCase/AOJ/DSL_1_A.EnumerableUnionFind.test.py
documentation_of: DataStructure/UnionFind/EnumerableUnionFind.py
layout: document
title: Enumerable Union Find
---

## 概要
素集合を管理するデータ構造。ある要素を含む集合に対して、全要素の列挙が線形時間で可能。

## 使い方
`EnumerableUnionFind(n: int)`  
$x = 0, 1, 2, \dots, n - 1$ に対して要素 $x$ の代表元が $x$ となるように、$n$ 個の素集合を構築する。計算量 $O(n)$

- `root(x: int) -> int`  
要素 $x$ の代表元を返す。計算量 $\mathrm{amortized}\ O(\alpha (n))$

- `merge(x: int, y: int) -> bool`  
要素 $x$ を含む集合と要素 $y$ を含む集合を併合する。併合に成功した場合は `True` を、失敗した場合（既に併合済みだった場合）は `False` を返す。計算量 $\mathrm{amortized}\ O(\alpha (n))$

- `same(x: int, y: int) -> bool`  
要素 $x$ と要素 $y$ が同じ集合に属するかどうかを返す。計算量 $\mathrm{amortized}\ O(\alpha (n))$

- `size(x: int) -> int`  
要素 $x$ を含む集合の大きさを返す。計算量 $\mathrm{amortized}\ O(\alpha (n))$

- `count() -> int`  
集合の個数を返す。計算量 $O(1)$

- `enumerate(x: int) -> List[int]`  
要素 $x$ を含む集合の全要素を列挙する。要素数を $k$ とすると、計算量 $O(k)$

- `groups() -> List[List[int]]`  
すべての集合とその要素を列挙する。計算量 $O(n)$

## 参考
[素集合の要素の列挙と併合 (単方向循環リスト) - noshi91のメモ](https://noshi91.hatenablog.com/entry/2019/07/19/180606)
