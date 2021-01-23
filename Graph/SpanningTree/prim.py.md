---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\GRL_2_A.prim.test.py
    title: TestCase\AOJ\GRL_2_A.prim.test.py
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
  code: "from heapq import heappop, heappush\r\n\r\n\r\ndef prim(graph):\r\n    res\
    \ = 0\r\n    used = [False] * len(graph)\r\n    hq = [(0, 0)]  # hq = [(\u8FBA\
    \u306E\u30B3\u30B9\u30C8, \u73FE\u5728\u5730)]\r\n    while hq:\r\n        cost,\
    \ v = heappop(hq)\r\n        if used[v]:\r\n            continue\r\n        used[v]\
    \ = True\r\n        res += cost\r\n        for nxt_v, cost in graph[v]:\r\n  \
    \          heappush(hq, (cost, nxt_v))\r\n    return res\r\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph\SpanningTree\prim.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\GRL_2_A.prim.test.py
documentation_of: Graph\SpanningTree\prim.py
layout: document
title: "\u6700\u5C0F\u5168\u57DF\u6728 (\u30D7\u30EA\u30E0\u6CD5)"
---
