---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_4_A.test.py
    title: TestCase/AOJ/GRL_4_A.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/cycle_detection.test.py
    title: TestCase/LibraryChecker/cycle_detection.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def cycle_detection(graph):\n    def _dfs(v):\n        stack = [v, 0]\n \
    \       visited[v] = 1\n        while stack:\n            v, idx = stack[-2:]\n\
    \            if idx < len(graph[v]):\n                nxt_v = graph[v][idx]\n\
    \                stack[-1] += 1\n                if visited[nxt_v] == 1:\n   \
    \                 # detect cycle\n                    cycle.append(nxt_v)\n  \
    \                  while cycle[0] != v:\n                        cycle.append(v)\n\
    \                        stack.pop(), stack.pop()\n                        v =\
    \ stack[-2]\n                    cycle.reverse()\n                    return\n\
    \                if visited[nxt_v] == 2:\n                    continue\n     \
    \           visited[nxt_v] = 1\n                stack.append(nxt_v)\n        \
    \        stack.append(0)\n            else:\n                visited[v] = 2\n\
    \                stack.pop(), stack.pop()\n\n    n = len(graph)\n    visited =\
    \ [0] * n\n    cycle = []\n    for v in range(n):\n        if not cycle and visited[v]\
    \ == 0:\n            _dfs(v)\n    return cycle\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/misc/cycle_detection.py
  requiredBy: []
  timestamp: '2021-01-14 17:41:58+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/GRL_4_A.test.py
  - TestCase/LibraryChecker/cycle_detection.test.py
documentation_of: Graph/misc/cycle_detection.py
layout: document
title: "\u30B5\u30A4\u30AF\u30EB\u691C\u51FA"
---
