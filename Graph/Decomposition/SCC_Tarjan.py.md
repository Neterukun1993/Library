---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: Graph\TwoSAT.py
    title: 2-SAT
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\GRL_3_C.Tarjan.test.py
    title: TestCase\AOJ\GRL_3_C.Tarjan.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\scc.Tarjan.test.py
    title: TestCase\LibraryChecker\scc.Tarjan.test.py
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
  code: "class StronglyConnectedComponents:\r\n    def __init__(self, n):\r\n    \
    \    self.n = n\r\n        self.graph = [[] for _ in range(n)]\r\n        self.ord\
    \ = [-1] * n\r\n        self.low = [-1] * n\r\n        self.labels = [-1] * n\r\
    \n        self.lb_cnt = 0\r\n\r\n    def add_edge(self, v, nxt_v):\r\n       \
    \ self.graph[v].append(nxt_v)\r\n\r\n    def build(self):\r\n        k = 0\r\n\
    \        idxs = [0] * self.n\r\n        for v in range(self.n):\r\n          \
    \  if self.ord[v] == -1:\r\n                k = self.dfs(v, k, idxs)\r\n     \
    \   self.labels = [self.lb_cnt - lb - 1 for lb in self.labels]\r\n\r\n    def\
    \ dfs(self, root, k, idxs):\r\n        dfs_stack = [root]\r\n        scc_stack\
    \ = []\r\n        while dfs_stack:\r\n            v = dfs_stack[-1]\r\n      \
    \      if v < 0:\r\n                v = ~v\r\n                prv_v = dfs_stack[-2]\r\
    \n                self.low[prv_v] = min(self.low[prv_v], self.low[v])\r\n    \
    \            dfs_stack.pop()\r\n                continue\r\n            idx =\
    \ idxs[v]\r\n            if self.ord[v] == -1:\r\n                self.ord[v]\
    \ = self.low[v] = k\r\n                k += 1\r\n                scc_stack.append(v)\r\
    \n            if idx < len(self.graph[v]):\r\n                nxt_v = self.graph[v][idx]\r\
    \n                idxs[v] += 1\r\n                if self.ord[nxt_v] == -1:\r\n\
    \                    dfs_stack.append(~nxt_v)\r\n                    dfs_stack.append(nxt_v)\r\
    \n                elif self.labels[nxt_v] == -1:\r\n                    self.low[v]\
    \ = min(self.low[v], self.ord[nxt_v])\r\n            else:\r\n               \
    \ if self.ord[v] == self.low[v]:\r\n                    while True:\r\n      \
    \                  prv_v = scc_stack.pop()\r\n                        self.labels[prv_v]\
    \ = self.lb_cnt\r\n                        if prv_v == v:\r\n                \
    \            break\r\n                    self.lb_cnt += 1\r\n               \
    \ dfs_stack.pop()\r\n        return k\r\n\r\n    def construct_dag(self):\r\n\
    \        self.dag = [[] for i in range(self.lb_cnt)]\r\n        self.groups =\
    \ [[] for i in range(self.lb_cnt)]\r\n        for v, lb in enumerate(self.labels):\r\
    \n            for nxt_v in self.graph[v]:\r\n                nxt_lb = self.labels[nxt_v]\r\
    \n                if lb == nxt_lb:\r\n                    continue\r\n       \
    \         self.dag[lb].append(nxt_lb)\r\n            self.groups[lb].append(v)\r\
    \n        return self.dag, self.groups\r\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph\Decomposition\SCC_Tarjan.py
  requiredBy:
  - Graph\TwoSAT.py
  timestamp: '2021-01-08 06:36:19+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\GRL_3_C.Tarjan.test.py
  - TestCase\LibraryChecker\scc.Tarjan.test.py
documentation_of: Graph\Decomposition\SCC_Tarjan.py
layout: document
title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3 (Tarjan\u306E\u30A2\u30EB\u30B4\
  \u30EA\u30BA\u30E0)"
---
