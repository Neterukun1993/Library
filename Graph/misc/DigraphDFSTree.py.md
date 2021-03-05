---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_11_B.test.py
    title: TestCase/AOJ/ALDS1_11_B.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class DigraphDFSTree:\n    def __init__(self, n):\n        self.n = n\n \
    \       self.digraph = [[] for _ in range(n)]\n        self.dfstree = [[] for\
    \ _ in range(n)]\n        self.par = [-1] * n\n        self.arrival = [-1] * n\n\
    \        self.depature = [-1] * n\n        self.roots = set()\n\n    def add_edge(self,\
    \ v, nxt_v):\n        self.digraph[v].append(nxt_v)\n\n    def build(self, root=None):\n\
    \        k = 0\n        idxs = [0] * self.n\n        if root is not None:\n  \
    \          self.roots.add(v)\n            self._dfs(v, idxs, k)\n        else:\n\
    \            for v in range(self.n):\n                if self.arrival[v] == -1:\n\
    \                    self.roots.add(v)\n                    k = self._dfs(v, idxs,\
    \ k)\n\n    def _dfs(self, root, idxs, k):\n        stack = [root]\n        while\
    \ stack:\n            v = stack[-1]\n            idx = idxs[v]\n            if\
    \ self.arrival[v] == -1:\n                self.arrival[v] = k\n              \
    \  k += 1\n            if idx < len(self.digraph[v]):\n                nxt_v =\
    \ self.digraph[v][idx]\n                idxs[v] += 1\n                if self.arrival[nxt_v]\
    \ == -1:\n                    self.dfstree[v].append(nxt_v)\n                \
    \    self.par[nxt_v] = v\n                    stack.append(nxt_v)\n          \
    \  else:\n                self.depature[v] = k\n                k += 1\n     \
    \           stack.pop()\n        return k\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/misc/DigraphDFSTree.py
  requiredBy: []
  timestamp: '2021-01-25 23:26:41+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_11_B.test.py
documentation_of: Graph/misc/DigraphDFSTree.py
layout: document
title: "\u6709\u5411\u30B0\u30E9\u30D5\u306EDFS\u6728\u306E\u69CB\u7BC9"
---
