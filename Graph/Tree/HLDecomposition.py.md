---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\2667.test.py
    title: TestCase\AOJ\2667.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\GRL_5_D.test.py
    title: TestCase\AOJ\GRL_5_D.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\GRL_5_E.test.py
    title: TestCase\AOJ\GRL_5_E.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\lca.HLDecomposition.test.py
    title: TestCase\LibraryChecker\lca.HLDecomposition.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\vertex_add_path_sum.test.py
    title: TestCase\LibraryChecker\vertex_add_path_sum.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\vertex_add_subtree_sum.test.py
    title: TestCase\LibraryChecker\vertex_add_subtree_sum.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\yukicoder\yuki0922.HLDecomposition.test.py
    title: TestCase\yukicoder\yuki0922.HLDecomposition.test.py
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
  code: "class HLDecomposition:\r\n    def __init__(self, tree):\r\n        self.tree\
    \ = tree\r\n        self.n = len(tree)\r\n        self.par = [-1] * self.n\r\n\
    \        self.size = [1] * self.n\r\n        self.depth = [0] * self.n\r\n   \
    \     self.preorder = [0] * self.n\r\n        self.head = [i for i in range(self.n)]\r\
    \n        self.k = 0\r\n\r\n        for v in range(self.n):\r\n            if\
    \ self.par[v] == -1:\r\n                self._dfs_pre(v)\r\n                self._dfs_hld(v)\r\
    \n\r\n    def __getitem__(self, v):\r\n        return self.preorder[v]\r\n\r\n\
    \    def _dfs_pre(self, v):\r\n        tree = self.tree\r\n        stack = [v]\r\
    \n        order = [v]\r\n        while stack:\r\n            v = stack.pop()\r\
    \n            for chi_v in tree[v]:\r\n                if chi_v == self.par[v]:\r\
    \n                    continue\r\n                self.par[chi_v] = v\r\n    \
    \            self.depth[chi_v] = self.depth[v] + 1\r\n                stack.append(chi_v)\r\
    \n                order.append(chi_v)\r\n\r\n        for v in reversed(order):\r\
    \n            tree_v = tree[v]\r\n            if len(tree_v) and tree_v[0] ==\
    \ self.par[v]:\r\n                tree_v[0], tree_v[-1] = tree_v[-1], tree_v[0]\r\
    \n            for idx, chi_v in enumerate(tree_v):\r\n                if chi_v\
    \ == self.par[v]:\r\n                    continue\r\n                self.size[v]\
    \ += self.size[chi_v]\r\n                if self.size[chi_v] > self.size[tree_v[0]]:\r\
    \n                    tree_v[idx], tree_v[0] = tree_v[0], tree_v[idx]\r\n\r\n\
    \    def _dfs_hld(self, v):\r\n        stack = [v]\r\n        while stack:\r\n\
    \            v = stack.pop()\r\n            self.preorder[v] = self.k\r\n    \
    \        self.k += 1\r\n            if len(self.tree[v]) == 0:\r\n           \
    \     continue\r\n            top = self.tree[v][0]\r\n            for chi_v in\
    \ reversed(self.tree[v]):\r\n                if chi_v == self.par[v]:\r\n    \
    \                continue\r\n                if chi_v == top:\r\n            \
    \        self.head[chi_v] = self.head[v]\r\n                else:\r\n        \
    \            self.head[chi_v] = chi_v\r\n                stack.append(chi_v)\r\
    \n\r\n    def lca(self, u, v):\r\n        while u != -1 and v != -1:\r\n     \
    \       if self.preorder[u] > self.preorder[v]:\r\n                u, v = v, u\r\
    \n            if self.head[u] == self.head[v]:\r\n                return u\r\n\
    \            v = self.par[self.head[v]]\r\n        return -1\r\n\r\n    def distance(self,\
    \ u, v):\r\n        lca_uv = self.lca(u, v)\r\n        if lca_uv == -1:\r\n  \
    \          return -1\r\n        else:\r\n            return self.depth[u] + self.depth[v]\
    \ - 2 * self.depth[lca_uv]\r\n\r\n    def range_vertex_path(self, u, v):\r\n \
    \       while True:\r\n            if self.preorder[u] > self.preorder[v]:\r\n\
    \                u, v = v, u\r\n            l = max(self.preorder[self.head[v]],\
    \ self.preorder[u])\r\n            r = self.preorder[v]\r\n            yield l,\
    \ r + 1\r\n            if self.head[u] != self.head[v]:\r\n                v =\
    \ self.par[self.head[v]]\r\n            else:\r\n                return\r\n\r\n\
    \    def range_edge_path(self, u, v):\r\n        while True:\r\n            if\
    \ self.preorder[u] > self.preorder[v]:\r\n                u, v = v, u\r\n    \
    \        if self.head[u] != self.head[v]:\r\n                yield self.preorder[self.head[v]],\
    \ self.preorder[v] + 1\r\n                v = self.par[self.head[v]]\r\n     \
    \       else:\r\n                if u != v:\r\n                    yield self.preorder[u]\
    \ + 1, self.preorder[v] + 1\r\n                break\r\n\r\n    def range_subtree(self,\
    \ u):\r\n        return self.preorder[u], self.preorder[u] + self.size[u]\r\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph\Tree\HLDecomposition.py
  requiredBy: []
  timestamp: '2021-01-16 03:42:28+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\2667.test.py
  - TestCase\AOJ\GRL_5_D.test.py
  - TestCase\AOJ\GRL_5_E.test.py
  - TestCase\LibraryChecker\lca.HLDecomposition.test.py
  - TestCase\LibraryChecker\vertex_add_path_sum.test.py
  - TestCase\LibraryChecker\vertex_add_subtree_sum.test.py
  - TestCase\yukicoder\yuki0922.HLDecomposition.test.py
documentation_of: Graph\Tree\HLDecomposition.py
layout: document
title: "HL\u5206\u89E3 (Heavy-Light Decomposition)"
---
