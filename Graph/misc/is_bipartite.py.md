---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/2370.test.py
    title: TestCase/AOJ/2370.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def is_bipartite(graph):\n    n = len(graph)\n    cols = [-1] * n\n    cnts\
    \ = []\n    for v in range(n):\n        if cols[v] != -1:\n            continue\n\
    \        cols[v] = 0\n        cnt = [1, 0]\n        stack = [v]\n        while\
    \ stack:\n            v = stack.pop()\n            for nxt_v in graph[v]:\n  \
    \              if cols[nxt_v] != -1:\n                    if cols[nxt_v] == cols[v]\
    \ ^ 1:\n                        continue\n                    else:\n        \
    \                return False, cols, cnts\n                cols[nxt_v] = cols[v]\
    \ ^ 1\n                cnt[cols[nxt_v]] += 1\n                stack.append(nxt_v)\n\
    \        cnts.append(cnt)\n    return True, cols, cnts\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/misc/is_bipartite.py
  requiredBy: []
  timestamp: '2021-05-07 07:33:57+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/2370.test.py
documentation_of: Graph/misc/is_bipartite.py
layout: document
title: "\u4E8C\u90E8\u30B0\u30E9\u30D5\u5224\u5B9A (DFS)"
---
