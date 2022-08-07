---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/BinaryIndexedTree/PointAddRangeSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/EulerTour.py
    title: "\u30AA\u30A4\u30E9\u30FC\u30C4\u30A2\u30FC"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/vertex_add_path_sum.EulerTourPathQuery.test.py
    title: TestCase/LibraryChecker/vertex_add_path_sum.EulerTourPathQuery.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.BinaryIndexedTree.PointAddRangeSum import BinaryIndexedTree\n\
    from Graph.Tree.EulerTour import EulerTour\n\n\nclass EulerTourPathQuery(EulerTour):\n\
    \    def __init__(self, tree):\n        super().__init__(tree, root=0)\n     \
    \   self.n = len(tree)\n        self.bit = BinaryIndexedTree(2 * self.n)\n\n \
    \   def build(self, vals):\n        array = [0] * (2 * self.n)\n        for i,\
    \ idx in enumerate(self.begin):\n            array[idx] = vals[i]\n        for\
    \ i, idx in enumerate(self.end):\n            array[idx] = -vals[i]\n        self.bit.build(array)\n\
    \n    def add(self, v, val):\n        self.bit.add(self.begin[v], val)\n     \
    \   self.bit.add(self.end[v], -val)\n\n    def vertex_path_sum(self, u, v):\n\
    \        lca_uv = self.lca(u, v)\n        res = self.bit.sum(self.begin[lca_uv],\
    \ self.begin[u] + 1) \\\n            + self.bit.sum(self.begin[lca_uv] + 1, self.begin[v]\
    \ + 1)\n        return res\n\n    def edge_path_sum(self, u, v):\n        lca_uv\
    \ = self.lca(u, v)\n        res = self.bit.sum(self.begin[lca_uv] + 1, self.begin[u]\
    \ + 1) \\\n            + self.bit.sum(self.begin[lca_uv] + 1, self.begin[v] +\
    \ 1)\n        return res\n"
  dependsOn:
  - Graph/Tree/EulerTour.py
  - DataStructure/BinaryIndexedTree/PointAddRangeSum.py
  isVerificationFile: false
  path: Graph/Tree/EulerTourPathQuery.py
  requiredBy: []
  timestamp: '2021-06-15 21:41:12+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/vertex_add_path_sum.EulerTourPathQuery.test.py
documentation_of: Graph/Tree/EulerTourPathQuery.py
layout: document
title: "\u30AA\u30A4\u30E9\u30FC\u30C4\u30A2\u30FC (\u30D1\u30B9\u306B\u5BFE\u3059\
  \u308B\u30AF\u30A8\u30EA)"
---

## 概要
オイラーツアーを行い、パスに対する一点加算、区間和取得を行うアルゴリズム。

## 使い方
`EulerTourPathQuery(tree: Sequence[Iterable[int]])`  
隣接リストで表現される木 `tree` に対してオイラーツアーを行う。同時に一点加算、区間和取得用の Binary Indexed Tree を初期構築する。計算量 $O(V\log V)$

- `lca(u: int, v: int) -> int`  
頂点 `u` と頂点 `v` の最小共通祖先を返す。計算量 $O(1)$

- `distance(u: int, v: int) -> int`  
パス `u - v` の距離を返す。計算量 $O(1)$

- `build(vals: Sequence[int]) -> None`  
頂点 `v` に対する値 `vals[v]` を格納した配列について Binary Indexed Tree を初期構築する。

- `add(u: int, val: int) -> int`  
頂点 `u` に値 `val` を加算する。計算量 $O(\log V)$

- `vertex_path_sum(u: int, v: int) -> int`  
パス `u - v` 上の頂点の値の総和を返す。計算量 $O(V\log V)$

- `edge_path_sum(u: int, v: int) -> int`  
パス `u - v` 上の辺の値の総和を返す。計算量 $O(V\log V)$`
