---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_1_B.test.py
    title: TestCase/AOJ/DSL_1_B.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class UnionFindWithPotential:\n    def __init__(self, n):\n        self.parent\
    \ = [-1] * n\n        self.pot = [0] * n\n        self.cnt = n\n        self.INF\
    \ = 10 ** 18\n\n    def root(self, x):\n        if self.parent[x] < 0:\n     \
    \       return x\n        rt = self.root(self.parent[x])\n        self.pot[x]\
    \ += self.pot[self.parent[x]]\n        self.parent[x] = rt\n        return rt\n\
    \n    def merge(self, x, y, potential):\n        \"\"\"merge x and y in pot[x]\
    \ = pot[y] + potential\"\"\"\n        root_x = self.root(x)\n        root_y =\
    \ self.root(y)\n        if root_x == root_y:\n            return False\n     \
    \   if self.parent[root_x] < self.parent[root_y]:\n            self.parent[root_x]\
    \ += self.parent[root_y]\n            self.parent[root_y] = root_x\n         \
    \   self.pot[root_y] = -potential + self.pot[x] - self.pot[y]\n        else:\n\
    \            self.parent[root_y] += self.parent[root_x]\n            self.parent[root_x]\
    \ = root_y\n            self.pot[root_x] = potential - self.pot[x] + self.pot[y]\n\
    \        self.cnt -= 1\n        return True\n\n    def same(self, x, y):\n   \
    \     return self.root(x) == self.root(y)\n\n    def diff(self, x, y):\n     \
    \   \"\"\"get x's potential on a reference point y\"\"\"\n        if not self.same(x,\
    \ y):\n            # potential is not defined between x and y\n            return\
    \ self.INF\n        return self.pot[x] - self.pot[y]\n\n    def size(self, x):\n\
    \        return -self.parent[self.root(x)]\n\n    def count(self):\n        return\
    \ self.cnt\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/UnionFind/UnionFindWithPotential.py
  requiredBy: []
  timestamp: '2021-01-02 02:52:46+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_1_B.test.py
documentation_of: DataStructure/UnionFind/UnionFindWithPotential.py
layout: document
redirect_from:
- /library/DataStructure/UnionFind/UnionFindWithPotential.py
- /library/DataStructure/UnionFind/UnionFindWithPotential.py.html
title: DataStructure/UnionFind/UnionFindWithPotential.py
---
