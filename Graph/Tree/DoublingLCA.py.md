---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\lca.Doubling.test.py
    title: TestCase\LibraryChecker\lca.Doubling.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\yukicoder\yuki0922.test.py
    title: TestCase\yukicoder\yuki0922.test.py
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
  code: "class DoublingLCA:\r\n    def __init__(self, tree, root=None):\r\n      \
    \  self.n = len(tree)\r\n        self.depth = [0] * self.n\r\n        self.log_size\
    \ = (self.n).bit_length()\r\n        self.parent = [[-1] * self.n for i in range(self.log_size)]\r\
    \n\r\n        if root is None:\r\n            for v in range(self.n):\r\n    \
    \            if self.parent[0][v] == -1:\r\n                    self._dfs(v, tree)\r\
    \n        else:\r\n            self._dfs(root, tree)\r\n\r\n        for k in range(self.log_size\
    \ - 1):\r\n            for v in range(self.n):\r\n                if self.parent[k][v]\
    \ == -1:\r\n                    self.parent[k + 1][v] = -1\r\n               \
    \ else:\r\n                    self.parent[k + 1][v] = self.parent[k][self.parent[k][v]]\r\
    \n\r\n    def _dfs(self, rt, tree):\r\n        stack = [(rt, -1)]\r\n        while\
    \ stack:\r\n            v, par = stack.pop()\r\n            for chi_v in tree[v]:\r\
    \n                if chi_v == par:\r\n                    continue\r\n       \
    \         self.parent[0][chi_v] = v\r\n                self.depth[chi_v] = self.depth[v]\
    \ + 1\r\n                stack.append((chi_v, v))\r\n\r\n    def lca(self, u,\
    \ v):\r\n        if self.depth[u] > self.depth[v]:\r\n            u, v = v, u\r\
    \n        for k in range(self.log_size):\r\n            if ((self.depth[v] - self.depth[u])\
    \ >> k) & 1:\r\n                v = self.parent[k][v]\r\n        if u == v:\r\n\
    \            return u\r\n        for k in reversed(range(self.log_size)):\r\n\
    \            if self.parent[k][u] != self.parent[k][v]:\r\n                u =\
    \ self.parent[k][u]\r\n                v = self.parent[k][v]\r\n        return\
    \ self.parent[0][u]\r\n\r\n    def distance(self, u, v):\r\n        lca_uv = self.lca(u,\
    \ v)\r\n        if lca_uv == -1:\r\n            return -1\r\n        else:\r\n\
    \            return self.depth[u] + self.depth[v] - 2 * self.depth[lca_uv]\r\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph\Tree\DoublingLCA.py
  requiredBy: []
  timestamp: '2021-01-14 15:15:35+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\LibraryChecker\lca.Doubling.test.py
  - TestCase\yukicoder\yuki0922.test.py
documentation_of: Graph\Tree\DoublingLCA.py
layout: document
redirect_from:
- /library\Graph\Tree\DoublingLCA.py
- /library\Graph\Tree\DoublingLCA.py.html
title: Graph\Tree\DoublingLCA.py
---
