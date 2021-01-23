---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\GRL_5_A.test.py
    title: TestCase\AOJ\GRL_5_A.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\GRL_5_B.test.py
    title: TestCase\AOJ\GRL_5_B.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\yukicoder\yuki0922.HLDecomposition.test.py
    title: TestCase\yukicoder\yuki0922.HLDecomposition.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\yukicoder\yuki0922.test.py
    title: TestCase\yukicoder\yuki0922.test.py
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
  code: "def rerooting(n, edges, unit, merge, addnode):\r\n    tree = [[] for i in\
    \ range(n)]\r\n    idxs = [[] for i in range(n)]\r\n    for u, v in edges:\r\n\
    \        idxs[u].append(len(tree[v]))\r\n        idxs[v].append(len(tree[u]))\r\
    \n        tree[u].append(v)\r\n        tree[v].append(u)\r\n    sub = [[unit]\
    \ * len(tree[v]) for v in range(n)]\r\n    noderes = [unit] * n\r\n\r\n    # topological\
    \ sort\r\n    tp_order = []\r\n    par = [-1] * n\r\n    for root in range(n):\r\
    \n        if par[root] != -1:\r\n            continue\r\n        stack = [root]\r\
    \n        while stack:\r\n            v = stack.pop()\r\n            tp_order.append(v)\r\
    \n            for nxt_v in tree[v]:\r\n                if nxt_v == par[v]:\r\n\
    \                    continue\r\n                par[nxt_v] = v\r\n          \
    \      stack.append(nxt_v)\r\n\r\n    # tree DP\r\n    for v in reversed(tp_order[1:]):\r\
    \n        res = unit\r\n        par_idx = -1\r\n        for idx, nxt_v in enumerate(tree[v]):\r\
    \n            if nxt_v == par[v]:\r\n                par_idx = idx\r\n       \
    \         continue\r\n            res = merge(res, sub[v][idx])\r\n        if\
    \ par_idx != -1:\r\n            sub[par[v]][idxs[v][par_idx]] = addnode(res, v)\r\
    \n\r\n    # rerooting DP\r\n    for v in tp_order:\r\n        acc_back = [unit]\
    \ * len(tree[v])\r\n        for i in reversed(range(1, len(acc_back))):\r\n  \
    \          acc_back[i - 1] = merge(sub[v][i], acc_back[i])\r\n        acc_front\
    \ = unit\r\n        for idx, nxt_v in enumerate(tree[v]):\r\n            res =\
    \ addnode(merge(acc_front, acc_back[idx]), v)\r\n            sub[nxt_v][idxs[v][idx]]\
    \ = res\r\n            acc_front = merge(acc_front, sub[v][idx])\r\n        noderes[v]\
    \ = addnode(acc_front, v)\r\n    return noderes\r\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph\Tree\rerooting.py
  requiredBy: []
  timestamp: '2021-01-14 15:36:57+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\GRL_5_A.test.py
  - TestCase\AOJ\GRL_5_B.test.py
  - TestCase\yukicoder\yuki0922.HLDecomposition.test.py
  - TestCase\yukicoder\yuki0922.test.py
documentation_of: Graph\Tree\rerooting.py
layout: document
title: "\u5168\u65B9\u4F4D\u6728DP (Re-Rooting)"
---
