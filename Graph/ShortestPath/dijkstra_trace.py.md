---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/shortest_path.test.py
    title: TestCase/LibraryChecker/shortest_path.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# from heapq import heappop, heappush\nfrom standard_library.heapq import\
    \ heappop, heappush\n\n\ndef dijkstra(start, graph):\n    INF = 10 ** 18\n   \
    \ n = len(graph)\n    dist = [INF] * n\n    dist[start] = 0\n    parent = [-1]\
    \ * n\n    q = [(0, start)]  # q = [(start\u304B\u3089\u306E\u8DDD\u96E2, \u73FE\
    \u5728\u5730)]\n    while q:\n        d, v = heappop(q)\n        if dist[v] <\
    \ d:\n            continue\n        for nxt_v, cost in graph[v]:\n           \
    \ if dist[v] + cost < dist[nxt_v]:\n                dist[nxt_v] = dist[v] + cost\n\
    \                parent[nxt_v] = v\n                heappush(q, (dist[nxt_v],\
    \ nxt_v))\n    return dist, parent\n\n\ndef trace_route(goal, parent):\n    if\
    \ parent[goal] == -1:\n        return []\n    path = []\n    v = goal\n    while\
    \ v != -1:\n        path.append(v)\n        v = parent[v]\n    return path[::-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/ShortestPath/dijkstra_trace.py
  requiredBy: []
  timestamp: '2022-01-22 18:47:07+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/shortest_path.test.py
documentation_of: Graph/ShortestPath/dijkstra_trace.py
layout: document
title: "\u30C0\u30A4\u30AF\u30B9\u30C8\u30E9\u6CD5 ($O((E + V)\\log V)$) + \u7D4C\u8DEF\
  \u5FA9\u5143"
---

## 概要
重み付き有向グラフにおける単一始点最短経路問題を解くアルゴリズム。経路復元が可能。

## 使い方
- `dijkstra(start: int, graph: Sequence[Iterable[Tuple[int, int]]]) -> Tuple[List[int], List[int]]`  
$G = (V, E)$ で表される重み付き有向グラフ `graph` に対して、`start` を始点とした単一始点最短距離の配列と、経路復元用の配列を返す。計算量 $O((E + V)\log V)$

- `trace_route(goal: int, parent: List[int]) -> List[int]`  
dijkstra 法で求めた経路復元用の配列 `parent` を用いて、終点 `goal` までの頂点経路を返す。経路の頂点数を $k$ とすると、計算量 $O(k)$