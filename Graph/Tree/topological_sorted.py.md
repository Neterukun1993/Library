---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/centroid.py
    title: "\u6728\u306E\u91CD\u5FC3"
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/dsu_on_tree.py
    title: DSU on tree
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0763.test.py
    title: TestCase/yukicoder/yuki0763.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def topological_sorted(tree, root=None):\n    n = len(tree)\n    par = [-1]\
    \ * n\n    tp_order = []\n    for v in range(n):\n        if par[v] != -1 or (root\
    \ is not None and v != root):\n            continue\n        stack = [v]\n   \
    \     while stack:\n            v = stack.pop()\n            tp_order.append(v)\n\
    \            for nxt_v in tree[v]:\n                if nxt_v == par[v]:\n    \
    \                continue\n                par[nxt_v] = v\n                stack.append(nxt_v)\n\
    \    return tp_order, par\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Tree/topological_sorted.py
  requiredBy:
  - Graph/Tree/centroid.py
  - Graph/Tree/dsu_on_tree.py
  timestamp: '2021-02-15 01:45:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki0763.test.py
documentation_of: Graph/Tree/topological_sorted.py
layout: document
title: "\u6728\u4E0A\u306E\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8"
---

## 概要
木 (もしくは森) に対してトポロジカルソートをする。木 DP を非再帰で行いたいときに使用する。

## 使い方
`topological_sorted(tree: Sequence[Iterable[int]], root: Optional[int] = None) -> Tuple[List[int], List[int]]`  
木（もしくは森）に対してトポロジカルソートを行い、トポロジカル順の配列と親頂点の配列を返す。根頂点 `root` を指定しない場合は、未訪問の頂点すべてに対してトポロジカルソートを行う。計算量 $O(V)$
