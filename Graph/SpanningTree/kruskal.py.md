---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\GRL_2_A.kruskal.test.py
    title: TestCase\AOJ\GRL_2_A.kruskal.test.py
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
  code: "from operator import itemgetter\r\nfrom DataStructure.UnionFind.UnionFind\
    \ import UnionFind\r\n\r\n\r\ndef kruskal(n, edges):\r\n    edges = sorted(edges,\
    \ key=itemgetter(2))\r\n    uf = UnionFind(n)\r\n    res = 0\r\n    for u, v,\
    \ cost in edges:\r\n        if not uf.same(u, v):\r\n            uf.merge(u, v)\r\
    \n            res += cost\r\n    return res\r\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph\SpanningTree\kruskal.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\GRL_2_A.kruskal.test.py
documentation_of: Graph\SpanningTree\kruskal.py
layout: document
title: "\u6700\u5C0F\u5168\u57DF\u6728 (\u30AF\u30E9\u30B9\u30AB\u30EB\u6CD5)"
---
