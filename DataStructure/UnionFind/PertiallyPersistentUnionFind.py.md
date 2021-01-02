---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0416.test.py
    title: TestCase/yukicoder/yuki0416.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from bisect import bisect_left\n\n\nclass PertiallyPersistentUnionFind:\n\
    \    def __init__(self, n):\n        self.INF = 10 ** 9\n        self.parent =\
    \ [-1] * n\n        self.time = [self.INF] * n\n        self.size = [[(-1, -1)]\
    \ for i in range(n)]\n\n    def root(self, t, x):\n        while self.time[x]\
    \ <= t:\n            x = self.parent[x]\n        return x\n\n    def merge(self,\
    \ t, x, y):\n        x = self.root(t, x)\n        y = self.root(t, y)\n      \
    \  if x == y:\n            return False\n        if self.parent[x] > self.parent[y]:\n\
    \            x, y = y, x\n        self.parent[x] += self.parent[y]\n        self.size[x].append((t,\
    \ self.parent[x]))\n        self.parent[y] = x\n        self.time[y] = t\n   \
    \     return True\n\n    def same(self, t, x, y):\n        return self.root(t,\
    \ x) == self.root(t, y)\n\n    def size(self, t, x):\n        x = self.root(t,\
    \ x)\n        idx = bisect_left(self.size[x], (t, self.INF)) - 1\n        return\
    \ -self.size[x][idx][1]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/UnionFind/PertiallyPersistentUnionFind.py
  requiredBy: []
  timestamp: '2021-01-03 01:00:38+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki0416.test.py
documentation_of: DataStructure/UnionFind/PertiallyPersistentUnionFind.py
layout: document
redirect_from:
- /library/DataStructure/UnionFind/PertiallyPersistentUnionFind.py
- /library/DataStructure/UnionFind/PertiallyPersistentUnionFind.py.html
title: DataStructure/UnionFind/PertiallyPersistentUnionFind.py
---
