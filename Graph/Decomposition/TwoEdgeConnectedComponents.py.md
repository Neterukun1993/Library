---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\LowLink.py
    title: "\u95A2\u7BC0\u70B9\u30FB\u6A4B\u306E\u5217\u6319\u3001DFS\u6728\u306E\u69CB\
      \u7BC9 (LowLink)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\two_edge_connected_components.test.py
    title: TestCase\LibraryChecker\two_edge_connected_components.test.py
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
  code: "from Graph.LowLink import LowLink\r\n\r\n\r\nclass TwoEdgeConnectedComponents(LowLink):\r\
    \n    def build(self):\r\n        super().build()\r\n        self.labels = [-1]\
    \ * self.n\r\n        self.lb_cnt = 0\r\n        for v in range(self.n):\r\n \
    \           if self.labels[v] != -1:\r\n                continue\r\n         \
    \   self.labels[v] = self.lb_cnt\r\n            stack = [v]\r\n            while\
    \ stack:\r\n                v = stack.pop()\r\n                for nxt_v in self.graph[v]:\r\
    \n                    if self.ord[v] < self.low[nxt_v] or self.ord[nxt_v] < self.low[v]:\r\
    \n                        continue\r\n                    if self.labels[nxt_v]\
    \ != -1:\r\n                        continue\r\n                    self.labels[nxt_v]\
    \ = self.lb_cnt\r\n                    stack.append(nxt_v)\r\n            self.lb_cnt\
    \ += 1\r\n\r\n    def groups(self):\r\n        res = [[] for _ in range(self.lb_cnt)]\r\
    \n        for v, lb in enumerate(self.labels):\r\n            res[lb].append(v)\r\
    \n        return res\r\n"
  dependsOn:
  - Graph\LowLink.py
  isVerificationFile: false
  path: Graph\Decomposition\TwoEdgeConnectedComponents.py
  requiredBy: []
  timestamp: '2021-01-10 06:54:35+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\LibraryChecker\two_edge_connected_components.test.py
documentation_of: Graph\Decomposition\TwoEdgeConnectedComponents.py
layout: document
title: "\u4E8C\u91CD\u8FBA\u9023\u7D50\u6210\u5206\u5206\u89E3"
---
