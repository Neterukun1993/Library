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
    path: TestCase/AOJ/DSL_2_F.test.py
    title: TestCase/AOJ/DSL_2_F.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.SegmentTree.LazySegmentTree import LazySegmentTree\n\n\
    \nclass RmQ_RUQ(LazySegmentTree):\n    def __init__(self, n):\n        unitX =\
    \ (1 << 31) - 1\n        unitA = -1\n        X_f = min\n        A_f = lambda a1,\
    \ a2: a1 if a2 == self.unitA else a2\n        XA_map = lambda x, a: x if a ==\
    \ self.unitA else a\n        super().__init__(n, unitX, unitA, X_f, A_f, XA_map)\n"
  dependsOn:
  - DataStructure/SegmentTree/LazySegmentTree.py
  isVerificationFile: false
  path: DataStructure/SegmentTree/RmQ_RUQ.py
  requiredBy: []
  timestamp: '2021-01-02 17:11:03+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_2_F.test.py
documentation_of: DataStructure/SegmentTree/RmQ_RUQ.py
layout: document
title: RmQ_RUQ
---