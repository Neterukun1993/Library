---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_2_A.prim.test.py
    title: TestCase/AOJ/GRL_2_A.prim.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# from heapq import heappop, heappush\nfrom standard_library.heapq import\
    \ heappop, heappush\n\n\ndef prim(graph):\n    res = 0\n    used = [False] * len(graph)\n\
    \    hq = [(0, 0)]  # hq = [(\u8FBA\u306E\u30B3\u30B9\u30C8, \u73FE\u5728\u5730\
    )]\n    while hq:\n        cost, v = heappop(hq)\n        if used[v]:\n      \
    \      continue\n        used[v] = True\n        res += cost\n        for nxt_v,\
    \ cost in graph[v]:\n            heappush(hq, (cost, nxt_v))\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/SpanningTree/prim.py
  requiredBy: []
  timestamp: '2022-01-20 17:35:30+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/GRL_2_A.prim.test.py
documentation_of: Graph/SpanningTree/prim.py
layout: document
title: "\u6700\u5C0F\u5168\u57DF\u6728 (\u30D7\u30EA\u30E0\u6CD5)"
---

## 概要
プリム法により最小全域木の総コストを求める。

## 使い方
`prim(graph: Sequence[Iterable[Tuple[int, int]]]) -> int`  
隣接リストで表現される無向グラフ `graph` に対して、最小全域木の総コストを返す。計算量 $O((V + E)\log V)$
