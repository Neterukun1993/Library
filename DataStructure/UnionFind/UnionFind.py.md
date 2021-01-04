---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_1_A.test.py
    title: TestCase/AOJ/DSL_1_A.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class UnionFind:\n    def __init__(self, n):\n        self.parent = [-1]\
    \ * n\n        self.n = n\n        self.cnt = n\n\n    def root(self, x):\n  \
    \      if self.parent[x] < 0:\n            return x\n        else:\n         \
    \   self.parent[x] = self.root(self.parent[x])\n            return self.parent[x]\n\
    \n    def merge(self, x, y):\n        x = self.root(x)\n        y = self.root(y)\n\
    \        if x == y:\n            return False\n        if self.parent[x] > self.parent[y]:\n\
    \            x, y = y, x\n        self.parent[x] += self.parent[y]\n        self.parent[y]\
    \ = x\n        self.cnt -= 1\n        return True\n\n    def same(self, x, y):\n\
    \        return self.root(x) == self.root(y)\n\n    def size(self, x):\n     \
    \   return -self.parent[self.root(x)]\n\n    def count(self):\n        return\
    \ self.cnt\n\n    def groups(self):\n        res = [[] for _ in range(self.n)]\n\
    \        for i in range(self.n):\n            res[self.root(i)].append(i)\n  \
    \      return [group for group in res if group]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/UnionFind/UnionFind.py
  requiredBy: []
  timestamp: '2021-01-02 02:09:18+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_1_A.test.py
documentation_of: DataStructure/UnionFind/UnionFind.py
layout: document
redirect_from:
- /library/DataStructure/UnionFind/UnionFind.py
- /library/DataStructure/UnionFind/UnionFind.py.html
title: DataStructure/UnionFind/UnionFind.py
---