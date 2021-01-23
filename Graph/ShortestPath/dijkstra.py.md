---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\GRL_1_A.test.py
    title: TestCase\AOJ\GRL_1_A.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import heapq\r\n\r\n\r\ndef dijkstra(start, graph):\r\n    INF = 10 ** 18\r\
    \n    n = len(graph)\r\n    dist = [INF] * n\r\n    dist[start] = 0\r\n    q =\
    \ [(0, start)]  # q = [(start\u304B\u3089\u306E\u8DDD\u96E2, \u73FE\u5728\u5730\
    )]\r\n    while q:\r\n        d, v = heapq.heappop(q)\r\n        if dist[v] <\
    \ d:\r\n            continue\r\n        for nxt_v, cost in graph[v]:\r\n     \
    \       if dist[v] + cost < dist[nxt_v]:\r\n                dist[nxt_v] = dist[v]\
    \ + cost\r\n                heapq.heappush(q, (dist[nxt_v], nxt_v))\r\n    return\
    \ dist\r\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph\ShortestPath\dijkstra.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\GRL_1_A.test.py
documentation_of: Graph\ShortestPath\dijkstra.py
layout: document
title: "\u30C0\u30A4\u30AF\u30B9\u30C8\u30E9\u6CD5"
---
