---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: Graph/SpanningTree/boruvka.py
    title: "\u6700\u5C0F\u5168\u57DF\u6728 (\u30D6\u30EB\u30FC\u30D5\u30AB\u6CD5)"
  - icon: ':heavy_check_mark:'
    path: Graph/SpanningTree/directed_mst.py
    title: "\u6700\u5C0F\u6709\u5411\u5168\u57DF\u6728"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/2821.test.py
    title: TestCase/AOJ/2821.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_1_A.test.py
    title: TestCase/AOJ/DSL_1_A.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0922.HLDecomposition.test.py
    title: TestCase/yukicoder/yuki0922.HLDecomposition.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0922.test.py
    title: TestCase/yukicoder/yuki0922.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class UnionFind:\n    def __init__(self, n):\n        self.parent = [-1]\
    \ * n\n        self.n = n\n        self.cnt = n\n\n    def root(self, x):\n  \
    \      if self.parent[x] < 0:\n            return x\n        else:\n         \
    \   self.parent[x] = self.root(self.parent[x])\n            return self.parent[x]\n\
    \n    def merge(self, x, y):\n        x = self.root(x)\n        y = self.root(y)\n\
    \        if x == y:\n            return False\n        if self.parent[x] > self.parent[y]:\n\
    \            x, y = y, x\n        self.parent[x] += self.parent[y]\n        self.parent[y]\
    \ = x\n        self.cnt -= 1\n        return True\n\n    def same(self, x, y):\n\
    \        return self.root(x) == self.root(y)\n\n    def size(self, x):\n     \
    \   return -self.parent[self.root(x)]\n\n    def count(self):\n        return\
    \ self.cnt\n\n    def groups(self):\n        res = [[] for _ in range(self.n)]\n\
    \        for i in range(self.n):\n            res[self.root(i)].append(i)\n  \
    \      return [group for group in res if group]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/UnionFind/UnionFind.py
  requiredBy:
  - Graph/SpanningTree/directed_mst.py
  - Graph/SpanningTree/boruvka.py
  timestamp: '2021-01-02 02:09:18+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki0922.HLDecomposition.test.py
  - TestCase/yukicoder/yuki0922.test.py
  - TestCase/AOJ/2821.test.py
  - TestCase/AOJ/DSL_1_A.test.py
documentation_of: DataStructure/UnionFind/UnionFind.py
layout: document
title: Union Find
---
## 使い方
`UnionFind(n: int)`  
$x = 0, 1, 2, \dots, n - 1$ に対して要素 $x$ の代表元が $x$ となるように、 $n$ 個の素集合を構築する。計算量 $\mathrm{O}(n)$

- `root(x: int) -> int`  
要素 $x$ の代表元を返す。計算量 $\mathrm{amortized}\ \mathrm{O}(\alpha (n))$

- `merge(x: int, y: int) -> bool`  
要素 $x$ を含む集合と要素 $y$ を含む集合を併合する。成功した場合は `True` を、失敗した場合（既に併合済みだった場合）は `False` を返す。計算量 $\mathrm{amortized}\ \mathrm{O}(\alpha (n))$

- `same(x: int, y: int) -> bool`  
要素 $x, y$ が同じ集合に属するかどうかを返す。計算量 $\mathrm{amortized}\ \mathrm{O}(\alpha (n))$

- `size(x: int) -> int`  
要素 $x$ を含む集合の大きさを返す。計算量 $\mathrm{amortized}\ \mathrm{O}(\alpha (n))$

- `count() -> int`  
集合の個数を返す。計算量 $\mathrm{O}(1))$

- `groups() -> List[List[int]]`  
すべての集合とその要素を列挙する。計算量 $\mathrm{O}(n)$
