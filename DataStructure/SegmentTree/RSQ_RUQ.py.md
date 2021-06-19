---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_2_I.test.py
    title: TestCase/AOJ/DSL_2_I.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.SegmentTree.LazySegmentTree import LazySegmentTree\n\n\
    \nclass RSQ_RUQ(LazySegmentTree):\n    def __init__(self, n):\n        unitX =\
    \ (0, 0)  # (val, size)\n        unitA = 10 ** 5\n        X_f = lambda x1, x2:\
    \ (x1[0] + x2[0], x1[1] + x2[1])\n        A_f = lambda a1, a2: a1 if a2 == unitA\
    \ else a2\n        XA_map = lambda x, a: x if a == unitA else (x[1] * a, x[1])\n\
    \        super().__init__(n, unitX, unitA, X_f, A_f, XA_map)\n        super().build([(0,\
    \ 1) for i in range(n)])\n\n    def build(self, array):\n        super().build([(x,\
    \ 1) for x in array])\n\n    def __getitem__(self, i):\n        return super().__getitem__(i)[0]\n\
    \n    def __setitem__(self, i, x):\n        super().__setitem__(i, (x, 1))\n\n\
    \    def fold(self, l, r):\n        return super().fold(l, r)[0]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SegmentTree/RSQ_RUQ.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_2_I.test.py
documentation_of: DataStructure/SegmentTree/RSQ_RUQ.py
layout: document
title: RSQ_RUQ
---
