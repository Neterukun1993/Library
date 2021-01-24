---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: DataStructure/SegmentTree/LazySegmentTree.py
    title: "\u9045\u5EF6\u4F1D\u64AD\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment\
      \ Tree with Lazy Propagation)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_2_H.test.py
    title: TestCase/AOJ/DSL_2_H.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.SegmentTree.LazySegmentTree import LazySegmentTree\n\n\
    \nclass RmQ_RAQ(LazySegmentTree):\n    def __init__(self, n):\n        unitX =\
    \ (1 << 31) - 1\n        unitA = 0\n        X_f = min\n        A_f = lambda a1,\
    \ a2: a1 + a2\n        XA_map = lambda x, a: x + a\n        super().__init__(n,\
    \ unitX, unitA, X_f, A_f, XA_map)\n        super().build([0] * n)\n"
  dependsOn:
  - DataStructure/SegmentTree/LazySegmentTree.py
  isVerificationFile: false
  path: DataStructure/SegmentTree/RmQ_RAQ.py
  requiredBy: []
  timestamp: '2021-01-02 18:15:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_2_H.test.py
documentation_of: DataStructure/SegmentTree/RmQ_RAQ.py
layout: document
title: RmQ_RAQ
---
