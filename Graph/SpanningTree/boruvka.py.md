---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: DataStructure/UnionFind/UnionFind.py
    title: Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: TestCase/AOJ/GRL_2_A.boruvka.test.py
    title: TestCase/AOJ/GRL_2_A.boruvka.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.UnionFind.UnionFind import UnionFind\n\n\ndef boruvka(n,\
    \ edges):\n    INF = 10 ** 18\n    uf = UnionFind(n)\n    res = 0\n    while uf.cnt\
    \ != 1:\n        update = False\n        min_costs = [(INF, -1, -1) for _ in range(n)]\n\
    \        for u, v, cost in edges:\n            if not uf.same(u, v):\n       \
    \         rt_u = uf.root(v)\n                rt_v = uf.root(u)\n             \
    \   min_costs[rt_u] = min(min_costs[rt_u], (cost, u, v))\n                min_costs[rt_v]\
    \ = min(min_costs[rt_v], (cost, u, v))\n        for cost, u, v in min_costs:\n\
    \            if cost != INF and not uf.same(u, v):\n                update = True\n\
    \                uf.merge(u, v)\n                res += cost\n        if not update:\n\
    \            return -1\n    return res\n"
  dependsOn:
  - DataStructure/UnionFind/UnionFind.py
  isVerificationFile: false
  path: Graph/SpanningTree/boruvka.py
  requiredBy: []
  timestamp: '2021-01-04 22:11:12+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - TestCase/AOJ/GRL_2_A.boruvka.test.py
documentation_of: Graph/SpanningTree/boruvka.py
layout: document
title: "\u6700\u5C0F\u5168\u57DF\u6728 (\u30D6\u30EB\u30FC\u30D5\u30AB\u6CD5)"
---
