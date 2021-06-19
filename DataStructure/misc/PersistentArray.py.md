---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure/UnionFind/PersistentUnionFind.py
    title: "\u6C38\u7D9AUnion Find"
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class PersistentArrayNode:\n    def __init__(self, LOG):\n        self.val\
    \ = None\n        self.ch = [None] * (1 << LOG)\n\n\nclass PersistentArray:\n\
    \    def __init__(self, LOG=4):\n        self.LOG = LOG\n        self.MASK = (1\
    \ << LOG) - 1\n\n    def build(self, array):\n        rt = None\n        for i,\
    \ val in enumerate(array):\n            rt = self.init_set(i, val, rt)\n     \
    \   return rt\n \n    def init_set(self, i, val, t):\n        if t is None:\n\
    \            t = PersistentArrayNode(self.LOG)\n        if i == 0:\n         \
    \   t.val = val\n        else:\n            t.ch[i & self.MASK] = self.init_set(i\
    \ >> self.LOG, val, t.ch[i & self.MASK])\n        return t\n\n    def set(self,\
    \ i, val, t):\n        ret = PersistentArrayNode(self.LOG)\n        if t is not\
    \ None:\n            ret.ch = t.ch[:]\n            ret.val = t.val\n        if\
    \ i == 0:\n            ret.val = val\n        else:\n            ret.ch[i & self.MASK]\
    \ = self.set(i >> self.LOG, val, ret.ch[i & self.MASK])\n        return ret\n\n\
    \    def get(self, i, t):\n        if i == 0:\n            return t.val\n    \
    \    else:\n            return self.get(i >> self.LOG, t.ch[i & self.MASK])\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/misc/PersistentArray.py
  requiredBy:
  - DataStructure/UnionFind/PersistentUnionFind.py
  timestamp: '2021-01-03 06:00:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/misc/PersistentArray.py
layout: document
title: "\u6C38\u7D9A\u914D\u5217"
---
