---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/Heap/PersistentLeftistHeap.py
    title: "\u4F75\u5408\u53EF\u80FD\u6C38\u7D9A\u30D2\u30FC\u30D7 (Persistent Leftist\
      \ Heap)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/k_shortest_walk.test.py
    title: TestCase/LibraryChecker/k_shortest_walk.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://qiita.com/hotman78/items/42534a01c4bd05ed5e1e
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# from heapq import heappop, heappush\nfrom standard_library.heapq import\
    \ heappop, heappush\nfrom DataStructure.Heap.PersistentLeftistHeap import LeftistHeap\n\
    \n\n# https://qiita.com/hotman78/items/42534a01c4bd05ed5e1e\ndef k_shortest_walk(n,\
    \ edges, start, goal, k):\n    INF = 10 ** 18\n    graph = [[] for _ in range(n)]\n\
    \    rev_graph = [[] for _ in range(n)]\n    for i, (u, v, cost) in enumerate(edges):\n\
    \        graph[u].append((v, cost, i))\n        rev_graph[v].append((u, cost,\
    \ i))\n\n    potential = [INF] * n\n    potential[goal] = 0\n    parent = [-1]\
    \ * n\n    children = [[] for i in range(n)]\n    idxs = [-1] * n\n\n    que =\
    \ [(0, goal)]\n    while que:\n        d, v = heappop(que)\n        if potential[v]\
    \ < d:\n            continue\n        for nxt_v, cost, idx in rev_graph[v]:\n\
    \            if potential[v] + cost < potential[nxt_v]:\n                potential[nxt_v]\
    \ = potential[v] + cost\n                parent[nxt_v] = v\n                idxs[nxt_v]\
    \ = idx\n                heappush(que, (potential[nxt_v], nxt_v))\n\n    for v\
    \ in range(n):\n        if parent[v] != -1:\n            children[parent[v]].append(v)\n\
    \n    heap_g = [LeftistHeap() for _ in range(n)]\n    que = [goal]\n    iq = 0\n\
    \    while iq < len(que):\n        v = que[iq]\n        iq += 1\n        if parent[v]\
    \ != -1:\n            heap_g[v] = LeftistHeap.merge(heap_g[v], heap_g[parent[v]])\n\
    \        for nxt_v, cost, idx in graph[v]:\n            if idxs[v] != idx:\n \
    \               heap_g[v] = heap_g[v].insert(\n                    cost - potential[v]\
    \ + potential[nxt_v], nxt_v)\n        for nxt_v in children[v]:\n            que.append(nxt_v)\n\
    \n    src = LeftistHeap().insert(potential[start], start)\n    que = [(potential[start],\
    \ src)]\n    ans = []\n    while que:\n        val, hp = heappop(que)\n      \
    \  if val >= INF:\n            break\n        ans.append(val)\n        if len(ans)\
    \ == k:\n            break\n        if hp.a:\n            heappush(que, (val +\
    \ hp.a.find_min[0] - hp.find_min[0], hp.a))\n        if hp.b:\n            heappush(que,\
    \ (val + hp.b.find_min[0] - hp.find_min[0], hp.b))\n        to = hp.find_min[1]\n\
    \        if heap_g[to]:\n            heappush(que, (val + heap_g[to].find_min[0],\
    \ heap_g[to]))\n\n    for _ in range(len(ans), k):\n        ans.append(-1)\n \
    \   return ans\n"
  dependsOn:
  - DataStructure/Heap/PersistentLeftistHeap.py
  isVerificationFile: false
  path: Graph/misc/k_shortest_walk.py
  requiredBy: []
  timestamp: '2022-01-20 20:13:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/k_shortest_walk.test.py
documentation_of: Graph/misc/k_shortest_walk.py
layout: document
title: "\u4E0A\u4F4D $k$ \u500B\u306E\u30A6\u30A9\u30FC\u30AF"
---
