---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\GRL_3_C.Kosaraju.test.py
    title: TestCase\AOJ\GRL_3_C.Kosaraju.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\scc.Kosaraju.test.py
    title: TestCase\LibraryChecker\scc.Kosaraju.test.py
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
    \    self.n = n\r\n        self.graph = [[] for _ in range(n)]\r\n        self.rev_graph\
    \ = [[] for _ in range(n)]\r\n        self.labels = [-1] * n\r\n        self.lb_cnt\
    \ = 0\r\n\r\n    def add_edge(self, v, nxt_v):\r\n        self.graph[v].append(nxt_v)\r\
    \n        self.rev_graph[nxt_v].append(v)\r\n\r\n    def build(self):\r\n    \
    \    self.post_order = []\r\n        self.used = [False] * self.n\r\n        for\
    \ v in range(self.n):\r\n            if not self.used[v]:\r\n                self._dfs(v)\r\
    \n\r\n        for v in reversed(self.post_order):\r\n            if self.labels[v]\
    \ == -1:\r\n                self._rev_dfs(v)\r\n                self.lb_cnt +=\
    \ 1\r\n\r\n    def _dfs(self, v):\r\n        stack = [v, 0]\r\n        while stack:\r\
    \n            v, idx = stack[-2:]\r\n            if not idx and self.used[v]:\r\
    \n                stack.pop()\r\n                stack.pop()\r\n            else:\r\
    \n                self.used[v] = True\r\n                if idx < len(self.graph[v]):\r\
    \n                    stack[-1] += 1\r\n                    stack.append(self.graph[v][idx])\r\
    \n                    stack.append(0)\r\n                else:\r\n           \
    \         stack.pop()\r\n                    self.post_order.append(stack.pop())\r\
    \n\r\n    def _rev_dfs(self, v):\r\n        stack = [v]\r\n        self.labels[v]\
    \ = self.lb_cnt\r\n        while stack:\r\n            v = stack.pop()\r\n   \
    \         for nxt_v in self.rev_graph[v]:\r\n                if self.labels[nxt_v]\
    \ != -1:\r\n                    continue\r\n                stack.append(nxt_v)\r\
    \n                self.labels[nxt_v] = self.lb_cnt\r\n\r\n    def construct_dag(self):\r\
    \n        self.dag = [[] for i in range(self.lb_cnt)]\r\n        self.groups =\
    \ [[] for i in range(self.lb_cnt)]\r\n        for v, lb in enumerate(self.labels):\r\
    \n            for nxt_v in self.graph[v]:\r\n                nxt_lb = self.labels[nxt_v]\r\
    \n                if lb == nxt_lb:\r\n                    continue\r\n       \
    \         self.dag[lb].append(nxt_lb)\r\n            self.groups[lb].append(v)\r\
    \n        return self.dag, self.groups\r\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph\Decomposition\SCC_Kosaraju.py
  requiredBy: []
  timestamp: '2021-01-09 01:09:35+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\GRL_3_C.Kosaraju.test.py
  - TestCase\LibraryChecker\scc.Kosaraju.test.py
documentation_of: Graph\Decomposition\SCC_Kosaraju.py
layout: document
title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3 (Kosaraju\u306E\u30A2\u30EB\u30B4\
  \u30EA\u30BA\u30E0)"
---
