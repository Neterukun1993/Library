---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: TestCase/AOJ/GRL_5_A.test.py
    title: TestCase/AOJ/GRL_5_A.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_5_B.test.py
    title: TestCase/AOJ/GRL_5_B.test.py
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def edge_to_vertex(n, edges):\n    m = len(edges)\n    new_edges = []\n \
    \   vals = [0] * (n + m)\n    for i, (u, v, val) in enumerate(edges):\n      \
    \  new_edges.append((u, n + i))\n        new_edges.append((n + i, v))\n      \
    \  vals[n + i] = val\n    return new_edges, vals\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/edge_to_vertex.py
  requiredBy: []
  timestamp: '2021-01-11 06:00:13+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - TestCase/AOJ/GRL_5_A.test.py
  - TestCase/AOJ/GRL_5_B.test.py
documentation_of: Graph/edge_to_vertex.py
layout: document
title: "\u8FBA\u60C5\u5831\u3092\u9802\u70B9\u60C5\u5831\u3078\u3068\u5909\u63DB"
---
