---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_4_B.test.py
    title: TestCase/AOJ/GRL_4_B.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def topological_sorted(digraph):\n    def dfs(v):\n        if not visited[v]:\n\
    \            for nxt_v in digraph[v]:\n                dfs(nxt_v)\n          \
    \  visited[v] = True\n            tp_order.append(v)\n\n    n = len(digraph)\n\
    \    visited = [False] * n\n    tp_order = []\n    for v in range(n):\n      \
    \  dfs(v)\n\n    return tp_order[::-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/misc/topological_sorted_dfs.py
  requiredBy: []
  timestamp: '2021-02-15 02:48:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/GRL_4_B.test.py
documentation_of: Graph/misc/topological_sorted_dfs.py
layout: document
title: "\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8 (\u6DF1\u3055\u512A\
  \u5148\u63A2\u7D22)"
---

## 概要
有向グラフに対してトポロジカルソートをする。グラフが巡回するときは未定義。

## 使い方
`topological_sorted(digraph: Sequence[Sequence[int]]) -> List[int]`  
有向グラフに対してトポロジカルソートを行い、トポロジカル順の配列を返す。グラフが巡回ときのトポロジカル順は未定義。計算量 $O(V + E)$
