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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from collections import deque\n\n\ndef bfs(graph, start):\n    INF = 10 **\
    \ 18\n    n = len(graph)\n    dist = [INF] * n\n    dist[start] = 0\n    que =\
    \ deque([start])\n    while que:\n        v = que.popleft()\n        for nxt_v\
    \ in graph[v]:\n            if dist[nxt_v] == INF:\n                dist[nxt_v]\
    \ = dist[v] + 1\n                que.append(nxt_v)\n    return dist\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/ShortestPath/bfs.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/ShortestPath/bfs.py
layout: document
title: BFS
---
## 使い方
`bfs(graph: Sequence[Sequence[int]], start: int) -> List[int]`  
各辺の長さが `1` のグラフ `graph` 上での、 `start` を始点とした単一始点最短距離の配列を返す。計算量 $O(V + E)$
