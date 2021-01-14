---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/lca.EulerTour.test.py
    title: TestCase/LibraryChecker/lca.EulerTour.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class EulerTour:\n    def __init__(self, tree, root=None):\n        self.n\
    \ = len(tree)\n        self.tree = tree\n        self.par = [-1] * self.n\n  \
    \      self.begin = [-1] * self.n\n        self.end = [-1] * self.n\n        self.walk_order\
    \ = []\n\n        used = [False] * self.n\n        if root is None:\n        \
    \    for i in range(self.n):\n                if used[v]:\n                  \
    \  self._traversal(v, used)\n        else:\n            self._traversal(root,\
    \ used)\n\n    def _traversal(self, rt, used):\n        stack = [rt, 0]\n    \
    \    self.begin[rt] = len(self.walk_order)\n        self.walk_order.append(rt)\n\
    \        while stack:\n            v, idx = stack[-2:]\n            if idx < len(self.tree[v]):\n\
    \                nxt_v = self.tree[v][idx]\n                stack[-1] += 1\n \
    \               if nxt_v == self.par[v]:\n                    continue\n     \
    \           self.begin[nxt_v] = len(self.walk_order)\n                self.walk_order.append(nxt_v)\n\
    \                self.par[nxt_v] = v\n                stack.append(nxt_v)\n  \
    \              stack.append(0)\n            else:\n                self.end[v]\
    \ = len(self.walk_order) \n                if self.par[v] != -1:\n           \
    \         self.walk_order.append(self.par[v])\n                stack.pop()\n \
    \               stack.pop()\n\n    def build_lca(self):\n        self.depth =\
    \ self.walk_order[:]\n        d = 0\n        for i, (prv_v, v) in enumerate(zip(self.walk_order,\
    \ self.walk_order[1:])):\n            if self.par[v] == -1: d = 0\n          \
    \  elif self.par[v] == prv_v: d += 1\n            else: d -= 1\n            self.depth[i\
    \ + 1] = (d << 32) + v\n        self._build_rmq()\n\n    def _build_rmq(self):\n\
    \        size = len(self.depth)\n        lg_size = size.bit_length()\n       \
    \ self.lg = [0] * (size + 1)\n        for i in range(2, size + 1):\n         \
    \   self.lg[i] = self.lg[i // 2] + 1\n\n        self.tbl = [[0] * size for _ in\
    \ range(lg_size)]\n        tbl = self.tbl\n        for i, val in enumerate(self.depth):\n\
    \            tbl[0][i] = val\n        for k in range(lg_size - 1):\n         \
    \   for i in range(size - (1 << k + 1) + 1):\n                tbl[k + 1][i] =\
    \ min(tbl[k][i], tbl[k][i + (1 << k)])\n\n    def _min_query(self, l, r):\n  \
    \      k = self.lg[r - l]\n        return min(self.tbl[k][l], self.tbl[k][r -\
    \ (1 << k)])                \n\n    def lca(self, u, v):\n        if self.begin[u]\
    \ > self.begin[v]:\n            u, v = v, u\n        l, r = self.begin[u], self.begin[v]\
    \ + 1\n        lca_uv = self._min_query(l, r) & ((1 << 32) - 1)\n        return\
    \ lca_uv\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Tree/EulerTour.py
  requiredBy: []
  timestamp: '2021-01-07 06:39:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/lca.EulerTour.test.py
documentation_of: Graph/Tree/EulerTour.py
layout: document
title: "\u30AA\u30A4\u30E9\u30FC\u30C4\u30A2\u30FC (LCA)"
---
