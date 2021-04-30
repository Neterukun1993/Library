---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Flow.Dinic import Dinic\n\n\nclass BipartiteGraph:\n    def __init__(self,\
    \ na, nb):\n        self.na = na\n        self.nb = nb\n        self.n = (na +\
    \ nb + 2)\n        self.s, self.t = self.n - 2, self.n - 1\n        self.dc =\
    \ Dinic(self.n)\n        for va in range(na):\n            self.dc.add_edge(self.s,\
    \ va, 1)\n        for vb in range(na, na + nb):\n            self.dc.add_edge(vb,\
    \ self.t, 1)\n\n    def add_edge(self, ia, ib):\n        self.dc.add_edge(ia,\
    \ self.na + ib, 1)\n\n    def maximum_matching(self):\n        return self.dc.max_flow(self.s,\
    \ self.t)\n\n    def matching_edges(self):\n        edges = []\n        for ia\
    \ in range(self.na):\n            for ib, _, val in self.dc.graph[ia]:\n     \
    \           if ib == self.s:\n                    continue\n                if\
    \ val == 0:\n                    edges.append((ia, ib - self.na))\n        return\
    \ edges\n"
  dependsOn: []
  isVerificationFile: false
  path: Flow/BipartiteGraph.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Flow/BipartiteGraph.py
layout: document
redirect_from:
- /library/Flow/BipartiteGraph.py
- /library/Flow/BipartiteGraph.py.html
title: Flow/BipartiteGraph.py
---
