---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure\UnionFind\PersistentUnionFind.py
    title: "\u6C38\u7D9AUnion Find"
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class PersistentArrayNode:\r\n    def __init__(self, LOG):\r\n        self.val\
    \ = None\r\n        self.ch = [None] * (1 << LOG)\r\n\r\n\r\nclass PersistentArray:\r\
    \n    def __init__(self, LOG=4):\r\n        self.LOG = LOG\r\n        self.MASK\
    \ = (1 << LOG) - 1\r\n\r\n    def build(self, array):\r\n        rt = None\r\n\
    \        for i, val in enumerate(array):\r\n            rt = self.init_set(i,\
    \ val, rt)\r\n        return rt\r\n \r\n    def init_set(self, i, val, t):\r\n\
    \        if t is None:\r\n            t = PersistentArrayNode(self.LOG)\r\n  \
    \      if i == 0:\r\n            t.val = val\r\n        else:\r\n            t.ch[i\
    \ & self.MASK] = self.init_set(i >> self.LOG, val, t.ch[i & self.MASK])\r\n  \
    \      return t\r\n\r\n    def set(self, i, val, t):\r\n        ret = PersistentArrayNode(self.LOG)\r\
    \n        if t is not None:\r\n            ret.ch = t.ch[:]\r\n            ret.val\
    \ = t.val\r\n        if i == 0:\r\n            ret.val = val\r\n        else:\r\
    \n            ret.ch[i & self.MASK] = self.set(i >> self.LOG, val, ret.ch[i &\
    \ self.MASK])\r\n        return ret\r\n\r\n    def get(self, i, t):\r\n      \
    \  if i == 0:\r\n            return t.val\r\n        else:\r\n            return\
    \ self.get(i >> self.LOG, t.ch[i & self.MASK])\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\misc\PersistentArray.py
  requiredBy:
  - DataStructure\UnionFind\PersistentUnionFind.py
  timestamp: '2021-01-03 06:00:12+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure\misc\PersistentArray.py
layout: document
title: "\u6C38\u7D9A\u914D\u5217"
---
