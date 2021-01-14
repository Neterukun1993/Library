---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_3_C.Kosaraju.test.py
    title: TestCase/AOJ/GRL_3_C.Kosaraju.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/scc.Kosaraju.test.py
    title: TestCase/LibraryChecker/scc.Kosaraju.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.8.7/x64/lib/python3.8/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.8.7/x64/lib/python3.8/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class StronglyConnectedComponents:\n    def __init__(self, n):\n        self.n\
    \ = n\n        self.graph = [[] for _ in range(n)]\n        self.rev_graph = [[]\
    \ for _ in range(n)]\n        self.labels = [-1] * n\n        self.lb_cnt = 0\n\
    \n    def add_edge(self, v, nxt_v):\n        self.graph[v].append(nxt_v)\n   \
    \     self.rev_graph[nxt_v].append(v)\n\n    def build(self):\n        self.post_order\
    \ = []\n        self.used = [False] * self.n\n        for v in range(self.n):\n\
    \            if not self.used[v]:\n                self._dfs(v)\n\n        for\
    \ v in reversed(self.post_order):\n            if self.labels[v] == -1:\n    \
    \            self._rev_dfs(v)\n                self.lb_cnt += 1\n\n    def _dfs(self,\
    \ v):\n        stack = [v, 0]\n        while stack:\n            v, idx = stack[-2:]\n\
    \            if not idx and self.used[v]:\n                stack.pop()\n     \
    \           stack.pop()\n            else:\n                self.used[v] = True\n\
    \                if idx < len(self.graph[v]):\n                    stack[-1] +=\
    \ 1\n                    stack.append(self.graph[v][idx])\n                  \
    \  stack.append(0)\n                else:\n                    stack.pop()\n \
    \                   self.post_order.append(stack.pop())\n\n    def _rev_dfs(self,\
    \ v):\n        stack = [v]\n        self.labels[v] = self.lb_cnt\n        while\
    \ stack:\n            v = stack.pop()\n            for nxt_v in self.rev_graph[v]:\n\
    \                if self.labels[nxt_v] != -1:\n                    continue\n\
    \                stack.append(nxt_v)\n                self.labels[nxt_v] = self.lb_cnt\n\
    \n    def construct_dag(self):\n        self.dag = [[] for i in range(self.lb_cnt)]\n\
    \        self.groups = [[] for i in range(self.lb_cnt)]\n        for v, lb in\
    \ enumerate(self.labels):\n            for nxt_v in self.graph[v]:\n         \
    \       nxt_lb = self.labels[nxt_v]\n                if lb == nxt_lb:\n      \
    \              continue\n                self.dag[lb].append(nxt_lb)\n       \
    \     self.groups[lb].append(v)\n        return self.dag, self.groups\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Decomposition/SCC_Kosaraju.py
  requiredBy: []
  timestamp: '2021-01-09 01:09:35+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/GRL_3_C.Kosaraju.test.py
  - TestCase/LibraryChecker/scc.Kosaraju.test.py
documentation_of: Graph/Decomposition/SCC_Kosaraju.py
layout: document
title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3 (Kosaraju\u306E\u30A2\u30EB\u30B4\
  \u30EA\u30BA\u30E0)"
---
