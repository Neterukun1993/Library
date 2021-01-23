---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\yukicoder\yuki0416.test.py
    title: TestCase\yukicoder\yuki0416.test.py
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
  code: "from bisect import bisect_left\r\n\r\n\r\nclass PartiallyPersistentUnionFind:\r\
    \n    def __init__(self, n):\r\n        self.INF = 10 ** 9\r\n        self.parent\
    \ = [-1] * n\r\n        self.time = [self.INF] * n\r\n        self.size = [[(-1,\
    \ -1)] for i in range(n)]\r\n\r\n    def root(self, t, x):\r\n        while self.time[x]\
    \ <= t:\r\n            x = self.parent[x]\r\n        return x\r\n\r\n    def merge(self,\
    \ t, x, y):\r\n        x = self.root(t, x)\r\n        y = self.root(t, y)\r\n\
    \        if x == y:\r\n            return False\r\n        if self.parent[x] >\
    \ self.parent[y]:\r\n            x, y = y, x\r\n        self.parent[x] += self.parent[y]\r\
    \n        self.size[x].append((t, self.parent[x]))\r\n        self.parent[y] =\
    \ x\r\n        self.time[y] = t\r\n        return True\r\n\r\n    def same(self,\
    \ t, x, y):\r\n        return self.root(t, x) == self.root(t, y)\r\n\r\n    def\
    \ size(self, t, x):\r\n        x = self.root(t, x)\r\n        idx = bisect_left(self.size[x],\
    \ (t, self.INF)) - 1\r\n        return -self.size[x][idx][1]\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\UnionFind\PartiallyPersistentUnionFind.py
  requiredBy: []
  timestamp: '2021-01-10 07:28:54+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\yukicoder\yuki0416.test.py
documentation_of: DataStructure\UnionFind\PartiallyPersistentUnionFind.py
layout: document
title: "\u90E8\u5206\u6C38\u7D9AUnion Find"
---
