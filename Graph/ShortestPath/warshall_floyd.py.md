---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\GRL_1_C.test.py
    title: TestCase\AOJ\GRL_1_C.test.py
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
  code: "def warshall_floyd(matrix):\r\n    n = len(matrix)\r\n    dist = [[d for\
    \ d in row] for row in matrix]\r\n    for k in range(n):\r\n        for i in range(n):\r\
    \n            for j in range(n):\r\n                dist[i][j] = min(dist[i][j],\
    \ dist[i][k] + dist[k][j])\r\n    return dist\r\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph\ShortestPath\warshall_floyd.py
  requiredBy: []
  timestamp: '2021-01-15 11:26:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\GRL_1_C.test.py
documentation_of: Graph\ShortestPath\warshall_floyd.py
layout: document
title: "\u30EF\u30FC\u30B7\u30E3\u30EB\u30D5\u30ED\u30A4\u30C9\u6CD5"
---
