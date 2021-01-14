---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def topological_sorted(digraph):\n    n = len(digraph)\n    indegree = [0]\
    \ * n\n    for v in range(n):\n        for nxt_v in digraph[v]:\n            indegree[nxt_v]\
    \ += 1\n\n    tp_order = [i for i in range(n) if indegree[i] == 0]\n    stack\
    \ = tp_order[:]\n    while stack:\n        v = stack.pop()\n        for nxt_v\
    \ in digraph[v]:\n            indegree[nxt_v] -= 1\n            if indegree[nxt_v]\
    \ == 0:\n                stack.append(nxt_v)\n                tp_order.append(nxt_v)\n\
    \n    return len(tp_order) == n, tp_order\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/misc/topological_sorted.py
  requiredBy: []
  timestamp: '2021-01-15 02:43:02+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/misc/topological_sorted.py
layout: document
title: "\u30C8\u30DD\u30ED\u30B8\u30AB\u30EB\u30BD\u30FC\u30C8"
---
