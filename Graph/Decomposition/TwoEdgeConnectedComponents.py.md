---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: TestCase/LibraryChecker/two_edge_connected_components.test.py
    title: TestCase/LibraryChecker/two_edge_connected_components.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Graph.LowLink import LowLink\n\n\nclass TwoEdgeConnectedComponents(LowLink):\n\
    \    def build(self):\n        super().build()\n        self.labels = [-1] * self.n\n\
    \        self.lb_cnt = 0\n        for v in range(self.n):\n            if self.labels[v]\
    \ != -1:\n                continue\n            self.labels[v] = self.lb_cnt\n\
    \            stack = [v]\n            while stack:\n                v = stack.pop()\n\
    \                for nxt_v in self.graph[v]:\n                    if self.ord[v]\
    \ < self.low[nxt_v] or self.ord[nxt_v] < self.low[v]:\n                      \
    \  continue\n                    if self.labels[nxt_v] != -1:\n              \
    \          continue\n                    self.labels[nxt_v] = self.lb_cnt\n  \
    \                  stack.append(nxt_v)\n            self.lb_cnt += 1\n\n    def\
    \ groups(self):\n        res = [[] for _ in range(self.lb_cnt)]\n        for v,\
    \ lb in enumerate(self.labels):\n            res[lb].append(v)\n        return\
    \ res\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Decomposition/TwoEdgeConnectedComponents.py
  requiredBy: []
  timestamp: '2021-01-10 06:54:35+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - TestCase/LibraryChecker/two_edge_connected_components.test.py
documentation_of: Graph/Decomposition/TwoEdgeConnectedComponents.py
layout: document
title: "\u4E8C\u91CD\u8FBA\u9023\u7D50\u6210\u5206\u5206\u89E3"
---
