---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DSL_1_B.test.py
    title: TestCase\AOJ\DSL_1_B.test.py
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
  code: "class UnionFindWithPotential:\r\n    def __init__(self, n):\r\n        self.parent\
    \ = [-1] * n\r\n        self.pot = [0] * n\r\n        self.cnt = n\r\n       \
    \ self.INF = 10 ** 18\r\n\r\n    def root(self, x):\r\n        if self.parent[x]\
    \ < 0:\r\n            return x\r\n        rt = self.root(self.parent[x])\r\n \
    \       self.pot[x] += self.pot[self.parent[x]]\r\n        self.parent[x] = rt\r\
    \n        return rt\r\n\r\n    def merge(self, x, y, potential):\r\n        \"\
    \"\"merge x and y in pot[x] = pot[y] + potential\"\"\"\r\n        root_x = self.root(x)\r\
    \n        root_y = self.root(y)\r\n        if root_x == root_y:\r\n          \
    \  return False\r\n        if self.parent[root_x] < self.parent[root_y]:\r\n \
    \           self.parent[root_x] += self.parent[root_y]\r\n            self.parent[root_y]\
    \ = root_x\r\n            self.pot[root_y] = -potential + self.pot[x] - self.pot[y]\r\
    \n        else:\r\n            self.parent[root_y] += self.parent[root_x]\r\n\
    \            self.parent[root_x] = root_y\r\n            self.pot[root_x] = potential\
    \ - self.pot[x] + self.pot[y]\r\n        self.cnt -= 1\r\n        return True\r\
    \n\r\n    def same(self, x, y):\r\n        return self.root(x) == self.root(y)\r\
    \n\r\n    def diff(self, x, y):\r\n        \"\"\"get x's potential on a reference\
    \ point y\"\"\"\r\n        if not self.same(x, y):\r\n            # potential\
    \ is not defined between x and y\r\n            return self.INF\r\n        return\
    \ self.pot[x] - self.pot[y]\r\n\r\n    def size(self, x):\r\n        return -self.parent[self.root(x)]\r\
    \n\r\n    def count(self):\r\n        return self.cnt\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\UnionFind\UnionFindWithPotential.py
  requiredBy: []
  timestamp: '2021-01-02 02:52:46+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\DSL_1_B.test.py
documentation_of: DataStructure\UnionFind\UnionFindWithPotential.py
layout: document
title: "\u30DD\u30C6\u30F3\u30B7\u30E3\u30EB\u4ED8\u304DUnion Find"
---
