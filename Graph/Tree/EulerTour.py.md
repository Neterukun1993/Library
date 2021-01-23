---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\lca.EulerTour.test.py
    title: TestCase\LibraryChecker\lca.EulerTour.test.py
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
  code: "class EulerTour:\r\n    def __init__(self, tree, root=None):\r\n        self.n\
    \ = len(tree)\r\n        self.tree = tree\r\n        self.par = [-1] * self.n\r\
    \n        self.begin = [-1] * self.n\r\n        self.end = [-1] * self.n\r\n \
    \       self.walk_order = []\r\n\r\n        used = [False] * self.n\r\n      \
    \  if root is None:\r\n            for i in range(self.n):\r\n               \
    \ if used[v]:\r\n                    self._traversal(v, used)\r\n        else:\r\
    \n            self._traversal(root, used)\r\n\r\n    def _traversal(self, rt,\
    \ used):\r\n        stack = [rt, 0]\r\n        self.begin[rt] = len(self.walk_order)\r\
    \n        self.walk_order.append(rt)\r\n        while stack:\r\n            v,\
    \ idx = stack[-2:]\r\n            if idx < len(self.tree[v]):\r\n            \
    \    nxt_v = self.tree[v][idx]\r\n                stack[-1] += 1\r\n         \
    \       if nxt_v == self.par[v]:\r\n                    continue\r\n         \
    \       self.begin[nxt_v] = len(self.walk_order)\r\n                self.walk_order.append(nxt_v)\r\
    \n                self.par[nxt_v] = v\r\n                stack.append(nxt_v)\r\
    \n                stack.append(0)\r\n            else:\r\n                self.end[v]\
    \ = len(self.walk_order) \r\n                if self.par[v] != -1:\r\n       \
    \             self.walk_order.append(self.par[v])\r\n                stack.pop()\r\
    \n                stack.pop()\r\n\r\n    def build_lca(self):\r\n        self.depth\
    \ = self.walk_order[:]\r\n        d = 0\r\n        for i, (prv_v, v) in enumerate(zip(self.walk_order,\
    \ self.walk_order[1:])):\r\n            if self.par[v] == -1: d = 0\r\n      \
    \      elif self.par[v] == prv_v: d += 1\r\n            else: d -= 1\r\n     \
    \       self.depth[i + 1] = (d << 32) + v\r\n        self._build_rmq()\r\n\r\n\
    \    def _build_rmq(self):\r\n        size = len(self.depth)\r\n        lg_size\
    \ = size.bit_length()\r\n        self.lg = [0] * (size + 1)\r\n        for i in\
    \ range(2, size + 1):\r\n            self.lg[i] = self.lg[i // 2] + 1\r\n\r\n\
    \        self.tbl = [[0] * size for _ in range(lg_size)]\r\n        tbl = self.tbl\r\
    \n        for i, val in enumerate(self.depth):\r\n            tbl[0][i] = val\r\
    \n        for k in range(lg_size - 1):\r\n            for i in range(size - (1\
    \ << k + 1) + 1):\r\n                tbl[k + 1][i] = min(tbl[k][i], tbl[k][i +\
    \ (1 << k)])\r\n\r\n    def _min_query(self, l, r):\r\n        k = self.lg[r -\
    \ l]\r\n        return min(self.tbl[k][l], self.tbl[k][r - (1 << k)])        \
    \        \r\n\r\n    def lca(self, u, v):\r\n        if self.begin[u] > self.begin[v]:\r\
    \n            u, v = v, u\r\n        l, r = self.begin[u], self.begin[v] + 1\r\
    \n        lca_uv = self._min_query(l, r) & ((1 << 32) - 1)\r\n        return lca_uv\r\
    \n"
  dependsOn: []
  isVerificationFile: false
  path: Graph\Tree\EulerTour.py
  requiredBy: []
  timestamp: '2021-01-07 06:39:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\LibraryChecker\lca.EulerTour.test.py
documentation_of: Graph\Tree\EulerTour.py
layout: document
title: "\u30AA\u30A4\u30E9\u30FC\u30C4\u30A2\u30FC (LCA)"
---
