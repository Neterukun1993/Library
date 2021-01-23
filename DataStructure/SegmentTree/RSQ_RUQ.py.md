---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: DataStructure\SegmentTree\LazySegmentTree.py
    title: "\u9045\u5EF6\u4F1D\u64AD\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment\
      \ Tree with Lazy Propagation)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DSL_2_I.test.py
    title: TestCase\AOJ\DSL_2_I.test.py
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
  code: "from DataStructure.SegmentTree.LazySegmentTree import LazySegmentTree\r\n\
    \r\n\r\nclass RSQ_RUQ(LazySegmentTree):\r\n    def __init__(self, n):\r\n    \
    \    unitX = (0, 0)  # (val, size)\r\n        unitA = 10 ** 5\r\n        X_f =\
    \ lambda x1, x2: (x1[0] + x2[0], x1[1] + x2[1])\r\n        A_f = lambda a1, a2:\
    \ a1 if a2 == unitA else a2\r\n        XA_map = lambda x, a: x if a == unitA else\
    \ (x[1] * a, x[1])\r\n        super().__init__(n, unitX, unitA, X_f, A_f, XA_map)\r\
    \n        super().build([(0, 1) for i in range(n)])\r\n\r\n    def build(self,\
    \ array):\r\n        super().build([(x, 1) for x in array])\r\n\r\n    def __getitem__(self,\
    \ i):\r\n        return super().__getitem__(i)[0]\r\n\r\n    def __setitem__(self,\
    \ i, x):\r\n        super().__setitem__(i, (x, 1))\r\n\r\n    def fold(self, l,\
    \ r):\r\n        return super().fold(l, r)[0]\r\n"
  dependsOn:
  - DataStructure\SegmentTree\LazySegmentTree.py
  isVerificationFile: false
  path: DataStructure\SegmentTree\RSQ_RUQ.py
  requiredBy: []
  timestamp: '2021-01-02 18:32:26+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\DSL_2_I.test.py
documentation_of: DataStructure\SegmentTree\RSQ_RUQ.py
layout: document
title: RSQ_RUQ
---
