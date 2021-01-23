---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: TestCase/LibraryChecker/lca.Doubling.test.py
    title: TestCase/LibraryChecker/lca.Doubling.test.py
  - icon: ':x:'
    path: TestCase/yukicoder/yuki0922.test.py
    title: TestCase/yukicoder/yuki0922.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class DoublingLCA:\n    def __init__(self, tree, root=None):\n        self.n\
    \ = len(tree)\n        self.depth = [0] * self.n\n        self.log_size = (self.n).bit_length()\n\
    \        self.parent = [[-1] * self.n for i in range(self.log_size)]\n\n     \
    \   if root is None:\n            for v in range(self.n):\n                if\
    \ self.parent[0][v] == -1:\n                    self._dfs(v, tree)\n        else:\n\
    \            self._dfs(root, tree)\n\n        for k in range(self.log_size - 1):\n\
    \            for v in range(self.n):\n                if self.parent[k][v] ==\
    \ -1:\n                    self.parent[k + 1][v] = -1\n                else:\n\
    \                    self.parent[k + 1][v] = self.parent[k][self.parent[k][v]]\n\
    \n    def _dfs(self, rt, tree):\n        stack = [(rt, -1)]\n        while stack:\n\
    \            v, par = stack.pop()\n            for chi_v in tree[v]:\n       \
    \         if chi_v == par:\n                    continue\n                self.parent[0][chi_v]\
    \ = v\n                self.depth[chi_v] = self.depth[v] + 1\n               \
    \ stack.append((chi_v, v))\n\n    def lca(self, u, v):\n        if self.depth[u]\
    \ > self.depth[v]:\n            u, v = v, u\n        for k in range(self.log_size):\n\
    \            if ((self.depth[v] - self.depth[u]) >> k) & 1:\n                v\
    \ = self.parent[k][v]\n        if u == v:\n            return u\n        for k\
    \ in reversed(range(self.log_size)):\n            if self.parent[k][u] != self.parent[k][v]:\n\
    \                u = self.parent[k][u]\n                v = self.parent[k][v]\n\
    \        return self.parent[0][u]\n\n    def distance(self, u, v):\n        lca_uv\
    \ = self.lca(u, v)\n        if lca_uv == -1:\n            return -1\n        else:\n\
    \            return self.depth[u] + self.depth[v] - 2 * self.depth[lca_uv]\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/Tree/DoublingLCA.py
  requiredBy: []
  timestamp: '2021-01-14 15:15:35+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - TestCase/yukicoder/yuki0922.test.py
  - TestCase/LibraryChecker/lca.Doubling.test.py
documentation_of: Graph/Tree/DoublingLCA.py
layout: document
redirect_from:
- /library/Graph/Tree/DoublingLCA.py
- /library/Graph/Tree/DoublingLCA.py.html
title: Graph/Tree/DoublingLCA.py
---
