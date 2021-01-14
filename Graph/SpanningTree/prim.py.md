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
  code: "from heapq import heappop, heappush\n\n\ndef prim(graph):\n    res = 0\n\
    \    used = [False] * len(graph)\n    hq = [(0, 0)]  # hq = [(\u8FBA\u306E\u30B3\
    \u30B9\u30C8, \u73FE\u5728\u5730)]\n    while hq:\n        cost, v = heappop(hq)\n\
    \        if used[v]:\n            continue\n        used[v] = True\n        res\
    \ += cost\n        for nxt_v, cost in graph[v]:\n            heappush(hq, (cost,\
    \ nxt_v))\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/SpanningTree/prim.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/SpanningTree/prim.py
layout: document
title: "\u6700\u5C0F\u5168\u57DF\u6728 (\u30D7\u30EA\u30E0\u6CD5)"
---
