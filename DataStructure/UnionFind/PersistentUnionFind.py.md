---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: DataStructure/misc/PersistentArray.py
    title: "\u6C38\u7D9A\u914D\u5217"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/persistent_unionfind.test.py
    title: TestCase/LibraryChecker/persistent_unionfind.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.misc.PersistentArray import PersistentArray\n\n\nclass\
    \ PersistentUnionFind:\n    def __init__(self, n):\n        self.parent = PersistentArray()\n\
    \        self.rt = self.parent.build([-1] * n)\n\n    def root(self, x, t):\n\
    \        px = self.parent.get(x, t)\n        if px < 0:\n            return x\n\
    \        return self.root(px, t)\n\n    def merge(self, x, y, t):\n        x,\
    \ y = self.root(x, t), self.root(y, t)\n        if x == y:\n            return\
    \ t\n        px = self.parent.get(x, t)\n        py = self.parent.get(y, t)\n\
    \        if px > py:\n            x, y = y, x\n        tmp = self.parent.set(y,\
    \ x, t)\n        return self.parent.set(x, px + py, tmp)\n\n    def same(self,\
    \ x, y, t):\n        return self.root(x, t) == self.root(y, t)\n\n    def size(self,\
    \ x, t):\n        return -self.parent.get(self.root(x, t), t)\n"
  dependsOn:
  - DataStructure/misc/PersistentArray.py
  isVerificationFile: false
  path: DataStructure/UnionFind/PersistentUnionFind.py
  requiredBy: []
  timestamp: '2021-01-03 06:00:12+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/persistent_unionfind.test.py
documentation_of: DataStructure/UnionFind/PersistentUnionFind.py
layout: document
title: "\u6C38\u7D9AUnion Find"
---
