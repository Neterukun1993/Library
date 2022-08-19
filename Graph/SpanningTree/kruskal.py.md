---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/UnionFind/UnionFind.py
    title: Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_2_A.kruskal.test.py
    title: TestCase/AOJ/GRL_2_A.kruskal.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "#from operator import itemgetter\nfrom standard_library.operator import itemgetter\n\
    from DataStructure.UnionFind.UnionFind import UnionFind\n\n\ndef kruskal(n, edges):\n\
    \    edges = sorted(edges, key=itemgetter(2))\n    uf = UnionFind(n)\n    res\
    \ = 0\n    for u, v, cost in edges:\n        if not uf.same(u, v):\n         \
    \   uf.merge(u, v)\n            res += cost\n    return res\n"
  dependsOn:
  - DataStructure/UnionFind/UnionFind.py
  isVerificationFile: false
  path: Graph/SpanningTree/kruskal.py
  requiredBy: []
  timestamp: '2022-01-22 12:11:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/GRL_2_A.kruskal.test.py
documentation_of: Graph/SpanningTree/kruskal.py
layout: document
title: "\u6700\u5C0F\u5168\u57DF\u6728 (\u30AF\u30E9\u30B9\u30AB\u30EB\u6CD5)"
---

## 概要
クラスカル法により最小全域木の総コストを求める。

## 使い方
`kruskal(n: int, edges: Iterable[Tuple[int, int, int]]) -> int`  
頂点数 `n` の無向グラフ $G=(V, E)$ に対して、重み付き辺集合 `edges` から構成される最小全域木の総コストを返す。計算量 $O(E\log V)$
