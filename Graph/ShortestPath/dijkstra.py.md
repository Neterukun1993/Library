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
  code: "# from heapq import heappop, heappush\nfrom heapq import heappop, heappush\n\
    \n\ndef dijkstra(start, graph):\n    INF = 10 ** 18\n    n = len(graph)\n    dist\
    \ = [INF] * n\n    dist[start] = 0\n    q = [(0, start)]  # q = [(start\u304B\u3089\
    \u306E\u8DDD\u96E2, \u73FE\u5728\u5730)]\n    while q:\n        d, v = heappop(q)\n\
    \        if dist[v] < d:\n            continue\n        for nxt_v, cost in graph[v]:\n\
    \            if dist[v] + cost < dist[nxt_v]:\n                dist[nxt_v] = dist[v]\
    \ + cost\n                heappush(q, (dist[nxt_v], nxt_v))\n    return dist\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/ShortestPath/dijkstra.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/ShortestPath/dijkstra.py
layout: document
title: "\u30C0\u30A4\u30AF\u30B9\u30C8\u30E9\u6CD5 ($O((E + V)\\log V)$)"
---

## 概要
重み付き有向グラフにおける単一始点最短経路問題を解くアルゴリズム。

## 使い方
`dijkstra(start: int, graph: Sequence[Iterable[Tuple[int, int]]]) -> List[int]`  
$G = (V, E)$ で表される重み付き有向グラフ `graph` に対して、`start` を始点とした単一始点最短距離の配列を返す。計算量 $O((E + V)\log V)$