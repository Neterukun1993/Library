---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/Decomposition/SCC_Tarjan.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3 (Tarjan\u306E\u30A2\u30EB\u30B4\
      \u30EA\u30BA\u30E0)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/two_sat.test.py
    title: TestCase/LibraryChecker/two_sat.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Graph.Decomposition.SCC_Tarjan import StronglyConnectedComponents\n\n\
    \nclass TwoSAT:\n    def __init__(self, n):\n        self.n = n\n        self.scc\
    \ = StronglyConnectedComponents(2 * n)\n        self.ans = [False] * self.n\n\n\
    \    def add_clause(self, i, f, j, g):\n        self.scc.add_edge(2 * i + int(not\
    \ f), 2 * j + int(g))\n        self.scc.add_edge(2 * j + int(not g), 2 * i + int(f))\n\
    \n    def satisfy(self):\n        self.scc.build()\n        for i in range(self.n):\n\
    \            if self.scc.labels[2 * i] == self.scc.labels[2 * i + 1]:\n      \
    \          return False\n            self.ans[i] = self.scc.labels[2 * i] < self.scc.labels[2\
    \ * i + 1]\n        return True\n\n    def answer(self):\n        return self.ans\n"
  dependsOn:
  - Graph/Decomposition/SCC_Tarjan.py
  isVerificationFile: false
  path: Graph/misc/TwoSAT.py
  requiredBy: []
  timestamp: '2021-01-24 18:01:48+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/two_sat.test.py
documentation_of: Graph/misc/TwoSAT.py
layout: document
title: 2-SAT
---
