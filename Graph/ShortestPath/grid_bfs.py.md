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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\n\n\ndef grid_bfs(grid, si, sj, wall=\"#\"\
    ):\n    INF = 10 ** 18\n    d = ((1, 0), (-1, 0), (0, 1), (0, -1))\n    h, w =\
    \ len(grid), len(grid[0])\n    dist = [[INF] * w for i in range(h)]\n    dist[si][sj]\
    \ = 0\n    que = deque([(si, sj)])\n    while que:\n        i, j = que.popleft()\n\
    \        for di, dj in d:\n            nxt_i, nxt_j = i + di, j + dj\n       \
    \     if not(0 <= nxt_i < h and 0 <= nxt_j < w):\n                continue\n \
    \           if grid[nxt_i][nxt_j] == wall:\n                continue\n       \
    \     if dist[nxt_i][nxt_j] != INF:\n                continue\n            dist[nxt_i][nxt_j]\
    \ = dist[i][j] + 1\n            que.append((nxt_i, nxt_j))\n    return dist\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/ShortestPath/grid_bfs.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/ShortestPath/grid_bfs.py
layout: document
title: "\u30B0\u30EA\u30C3\u30C9\u4E0A\u306EBFS"
---

## 概要
二次元グリッドグラフ上の単一始点最短経路問題を解くアルゴリズム。

## 使い方
`bfs(grid: Sequence[str], si: int, sj: int, wall: str) -> List[List[int]]`  
グリッドグラフ `grid` 上での、`(si, sj)` を始点とした単一始点最短距離の配列を返す。グリッドグラフの大きさを `h * w` としたとき、計算量 $O(hw)$
