---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/Tree/topological_sorted.py
    title: "\u6728\u4E0A\u306E\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8"
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
  code: "from Graph.Tree.topological_sorted import topological_sorted\n\n\ndef centroid(tree):\n\
    \    n = len(tree)\n    tp_order, par = topological_sorted(tree)\n    sub_size\
    \ = [0] * n\n    res = []\n    for v in tp_order[::-1]:\n        is_centroid =\
    \ True\n        sub_size[v] = 1\n        for nxt_v in tree[v]:\n            if\
    \ nxt_v == par[v]:\n                continue\n            if sub_size[nxt_v] >\
    \ n // 2:\n                is_centroid = False\n            sub_size[v] += sub_size[nxt_v]\n\
    \        if is_centroid and n - sub_size[v] <= n // 2:\n            res.append(v)\n\
    \    return res\n"
  dependsOn:
  - Graph/Tree/topological_sorted.py
  isVerificationFile: false
  path: Graph/Tree/centroid.py
  requiredBy: []
  timestamp: '2021-02-16 00:44:23+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/Tree/centroid.py
layout: document
title: "\u6728\u306E\u91CD\u5FC3"
---

## 概要
木の重心を求めるアルゴリズム。重心は最大で 2 つ存在する。木の代わりに森を与えた場合はバグるので注意。

## 使い方
`centroid(tree) -> List[int]`  
木の重心を格納した配列を返す。計算量 $O(V)$
