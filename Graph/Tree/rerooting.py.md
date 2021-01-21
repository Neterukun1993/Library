---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_5_A.test.py
    title: TestCase/AOJ/GRL_5_A.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_5_B.test.py
    title: TestCase/AOJ/GRL_5_B.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0922.HLDecomposition.test.py
    title: TestCase/yukicoder/yuki0922.HLDecomposition.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0922.test.py
    title: TestCase/yukicoder/yuki0922.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def rerooting(n, edges, unit, merge, addnode):\n    tree = [[] for i in range(n)]\n\
    \    idxs = [[] for i in range(n)]\n    for u, v in edges:\n        idxs[u].append(len(tree[v]))\n\
    \        idxs[v].append(len(tree[u]))\n        tree[u].append(v)\n        tree[v].append(u)\n\
    \    sub = [[unit] * len(tree[v]) for v in range(n)]\n    noderes = [unit] * n\n\
    \n    # topological sort\n    tp_order = []\n    par = [-1] * n\n    for root\
    \ in range(n):\n        if par[root] != -1:\n            continue\n        stack\
    \ = [root]\n        while stack:\n            v = stack.pop()\n            tp_order.append(v)\n\
    \            for nxt_v in tree[v]:\n                if nxt_v == par[v]:\n    \
    \                continue\n                par[nxt_v] = v\n                stack.append(nxt_v)\n\
    \n    # tree DP\n    for v in reversed(tp_order[1:]):\n        res = unit\n  \
    \      par_idx = -1\n        for idx, nxt_v in enumerate(tree[v]):\n         \
    \   if nxt_v == par[v]:\n                par_idx = idx\n                continue\n\
    \            res = merge(res, sub[v][idx])\n        if par_idx != -1:\n      \
    \      sub[par[v]][idxs[v][par_idx]] = addnode(res, v)\n\n    # rerooting DP\n\
    \    for v in tp_order:\n        acc_back = [unit] * len(tree[v])\n        for\
    \ i in reversed(range(1, len(acc_back))):\n            acc_back[i - 1] = merge(sub[v][i],\
    \ acc_back[i])\n        acc_front = unit\n        for idx, nxt_v in enumerate(tree[v]):\n\
    \            res = addnode(merge(acc_front, acc_back[idx]), v)\n            sub[nxt_v][idxs[v][idx]]\
    \ = res\n            acc_front = merge(acc_front, sub[v][idx])\n        noderes[v]\
    \ = addnode(acc_front, v)\n    return noderes\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Tree/rerooting.py
  requiredBy: []
  timestamp: '2021-01-14 15:36:57+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/GRL_5_A.test.py
  - TestCase/AOJ/GRL_5_B.test.py
  - TestCase/yukicoder/yuki0922.test.py
  - TestCase/yukicoder/yuki0922.HLDecomposition.test.py
documentation_of: Graph/Tree/rerooting.py
layout: document
title: "\u5168\u65B9\u4F4D\u6728DP (Re-Rooting)"
---
