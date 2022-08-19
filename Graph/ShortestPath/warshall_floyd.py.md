---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_1_C.test.py
    title: TestCase/AOJ/GRL_1_C.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def warshall_floyd(matrix):\n    n = len(matrix)\n    dist = [[d for d in\
    \ row] for row in matrix]\n    for k in range(n):\n        for i in range(n):\n\
    \            for j in range(n):\n                dist[i][j] = min(dist[i][j],\
    \ dist[i][k] + dist[k][j])\n    return dist\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/ShortestPath/warshall_floyd.py
  requiredBy: []
  timestamp: '2021-01-15 11:26:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/GRL_1_C.test.py
documentation_of: Graph/ShortestPath/warshall_floyd.py
layout: document
title: "\u30EF\u30FC\u30B7\u30E3\u30EB\u30D5\u30ED\u30A4\u30C9\u6CD5"
---

## 概要
重み付き有向グラフにおける全点対最短距離問題を解くアルゴリズム。各辺の重みは負でもよい。

## 使い方
`warshall_floyd(matrix: Sequence[Sequence[int]]) -> List[List[int]]`  
隣接行列 `matrix` で表現されるグラフ上での、全点対最短距離の配列を返す。計算量 $O(V^3)$

## 備考
- 頂点 $u$ が負閉路に含まれるとき、$u$ - $u$ 間の最短距離 `distance[u][u]` が負になる。
- ある辺を既存の辺より小さいコストの辺に変更するとき、$O(V^2)$ で更新ができる。[ARC035-C](https://atcoder.jp/contests/arc035/tasks/arc035_c)
