---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\UnionFind\UnionFind.py
    title: Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\GRL_2_A.boruvka.test.py
    title: TestCase\AOJ\GRL_2_A.boruvka.test.py
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
  code: "from DataStructure.UnionFind.UnionFind import UnionFind\r\n\r\n\r\ndef boruvka(n,\
    \ edges):\r\n    INF = 10 ** 18\r\n    uf = UnionFind(n)\r\n    res = 0\r\n  \
    \  while uf.cnt != 1:\r\n        update = False\r\n        min_costs = [(INF,\
    \ -1, -1) for _ in range(n)]\r\n        for u, v, cost in edges:\r\n         \
    \   if not uf.same(u, v):\r\n                rt_u = uf.root(v)\r\n           \
    \     rt_v = uf.root(u)\r\n                min_costs[rt_u] = min(min_costs[rt_u],\
    \ (cost, u, v))\r\n                min_costs[rt_v] = min(min_costs[rt_v], (cost,\
    \ u, v))\r\n        for cost, u, v in min_costs:\r\n            if cost != INF\
    \ and not uf.same(u, v):\r\n                update = True\r\n                uf.merge(u,\
    \ v)\r\n                res += cost\r\n        if not update:\r\n            return\
    \ -1\r\n    return res\r\n"
  dependsOn:
  - DataStructure\UnionFind\UnionFind.py
  isVerificationFile: false
  path: Graph\SpanningTree\boruvka.py
  requiredBy: []
  timestamp: '2021-01-04 22:11:12+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\GRL_2_A.boruvka.test.py
documentation_of: Graph\SpanningTree\boruvka.py
layout: document
title: "\u6700\u5C0F\u5168\u57DF\u6728 (\u30D6\u30EB\u30FC\u30D5\u30AB\u6CD5)"
---
