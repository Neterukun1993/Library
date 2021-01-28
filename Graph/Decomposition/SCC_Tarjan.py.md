---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: Graph/misc/TwoSAT.py
    title: 2-SAT
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_3_C.Tarjan.test.py
    title: TestCase/AOJ/GRL_3_C.Tarjan.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/scc.Tarjan.test.py
    title: TestCase/LibraryChecker/scc.Tarjan.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class StronglyConnectedComponents:\n    def __init__(self, n):\n        self.n\
    \ = n\n        self.graph = [[] for _ in range(n)]\n        self.ord = [-1] *\
    \ n\n        self.low = [-1] * n\n        self.labels = [-1] * n\n        self.lb_cnt\
    \ = 0\n\n    def add_edge(self, v, nxt_v):\n        self.graph[v].append(nxt_v)\n\
    \n    def build(self):\n        k = 0\n        idxs = [0] * self.n\n        for\
    \ v in range(self.n):\n            if self.ord[v] == -1:\n                k =\
    \ self.dfs(v, k, idxs)\n        self.labels = [self.lb_cnt - lb - 1 for lb in\
    \ self.labels]\n\n    def dfs(self, root, k, idxs):\n        dfs_stack = [root]\n\
    \        scc_stack = []\n        while dfs_stack:\n            v = dfs_stack[-1]\n\
    \            if v < 0:\n                v = ~v\n                prv_v = dfs_stack[-2]\n\
    \                self.low[prv_v] = min(self.low[prv_v], self.low[v])\n       \
    \         dfs_stack.pop()\n                continue\n            idx = idxs[v]\n\
    \            if self.ord[v] == -1:\n                self.ord[v] = self.low[v]\
    \ = k\n                k += 1\n                scc_stack.append(v)\n         \
    \   if idx < len(self.graph[v]):\n                nxt_v = self.graph[v][idx]\n\
    \                idxs[v] += 1\n                if self.ord[nxt_v] == -1:\n   \
    \                 dfs_stack.append(~nxt_v)\n                    dfs_stack.append(nxt_v)\n\
    \                elif self.labels[nxt_v] == -1:\n                    self.low[v]\
    \ = min(self.low[v], self.ord[nxt_v])\n            else:\n                if self.ord[v]\
    \ == self.low[v]:\n                    while True:\n                        prv_v\
    \ = scc_stack.pop()\n                        self.labels[prv_v] = self.lb_cnt\n\
    \                        if prv_v == v:\n                            break\n \
    \                   self.lb_cnt += 1\n                dfs_stack.pop()\n      \
    \  return k\n\n    def construct_dag(self):\n        self.dag = [[] for i in range(self.lb_cnt)]\n\
    \        self.groups = [[] for i in range(self.lb_cnt)]\n        for v, lb in\
    \ enumerate(self.labels):\n            for nxt_v in self.graph[v]:\n         \
    \       nxt_lb = self.labels[nxt_v]\n                if lb == nxt_lb:\n      \
    \              continue\n                self.dag[lb].append(nxt_lb)\n       \
    \     self.groups[lb].append(v)\n        return self.dag, self.groups\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Decomposition/SCC_Tarjan.py
  requiredBy:
  - Graph/misc/TwoSAT.py
  timestamp: '2021-01-08 06:36:19+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/GRL_3_C.Tarjan.test.py
  - TestCase/LibraryChecker/scc.Tarjan.test.py
documentation_of: Graph/Decomposition/SCC_Tarjan.py
layout: document
title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3 (Tarjan\u306E\u30A2\u30EB\u30B4\
  \u30EA\u30BA\u30E0)"
---
