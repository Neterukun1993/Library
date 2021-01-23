---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\GRL_4_A.test.py
    title: TestCase\AOJ\GRL_4_A.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\cycle_detection.test.py
    title: TestCase\LibraryChecker\cycle_detection.test.py
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
  code: "def cycle_detection(graph):\r\n    def _dfs(v):\r\n        stack = [v, 0]\r\
    \n        visited[v] = 1\r\n        while stack:\r\n            v, idx = stack[-2:]\r\
    \n            if idx < len(graph[v]):\r\n                nxt_v = graph[v][idx]\r\
    \n                stack[-1] += 1\r\n                if visited[nxt_v] == 1:\r\n\
    \                    # detect cycle\r\n                    cycle.append(nxt_v)\r\
    \n                    while cycle[0] != v:\r\n                        cycle.append(v)\r\
    \n                        stack.pop(), stack.pop()\r\n                       \
    \ v = stack[-2]\r\n                    cycle.reverse()\r\n                   \
    \ return\r\n                if visited[nxt_v] == 2:\r\n                    continue\r\
    \n                visited[nxt_v] = 1\r\n                stack.append(nxt_v)\r\n\
    \                stack.append(0)\r\n            else:\r\n                visited[v]\
    \ = 2\r\n                stack.pop(), stack.pop()\r\n\r\n    n = len(graph)\r\n\
    \    visited = [0] * n\r\n    cycle = []\r\n    for v in range(n):\r\n       \
    \ if not cycle and visited[v] == 0:\r\n            _dfs(v)\r\n    return cycle\r\
    \n"
  dependsOn: []
  isVerificationFile: false
  path: Graph\misc\cycle_detection.py
  requiredBy: []
  timestamp: '2021-01-14 17:41:58+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\GRL_4_A.test.py
  - TestCase\LibraryChecker\cycle_detection.test.py
documentation_of: Graph\misc\cycle_detection.py
layout: document
title: "\u30B5\u30A4\u30AF\u30EB\u691C\u51FA"
---
