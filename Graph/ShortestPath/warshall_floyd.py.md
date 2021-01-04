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
  code: "from copy import deepcopy\n\n\ndef warshall_floyd(matrix):\n    n = len(matrix)\n\
    \    dist = deepcopy(matrix)\n    for k in range(n):\n        for i in range(n):\n\
    \            for j in range(n):\n                dist[i][j] = min(dist[i][j],\
    \ dist[i][k] + dist[k][j])\n    return dist\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/ShortestPath/warshall_floyd.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/ShortestPath/warshall_floyd.py
layout: document
redirect_from:
- /library/Graph/ShortestPath/warshall_floyd.py
- /library/Graph/ShortestPath/warshall_floyd.py.html
title: Graph/ShortestPath/warshall_floyd.py
---
