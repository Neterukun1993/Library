---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\Decomposition\SCC_Tarjan.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3 (Tarjan\u306E\u30A2\u30EB\u30B4\
      \u30EA\u30BA\u30E0)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\two_sat.test.py
    title: TestCase\LibraryChecker\two_sat.test.py
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
  code: "from Graph.Decomposition.SCC_Tarjan import StronglyConnectedComponents\r\n\
    \r\n\r\nclass TwoSAT:\r\n    def __init__(self, n):\r\n        self.n = n\r\n\
    \        self.scc = StronglyConnectedComponents(2 * n)\r\n        self.ans = [False]\
    \ * self.n\r\n\r\n    def add_clause(self, i, f, j, g):\r\n        self.scc.add_edge(2\
    \ * i + int(not f), 2 * j + int(g))\r\n        self.scc.add_edge(2 * j + int(not\
    \ g), 2 * i + int(f))\r\n\r\n    def satisfy(self):\r\n        self.scc.build()\r\
    \n        for i in range(self.n):\r\n            if self.scc.labels[2 * i] ==\
    \ self.scc.labels[2 * i + 1]:\r\n                return False\r\n            self.ans[i]\
    \ = self.scc.labels[2 * i] < self.scc.labels[2 * i + 1]\r\n        return True\r\
    \n\r\n    def answer(self):\r\n        return self.ans\r\n"
  dependsOn:
  - Graph\Decomposition\SCC_Tarjan.py
  isVerificationFile: false
  path: Graph\TwoSAT.py
  requiredBy: []
  timestamp: '2021-01-10 04:02:27+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\LibraryChecker\two_sat.test.py
documentation_of: Graph\TwoSAT.py
layout: document
title: 2-SAT
---
