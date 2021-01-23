---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: Graph\Decomposition\TwoEdgeConnectedComponents.py
    title: "\u4E8C\u91CD\u8FBA\u9023\u7D50\u6210\u5206\u5206\u89E3"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\GRL_3_A.test.py
    title: TestCase\AOJ\GRL_3_A.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\GRL_3_B.test.py
    title: TestCase\AOJ\GRL_3_B.test.py
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
  code: "class LowLink:\r\n    def __init__(self, n):\r\n        self.n = n\r\n  \
    \      self.graph = [[] for _ in range(n)]\r\n        self.dfstree = [[] for _\
    \ in range(n)]\r\n        self.par = [-1] * n\r\n        self.ord = [-1] * n\r\
    \n        self.low = [-1] * n\r\n        self.articulations = []\r\n        self.bridges\
    \ = []\r\n        self.roots = set()\r\n\r\n    def add_edge(self, u, v):\r\n\
    \        self.graph[u].append(v)\r\n        self.graph[v].append(u)\r\n\r\n  \
    \  def build(self):\r\n        k = 0\r\n        self.edge_cnt = {}\r\n       \
    \ for v in range(self.n):\r\n            for nxt_v in self.graph[v]:\r\n     \
    \           self.edge_cnt[v, nxt_v] = self.edge_cnt.get((v, nxt_v), 0) + 1\r\n\
    \        idxs = [0] * self.n\r\n        arts = [False] * self.n\r\n        for\
    \ v in range(self.n):\r\n            if self.ord[v] == -1:\r\n               \
    \ self.roots.add(v)\r\n                k = self._dfs(v, idxs, arts, k)\r\n\r\n\
    \    def _dfs(self, root, idxs, arts, k):\r\n        stack = [root]\r\n      \
    \  while stack:\r\n            v = stack[-1]\r\n            if v < 0:\r\n    \
    \            v = ~v\r\n                par_v = self.par[v]\r\n               \
    \ self.low[par_v] = min(self.low[par_v], self.low[v])\r\n                arts[par_v]\
    \ |= (self.par[par_v] != -1 and self.ord[par_v] <= self.low[v])\r\n          \
    \      if self.ord[par_v] < self.low[v]:\r\n                    self.bridges.append((par_v,\
    \ v))\r\n                stack.pop()\r\n                continue\r\n         \
    \   idx = idxs[v]\r\n            if self.ord[v] == -1:\r\n                self.ord[v]\
    \ = self.low[v] = k\r\n                k += 1\r\n            if idx < len(self.graph[v]):\r\
    \n                nxt_v = self.graph[v][idx]\r\n                idxs[v] += 1\r\
    \n                if nxt_v == self.par[v] and self.edge_cnt[v, nxt_v] == 1:\r\n\
    \                    continue \r\n                elif self.ord[nxt_v] == -1:\r\
    \n                    self.dfstree[v].append(nxt_v)\r\n                    self.dfstree[nxt_v].append(v)\r\
    \n                    self.par[nxt_v] = v\r\n                    stack.append(~nxt_v)\r\
    \n                    stack.append(nxt_v)\r\n                else:\r\n       \
    \             self.low[v] = min(self.low[v], self.ord[nxt_v])\r\n            else:\r\
    \n                arts[v] |= (root == v and len(self.dfstree[v]) >= 2)\r\n   \
    \             if arts[v]:\r\n                    self.articulations.append(v)\r\
    \n                stack.pop()\r\n        return k\r\n\r\n    def enumerate_articulations(self):\r\
    \n        for v in self.articulations:\r\n            yield v\r\n\r\n    def enumerate_bridges(self):\r\
    \n        for u, v in self.bridges:\r\n            yield u, v\r\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph\LowLink.py
  requiredBy:
  - Graph\Decomposition\TwoEdgeConnectedComponents.py
  timestamp: '2021-01-10 06:06:37+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\GRL_3_A.test.py
  - TestCase\AOJ\GRL_3_B.test.py
documentation_of: Graph\LowLink.py
layout: document
title: "\u95A2\u7BC0\u70B9\u30FB\u6A4B\u306E\u5217\u6319\u3001DFS\u6728\u306E\u69CB\
  \u7BC9 (LowLink)"
---
