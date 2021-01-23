---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: DataStructure\misc\PersistentArray.py
    title: "\u6C38\u7D9A\u914D\u5217"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\persistent_unionfind.test.py
    title: TestCase\LibraryChecker\persistent_unionfind.test.py
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
  code: "from DataStructure.misc.PersistentArray import PersistentArray\r\n\r\n\r\n\
    class PersistentUnionFind:\r\n    def __init__(self, n):\r\n        self.parent\
    \ = PersistentArray()\r\n        self.rt = self.parent.build([-1] * n)\r\n\r\n\
    \    def root(self, x, t):\r\n        px = self.parent.get(x, t)\r\n        if\
    \ px < 0:\r\n            return x\r\n        return self.root(px, t)\r\n\r\n \
    \   def merge(self, x, y, t):\r\n        x, y = self.root(x, t), self.root(y,\
    \ t)\r\n        if x == y:\r\n            return t\r\n        px = self.parent.get(x,\
    \ t)\r\n        py = self.parent.get(y, t)\r\n        if px > py:\r\n        \
    \    x, y = y, x\r\n        tmp = self.parent.set(y, x, t)\r\n        return self.parent.set(x,\
    \ px + py, tmp)\r\n\r\n    def same(self, x, y, t):\r\n        return self.root(x,\
    \ t) == self.root(y, t)\r\n\r\n    def size(self, x, t):\r\n        return -self.parent.get(self.root(x,\
    \ t), t)\r\n"
  dependsOn:
  - DataStructure\misc\PersistentArray.py
  isVerificationFile: false
  path: DataStructure\UnionFind\PersistentUnionFind.py
  requiredBy: []
  timestamp: '2021-01-03 06:00:12+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\LibraryChecker\persistent_unionfind.test.py
documentation_of: DataStructure\UnionFind\PersistentUnionFind.py
layout: document
title: "\u6C38\u7D9AUnion Find"
---
