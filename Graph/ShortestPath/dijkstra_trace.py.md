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
  code: "import heapq\n\n\ndef dijkstra(start, graph):\n    INF = 10 ** 18\n    n\
    \ = len(graph)\n    dist = [INF] * n\n    dist[start] = 0\n    parent = [-1] *\
    \ n\n    q = [(0, start)]  # q = [(start\u304B\u3089\u306E\u8DDD\u96E2, \u73FE\
    \u5728\u5730)]\n    while q:\n        d, v = heapq.heappop(q)\n        if dist[v]\
    \ < d:\n            continue\n        for nxt_v, cost in graph[v]:\n         \
    \   if dist[v] + cost < dist[nxt_v]:\n                dist[nxt_v] = dist[v] +\
    \ cost\n                parent[nxt_v] = v\n                heapq.heappush(q, (dist[nxt_v],\
    \ nxt_v))\n    return dist, parent\n\n\ndef trace_route(goal, parent):\n    if\
    \ parent[goal] == -1:\n        return []\n    path = []\n    v = goal\n    while\
    \ v != -1:\n        path.append(v)\n        v = parent[v]\n    return path[::-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/ShortestPath/dijkstra_trace.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/ShortestPath/dijkstra_trace.py
layout: document
redirect_from:
- /library/Graph/ShortestPath/dijkstra_trace.py
- /library/Graph/ShortestPath/dijkstra_trace.py.html
title: Graph/ShortestPath/dijkstra_trace.py
---
