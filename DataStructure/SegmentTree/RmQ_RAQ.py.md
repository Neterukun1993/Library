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
    path: TestCase\AOJ\DSL_2_H.test.py
    title: TestCase\AOJ\DSL_2_H.test.py
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
    \r\n\r\nclass RmQ_RAQ(LazySegmentTree):\r\n    def __init__(self, n):\r\n    \
    \    unitX = (1 << 31) - 1\r\n        unitA = 0\r\n        X_f = min\r\n     \
    \   A_f = lambda a1, a2: a1 + a2\r\n        XA_map = lambda x, a: x + a\r\n  \
    \      super().__init__(n, unitX, unitA, X_f, A_f, XA_map)\r\n        super().build([0]\
    \ * n)\r\n"
  dependsOn:
  - DataStructure\SegmentTree\LazySegmentTree.py
  isVerificationFile: false
  path: DataStructure\SegmentTree\RmQ_RAQ.py
  requiredBy: []
  timestamp: '2021-01-02 18:15:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\DSL_2_H.test.py
documentation_of: DataStructure\SegmentTree\RmQ_RAQ.py
layout: document
title: RmQ_RAQ
---
