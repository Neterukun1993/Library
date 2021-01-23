---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\tree_diameter.test.py
    title: TestCase\LibraryChecker\tree_diameter.test.py
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
  code: "def diameter(tree):\r\n    def _dfs(start):\r\n        dist = [-1] * n\r\n\
    \        dist[start] = 0\r\n        stack = [start]\r\n        while stack:\r\n\
    \            v = stack.pop()\r\n            for nxt_v, cost in tree[v]:\r\n  \
    \              if dist[nxt_v] != -1:\r\n                    continue\r\n     \
    \           dist[nxt_v] = dist[v] + cost\r\n                stack.append(nxt_v)\r\
    \n        max_d = max(dist)\r\n        return dist.index(max_d), max_d, dist\r\
    \n\r\n    n = len(tree)\r\n    u, _, _ = _dfs(0)\r\n    v, diam, dist = _dfs(u)\r\
    \n    path = [v]\r\n    while v != u:\r\n        for nxt_v, cost in tree[v]:\r\
    \n            if cost + dist[nxt_v] == dist[v]:\r\n                path.append(nxt_v)\r\
    \n                v = nxt_v\r\n                break\r\n    return diam, path\r\
    \n"
  dependsOn: []
  isVerificationFile: false
  path: Graph\Tree\diameter.py
  requiredBy: []
  timestamp: '2021-01-11 01:21:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\LibraryChecker\tree_diameter.test.py
documentation_of: Graph\Tree\diameter.py
layout: document
title: "\u6728\u306E\u76F4\u5F84"
---
