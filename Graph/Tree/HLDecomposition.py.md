---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/2667.test.py
    title: TestCase/AOJ/2667.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_5_D.test.py
    title: TestCase/AOJ/GRL_5_D.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_5_E.test.py
    title: TestCase/AOJ/GRL_5_E.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/lca.HLDecomposition.test.py
    title: TestCase/LibraryChecker/lca.HLDecomposition.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/vertex_add_path_sum.test.py
    title: TestCase/LibraryChecker/vertex_add_path_sum.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/vertex_add_subtree_sum.test.py
    title: TestCase/LibraryChecker/vertex_add_subtree_sum.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0922.HLDecomposition.test.py
    title: TestCase/yukicoder/yuki0922.HLDecomposition.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class HLDecomposition:\n    def __init__(self, tree):\n        self.tree\
    \ = tree\n        self.n = len(tree)\n        self.par = [-1] * self.n\n     \
    \   self.size = [1] * self.n\n        self.depth = [0] * self.n\n        self.preorder\
    \ = [0] * self.n\n        self.head = [i for i in range(self.n)]\n        self.k\
    \ = 0\n\n        for v in range(self.n):\n            if self.par[v] == -1:\n\
    \                self._dfs_pre(v)\n                self._dfs_hld(v)\n\n    def\
    \ __getitem__(self, v):\n        return self.preorder[v]\n\n    def _dfs_pre(self,\
    \ v):\n        tree = self.tree\n        stack = [v]\n        order = [v]\n  \
    \      while stack:\n            v = stack.pop()\n            for chi_v in tree[v]:\n\
    \                if chi_v == self.par[v]:\n                    continue\n    \
    \            self.par[chi_v] = v\n                self.depth[chi_v] = self.depth[v]\
    \ + 1\n                stack.append(chi_v)\n                order.append(chi_v)\n\
    \n        for v in reversed(order):\n            tree_v = tree[v]\n          \
    \  if len(tree_v) and tree_v[0] == self.par[v]:\n                tree_v[0], tree_v[-1]\
    \ = tree_v[-1], tree_v[0]\n            for idx, chi_v in enumerate(tree_v):\n\
    \                if chi_v == self.par[v]:\n                    continue\n    \
    \            self.size[v] += self.size[chi_v]\n                if self.size[chi_v]\
    \ > self.size[tree_v[0]]:\n                    tree_v[idx], tree_v[0] = tree_v[0],\
    \ tree_v[idx]\n\n    def _dfs_hld(self, v):\n        stack = [v]\n        while\
    \ stack:\n            v = stack.pop()\n            self.preorder[v] = self.k\n\
    \            self.k += 1\n            if len(self.tree[v]) == 0:\n           \
    \     continue\n            top = self.tree[v][0]\n            for chi_v in reversed(self.tree[v]):\n\
    \                if chi_v == self.par[v]:\n                    continue\n    \
    \            if chi_v == top:\n                    self.head[chi_v] = self.head[v]\n\
    \                else:\n                    self.head[chi_v] = chi_v\n       \
    \         stack.append(chi_v)\n\n    def lca(self, u, v):\n        while u !=\
    \ -1 and v != -1:\n            if self.preorder[u] > self.preorder[v]:\n     \
    \           u, v = v, u\n            if self.head[u] == self.head[v]:\n      \
    \          return u\n            v = self.par[self.head[v]]\n        return -1\n\
    \n    def distance(self, u, v):\n        lca_uv = self.lca(u, v)\n        if lca_uv\
    \ == -1:\n            return -1\n        else:\n            return self.depth[u]\
    \ + self.depth[v] - 2 * self.depth[lca_uv]\n\n    def range_vertex_path(self,\
    \ u, v):\n        while True:\n            if self.preorder[u] > self.preorder[v]:\n\
    \                u, v = v, u\n            l = max(self.preorder[self.head[v]],\
    \ self.preorder[u])\n            r = self.preorder[v]\n            yield l, r\
    \ + 1\n            if self.head[u] != self.head[v]:\n                v = self.par[self.head[v]]\n\
    \            else:\n                return\n\n    def range_edge_path(self, u,\
    \ v):\n        while True:\n            if self.preorder[u] > self.preorder[v]:\n\
    \                u, v = v, u\n            if self.head[u] != self.head[v]:\n \
    \               yield self.preorder[self.head[v]], self.preorder[v] + 1\n    \
    \            v = self.par[self.head[v]]\n            else:\n                if\
    \ u != v:\n                    yield self.preorder[u] + 1, self.preorder[v] +\
    \ 1\n                break\n\n    def range_subtree(self, u):\n        return\
    \ self.preorder[u], self.preorder[u] + self.size[u]\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Tree/HLDecomposition.py
  requiredBy: []
  timestamp: '2021-01-16 03:42:28+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki0922.HLDecomposition.test.py
  - TestCase/AOJ/GRL_5_D.test.py
  - TestCase/AOJ/2667.test.py
  - TestCase/AOJ/GRL_5_E.test.py
  - TestCase/LibraryChecker/vertex_add_subtree_sum.test.py
  - TestCase/LibraryChecker/vertex_add_path_sum.test.py
  - TestCase/LibraryChecker/lca.HLDecomposition.test.py
documentation_of: Graph/Tree/HLDecomposition.py
layout: document
title: "HL\u5206\u89E3 (Heavy-Light Decomposition)"
---