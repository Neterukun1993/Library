---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\ALDS1_12_B.test.py
    title: TestCase\AOJ\ALDS1_12_B.test.py
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
  code: "def dijkstra_v2(start, matrix):\r\n    INF = 10 ** 18\r\n    n = len(matrix)\r\
    \n    used = [False] * n\r\n    dist = [INF] * n\r\n    dist[start] = 0\r\n  \
    \  while True:\r\n        v = -1\r\n        for u in range(n):\r\n           \
    \ if not used[u] and (v == -1 or dist[u] < dist[v]):\r\n                v = u\r\
    \n        if v == -1:\r\n            break\r\n        used[v] = True\r\n     \
    \   for nxt_v in range(n):\r\n            dist[nxt_v] = min(dist[nxt_v], dist[v]\
    \ + matrix[v][nxt_v])\r\n    return dist\r\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph\ShortestPath\dijkstra_v2.py
  requiredBy: []
  timestamp: '2021-01-05 04:12:38+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\ALDS1_12_B.test.py
documentation_of: Graph\ShortestPath\dijkstra_v2.py
layout: document
title: "\u30C0\u30A4\u30AF\u30B9\u30C8\u30E9\u6CD5 ($\\mathrm{O}(V^2)$)"
---
