---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0416.test.py
    title: TestCase/yukicoder/yuki0416.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from bisect import bisect_left\n\n\nclass PartiallyPersistentUnionFind:\n\
    \    def __init__(self, n):\n        self.INF = 10 ** 9\n        self.parent =\
    \ [-1] * n\n        self.time = [self.INF] * n\n        self.size = [[(-1, -1)]\
    \ for i in range(n)]\n\n    def root(self, t, x):\n        while self.time[x]\
    \ <= t:\n            x = self.parent[x]\n        return x\n\n    def merge(self,\
    \ t, x, y):\n        x = self.root(t, x)\n        y = self.root(t, y)\n      \
    \  if x == y:\n            return False\n        if self.parent[x] > self.parent[y]:\n\
    \            x, y = y, x\n        self.parent[x] += self.parent[y]\n        self.size[x].append((t,\
    \ self.parent[x]))\n        self.parent[y] = x\n        self.time[y] = t\n   \
    \     return True\n\n    def same(self, t, x, y):\n        return self.root(t,\
    \ x) == self.root(t, y)\n\n    def size(self, t, x):\n        x = self.root(t,\
    \ x)\n        idx = bisect_left(self.size[x], (t, self.INF)) - 1\n        return\
    \ -self.size[x][idx][1]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/UnionFind/PartiallyPersistentUnionFind.py
  requiredBy: []
  timestamp: '2021-01-10 07:28:54+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki0416.test.py
documentation_of: DataStructure/UnionFind/PartiallyPersistentUnionFind.py
layout: document
title: "\u90E8\u5206\u6C38\u7D9A Union Find"
---

## 概要
素集合を管理するデータ構造。過去の状態における `same` と `size` の操作をサポートする。

## 使い方
`PartiallyPersistentUnionFind(n: int)`  
$x = 0, 1, 2, \dots, n - 1$ に対して要素 $x$ の代表元が $x$ となるように、$n$ 個の素集合を構築する。計算量 $O(n)$

- `root(t: int, x: int) -> int`  
時刻 $t$ における、要素 $x$ の代表元を返す。計算量 $O(\log n)$

- `merge(t: int, x: int, y: int) -> bool`  
時刻 $t$ において、要素 $x$ を含む集合と要素 $y$ を含む集合を併合する。**時刻 $t$ は、最後に `merge` を行ったときの時刻 $t_{\mathrm{last}}$ よりも大きくすること！** 併合に成功した場合は `True` を、失敗した場合（既に併合済みだった場合）は `False` を返す。計算量 $O(\log n)$

- `same(t: int, x: int, y: int) -> bool`  
時刻 $t$ において、要素 $x$ と要素 $y$ が同じ集合に属するかどうかを返す。計算量 $O(\log n)$

- `size(t: int, x: int) -> int`  
時刻 $t$ における、要素 $x$ を含む集合の大きさを返す。計算量 $O(\log n)$
