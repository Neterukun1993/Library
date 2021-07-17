---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_12_B.test.py
    title: TestCase/AOJ/ALDS1_12_B.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def dijkstra_v2(start, matrix):\n    INF = 10 ** 18\n    n = len(matrix)\n\
    \    used = [False] * n\n    dist = [INF] * n\n    dist[start] = 0\n    while\
    \ True:\n        v = -1\n        for u in range(n):\n            if not used[u]\
    \ and (v == -1 or dist[u] < dist[v]):\n                v = u\n        if v ==\
    \ -1:\n            break\n        used[v] = True\n        for nxt_v in range(n):\n\
    \            dist[nxt_v] = min(dist[nxt_v], dist[v] + matrix[v][nxt_v])\n    return\
    \ dist\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/ShortestPath/dijkstra_v2.py
  requiredBy: []
  timestamp: '2021-01-05 04:12:38+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_12_B.test.py
documentation_of: Graph/ShortestPath/dijkstra_v2.py
layout: document
title: "\u30C0\u30A4\u30AF\u30B9\u30C8\u30E9\u6CD5 ($O(V^2)$)"
---
