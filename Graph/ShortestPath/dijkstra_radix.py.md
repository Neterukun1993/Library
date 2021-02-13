---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: DataStructure/Heap/RadixHeap.py
    title: Radix Heap
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_1_A.RadixHeap.test.py
    title: TestCase/AOJ/GRL_1_A.RadixHeap.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.Heap.RadixHeap import RadixHeap\n\n\ndef dijkstra(start,\
    \ graph, LIMIT=1<<64):\n    INF = 10 ** 18\n    n = len(graph)\n    dist = [INF]\
    \ * n\n    dist[start] = 0\n    rh = RadixHeap(LIMIT)\n    rh.push(0, start)\n\
    \    while rh:\n        d, v = rh.pop()\n        if dist[v] < d:\n           \
    \ continue\n        for nxt_v, cost in graph[v]:\n            if dist[v] + cost\
    \ < dist[nxt_v]:\n                dist[nxt_v] = dist[v] + cost\n             \
    \   rh.push(dist[nxt_v], nxt_v)\n    return dist\n"
  dependsOn:
  - DataStructure/Heap/RadixHeap.py
  isVerificationFile: false
  path: Graph/ShortestPath/dijkstra_radix.py
  requiredBy: []
  timestamp: '2021-02-02 20:30:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/GRL_1_A.RadixHeap.test.py
documentation_of: Graph/ShortestPath/dijkstra_radix.py
layout: document
title: "\u30C0\u30A4\u30AF\u30B9\u30C8\u30E9\u6CD5 (Radix Heap)"
---