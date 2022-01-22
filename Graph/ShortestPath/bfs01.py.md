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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# from collections import deque\nfrom standard_library.collections import\
    \ deque\n\n\ndef bfs01(graph, start):\n    INF = 10 ** 18\n    n = len(graph)\n\
    \    dist = [INF] * n\n    dist[start] = 0\n    que = deque([start])\n    while\
    \ que:\n        v = que.popleft()\n        for nxt_v, cost in graph[v]:\n    \
    \        d = dist[v] + cost\n            if d < dist[nxt_v]:\n               \
    \ dist[nxt_v] = d\n                if cost == 0:\n                    que.appendleft(nxt_v)\n\
    \                else:\n                    que.append(nxt_v)\n    return dist\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/ShortestPath/bfs01.py
  requiredBy: []
  timestamp: '2022-01-22 12:11:49+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/ShortestPath/bfs01.py
layout: document
title: 01-BFS
---

## 概要
各辺の長さが $0$ または $1$ の有向グラフ上で、単一始点最短経路問題を解くアルゴリズム。

## 使い方
`bfs(graph: Sequence[Sequence[Tuple[int, int]]], start: int) -> List[int]`  
重み付き有向グラフ `graph` 上での、 `start` を始点とした単一始点最短距離の配列を返す。ただし、重みは $0$ または $1$ のどちらかでなければならないことに注意。計算量 $O(V + E)$

## 参考
・[01-BFSのちょっと丁寧な解説 - ARMERIA](https://betrue12.hateblo.jp/entry/2018/12/08/000020)
