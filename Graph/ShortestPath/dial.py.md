---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_12_B.dial.test.py
    title: TestCase/AOJ/ALDS1_12_B.dial.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def dial(graph, start, max_w):\n    INF = 10 ** 18\n    n = len(graph)\n\
    \    dist = [INF] * n\n    dist[start] = 0\n    stacks = [[] for i in range(max_w\
    \ + 1)]\n    stacks[0].append(start)\n    for d in range(max_w * (n - 1) + 1):\n\
    \        st = stacks[d % (max_w + 1)]\n        while st:\n            v = st.pop()\n\
    \            if dist[v] < d:\n                continue\n            for nxt_v,\
    \ cost in graph[v]:\n                if dist[v] + cost < dist[nxt_v]:\n      \
    \              dist[nxt_v] = dist[v] + cost\n                    stacks[(d + cost)\
    \ % (max_w + 1)].append(nxt_v)\n    return dist\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/ShortestPath/dial.py
  requiredBy: []
  timestamp: '2021-06-02 23:10:54+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_12_B.dial.test.py
documentation_of: Graph/ShortestPath/dial.py
layout: document
title: "Dial\u2019s Algorithm"
---