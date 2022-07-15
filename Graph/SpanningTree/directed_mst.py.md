---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/Heap/SkewHeap.py
    title: "\u4F75\u5408\u53EF\u80FD\u30D2\u30FC\u30D7 (Skew Heap)"
  - icon: ':heavy_check_mark:'
    path: DataStructure/UnionFind/UnionFind.py
    title: Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_2_B.test.py
    title: TestCase/AOJ/GRL_2_B.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/directedmst.test.py
    title: TestCase/LibraryChecker/directedmst.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.UnionFind.UnionFind import UnionFind\nfrom DataStructure.Heap.SkewHeap\
    \ import SkewHeap\n\n\ndef directed_mst(n, edges, root):\n    OFFSET = m = len(edges)\n\
    \    from_ = [0] * n\n    from_cost = [0] * n\n    from_heap = [SkewHeap() for\
    \ i in range(n)]\n\n    uf = UnionFind(n)\n    par_e = [-1] * m\n    stem = [-1]\
    \ * n\n    used = [0] * n\n    used[root] = 2\n    idxs = []\n\n    for idx, (fr,\
    \ to, cost) in enumerate(edges):\n        from_heap[to].push(cost * OFFSET + idx)\n\
    \n    res = 0\n    for v in range(n):\n        if used[v] != 0:\n            continue\n\
    \        processing = []\n        chi_e = []\n        cycle = 0\n        while\
    \ used[v] != 2:\n            used[v] = 1\n            processing.append(v)\n \
    \           if from_heap[v].empty():\n                return -1, [-1] * n\n  \
    \          from_cost[v], idx = divmod(from_heap[v].pop(), OFFSET)\n          \
    \  from_[v] = uf.root(edges[idx][0])\n            if stem[v] == -1:\n        \
    \        stem[v] = idx\n            if from_[v] == v:\n                continue\n\
    \            res += from_cost[v]\n            idxs.append(idx)\n            while\
    \ cycle:\n                par_e[chi_e.pop()] = idx\n                cycle -= 1\n\
    \            chi_e.append(idx)\n            if used[from_[v]] == 1:\n        \
    \        p = v\n                while True:\n                    if not from_heap[p].empty():\n\
    \                        from_heap[p].add(-from_cost[p] * OFFSET)\n          \
    \          if p != v:\n                        uf.merge(v, p)\n              \
    \          from_heap[v].meld(from_heap[p])\n                    p = uf.root(from_[p])\n\
    \                    new_v = uf.root(v)\n                    from_heap[new_v]\
    \ = from_heap[v]\n                    v = new_v\n                    cycle +=\
    \ 1\n                    if p == v:\n                        break\n         \
    \   else:\n                v = from_[v]\n        for v in processing:\n      \
    \      used[v] = 2\n\n    used_e = [False] * m\n    par = [-1] * n\n    for idx\
    \ in reversed(idxs):\n        if used_e[idx]:\n            continue\n        fr,\
    \ to, cost = edges[idx]\n        par[to] = fr\n        x = stem[to]\n        while\
    \ x != idx:\n            used_e[x] = True\n            x = par_e[x]\n    return\
    \ res, par\n"
  dependsOn:
  - DataStructure/Heap/SkewHeap.py
  - DataStructure/UnionFind/UnionFind.py
  isVerificationFile: false
  path: Graph/SpanningTree/directed_mst.py
  requiredBy: []
  timestamp: '2021-01-14 12:29:07+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/directedmst.test.py
  - TestCase/AOJ/GRL_2_B.test.py
documentation_of: Graph/SpanningTree/directed_mst.py
layout: document
title: "\u6700\u5C0F\u6709\u5411\u5168\u57DF\u6728"
---

## 概要
最小有向全域木とその総コストを求める。

## 使い方
`directed_mst(n: int, edges: Sequence[Tuple[int, int, int]], root: int)　-> Tuple[int, List[int]]`  
重み付き有向辺のリスト `edges` に対して、`root` を根とした最小有向全域木の総コスト、その有向木を表す親頂点の配列を返す。計算量 $O(E\log V)$
