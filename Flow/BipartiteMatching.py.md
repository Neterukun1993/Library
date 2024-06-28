---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/bipartitematching.test.py
    title: TestCase/LibraryChecker/bipartitematching.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links:
    - https://snuke.hatenablog.com/entry/2019/05/07/013609
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import sys\nsys.setrecursionlimit(10 ** 6)\n\n\n# https://snuke.hatenablog.com/entry/2019/05/07/013609\n\
    class BipartiteMatching:\n    def __init__(self, n, m):\n        self.n = n\n\
    \        self.m = m\n        self.graph = [[] for i in range(n)]\n        self.p\
    \ = [-1] * n\n        self.q = [-1] * m\n\n    def add_edge(self, u, v):\n   \
    \     assert(0 <= u <= self.n)\n        assert(0 <= v <= self.m)\n        self.graph[u].append(v)\n\
    \n    def maximum_matching(self):\n        def dfs(v):\n            # \u975E\u518D\
    \u5E30\u306B\u66F8\u304D\u76F4\u3057\u305F\u3044\n            if used[v]:\n  \
    \              return False\n            used[v] = True\n            for u in\
    \ self.graph[v]:\n                if self.q[u] == -1 or dfs(self.q[u]):\n    \
    \                self.q[u] = v\n                    self.p[v] = u\n          \
    \          return True\n            return False\n\n        res = 0\n        used\
    \ = [False] * self.n\n        update = True\n        while update:\n         \
    \   update = False\n            for v in range(self.n):\n                if self.p[v]\
    \ == -1 and dfs(v):\n                    update = True\n                    res\
    \ += 1\n            if update:\n                used = [False] * self.n\n    \
    \    return res\n\n    def matching_edges(self):\n        edges = []\n       \
    \ for v in range(self.n):\n            if self.p[v] != -1:\n                edges.append((v,\
    \ self.p[v]))\n        return edges\n"
  dependsOn: []
  isVerificationFile: false
  path: Flow/BipartiteMatching.py
  requiredBy: []
  timestamp: '2022-01-15 20:42:51+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/bipartitematching.test.py
documentation_of: Flow/BipartiteMatching.py
layout: document
title: "\u4E8C\u90E8\u30B0\u30E9\u30D5\u306E\u30DE\u30C3\u30C1\u30F3\u30B0"
---
