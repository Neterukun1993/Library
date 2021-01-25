---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_1_C.test.py
    title: TestCase/AOJ/GRL_1_C.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def warshall_floyd(matrix):\n    n = len(matrix)\n    dist = [[d for d in\
    \ row] for row in matrix]\n    for k in range(n):\n        for i in range(n):\n\
    \            for j in range(n):\n                dist[i][j] = min(dist[i][j],\
    \ dist[i][k] + dist[k][j])\n    return dist\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/ShortestPath/warshall_floyd.py
  requiredBy: []
  timestamp: '2021-01-15 11:26:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/GRL_1_C.test.py
documentation_of: Graph/ShortestPath/warshall_floyd.py
layout: document
title: "\u30EF\u30FC\u30B7\u30E3\u30EB\u30D5\u30ED\u30A4\u30C9\u6CD5"
---
