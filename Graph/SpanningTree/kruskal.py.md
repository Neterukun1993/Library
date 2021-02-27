---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from operator import itemgetter\nfrom DataStructure.UnionFind.UnionFind import\
    \ UnionFind\n\n\ndef kruskal(n, edges):\n    edges = sorted(edges, key=itemgetter(2))\n\
    \    uf = UnionFind(n)\n    res = 0\n    for u, v, cost in edges:\n        if\
    \ not uf.same(u, v):\n            uf.merge(u, v)\n            res += cost\n  \
    \  return res\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/SpanningTree/kruskal.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/SpanningTree/kruskal.py
layout: document
title: "\u6700\u5C0F\u5168\u57DF\u6728 (\u30AF\u30E9\u30B9\u30AB\u30EB\u6CD5)"
---

## 概要
クラスカル法により最小全域木の総コストを求める。

## 使い方
`prim(graph: Sequence[Iterable[Tuple[int, int]]]) -> int`  
隣接リストで表現される無向グラフ `graph` に対して、最小全域木の総コストを返す。計算量 $O(E\log V)$
