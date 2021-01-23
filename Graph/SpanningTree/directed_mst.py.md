---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\Heap\SkewHeap.py
    title: "\u4F75\u5408\u53EF\u80FD\u30D2\u30FC\u30D7 (Skew Heap)"
  - icon: ':heavy_check_mark:'
    path: DataStructure\UnionFind\UnionFind.py
    title: Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\GRL_2_B.test.py
    title: TestCase\AOJ\GRL_2_B.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\directedmst.test.py
    title: TestCase\LibraryChecker\directedmst.test.py
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
  code: "from DataStructure.UnionFind.UnionFind import UnionFind\r\nfrom DataStructure.Heap.SkewHeap\
    \ import SkewHeap\r\n\r\n\r\ndef directed_mst(n, edges, root):\r\n    OFFSET =\
    \ m = len(edges)\r\n    from_ = [0] * n\r\n    from_cost = [0] * n\r\n    from_heap\
    \ = [SkewHeap() for i in range(n)]\r\n\r\n    uf = UnionFind(n)\r\n    par_e =\
    \ [-1] * m\r\n    stem = [-1] * n\r\n    used = [0] * n\r\n    used[root] = 2\r\
    \n    idxs = []\r\n\r\n    for idx, (fr, to, cost) in enumerate(edges):\r\n  \
    \      from_heap[to].push(cost * OFFSET + idx)\r\n\r\n    res = 0\r\n    for v\
    \ in range(n):\r\n        if used[v] != 0:\r\n            continue\r\n       \
    \ processing = []\r\n        chi_e = []\r\n        cycle = 0\r\n        while\
    \ used[v] != 2:\r\n            used[v] = 1\r\n            processing.append(v)\r\
    \n            if from_heap[v].empty():\r\n                return -1, [-1] * n\r\
    \n            from_cost[v], idx = divmod(from_heap[v].pop(), OFFSET)\r\n     \
    \       from_[v] = uf.root(edges[idx][0])\r\n            if stem[v] == -1:\r\n\
    \                stem[v] = idx\r\n            if from_[v] == v:\r\n          \
    \      continue\r\n            res += from_cost[v]\r\n            idxs.append(idx)\r\
    \n            while cycle:\r\n                par_e[chi_e.pop()] = idx\r\n   \
    \             cycle -= 1\r\n            chi_e.append(idx)\r\n            if used[from_[v]]\
    \ == 1:\r\n                p = v\r\n                while True:\r\n          \
    \          if not from_heap[p].empty():\r\n                        from_heap[p].add(-from_cost[p]\
    \ * OFFSET)\r\n                    if p != v:\r\n                        uf.merge(v,\
    \ p)\r\n                        from_heap[v].meld(from_heap[p])\r\n          \
    \          p = uf.root(from_[p])\r\n                    new_v = uf.root(v)\r\n\
    \                    from_heap[new_v] = from_heap[v]\r\n                    v\
    \ = new_v\r\n                    cycle += 1\r\n                    if p == v:\r\
    \n                        break\r\n            else:\r\n                v = from_[v]\r\
    \n        for v in processing:\r\n            used[v] = 2\r\n\r\n    used_e =\
    \ [False] * m\r\n    par = [-1] * n\r\n    for idx in reversed(idxs):\r\n    \
    \    if used_e[idx]:\r\n            continue\r\n        fr, to, cost = edges[idx]\r\
    \n        par[to] = fr\r\n        x = stem[to]\r\n        while x != idx:\r\n\
    \            used_e[x] = True\r\n            x = par_e[x]\r\n    return res, par\r\
    \n"
  dependsOn:
  - DataStructure\Heap\SkewHeap.py
  - DataStructure\UnionFind\UnionFind.py
  isVerificationFile: false
  path: Graph\SpanningTree\directed_mst.py
  requiredBy: []
  timestamp: '2021-01-14 12:29:07+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\GRL_2_B.test.py
  - TestCase\LibraryChecker\directedmst.test.py
documentation_of: Graph\SpanningTree\directed_mst.py
layout: document
title: "\u6700\u5C0F\u6709\u5411\u5168\u57DF\u6728"
---
