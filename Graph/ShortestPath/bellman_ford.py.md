---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_1_B.test.py
    title: TestCase/AOJ/GRL_1_B.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def bellman_ford(start, graph):\n    INF = 10 ** 18\n    n = len(graph)\n\
    \    dist = [INF] * n\n    dist[start] = 0\n    for _ in range(n):\n        update\
    \ = False\n        for v, edges in enumerate(graph):\n            for nxt_v, cost\
    \ in edges:\n                if dist[v] != INF and dist[nxt_v] > dist[v] + cost:\n\
    \                    dist[nxt_v] = dist[v] + cost\n                    update\
    \ = True\n        if not update:\n            break\n    else:\n        return\
    \ True, dist  # start\u304B\u3089\u8FBF\u308A\u7740\u3051\u308B\u8CA0\u9589\u8DEF\
    \u304C\u5B58\u5728\n    return False, dist  # start\u304B\u3089\u8FBF\u308A\u7740\
    \u3051\u308B\u8CA0\u9589\u8DEF\u304C\u5B58\u5728\u3057\u306A\u3044\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/ShortestPath/bellman_ford.py
  requiredBy: []
  timestamp: '2021-01-05 04:12:38+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/GRL_1_B.test.py
documentation_of: Graph/ShortestPath/bellman_ford.py
layout: document
title: "\u30D9\u30EB\u30DE\u30F3\u30D5\u30A9\u30FC\u30C9\u6CD5"
---
