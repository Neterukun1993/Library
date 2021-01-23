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
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def topological_sorted(digraph):\r\n    n = len(digraph)\r\n    indegree\
    \ = [0] * n\r\n    for v in range(n):\r\n        for nxt_v in digraph[v]:\r\n\
    \            indegree[nxt_v] += 1\r\n\r\n    tp_order = [i for i in range(n) if\
    \ indegree[i] == 0]\r\n    stack = tp_order[:]\r\n    while stack:\r\n       \
    \ v = stack.pop()\r\n        for nxt_v in digraph[v]:\r\n            indegree[nxt_v]\
    \ -= 1\r\n            if indegree[nxt_v] == 0:\r\n                stack.append(nxt_v)\r\
    \n                tp_order.append(nxt_v)\r\n\r\n    return len(tp_order) == n,\
    \ tp_order\r\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph\misc\topological_sorted.py
  requiredBy: []
  timestamp: '2021-01-15 02:43:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph\misc\topological_sorted.py
layout: document
title: "\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8"
---
