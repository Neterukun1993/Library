---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_2_D.CommutativeDualSegTree.test.py
    title: TestCase/AOJ/DSL_2_D.CommutativeDualSegTree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.SegmentTree.CommutativeDualSegmentTree import CommutativeDualSegmentTree\n\
    \n\nclass RUQ(CommutativeDualSegmentTree):\n    def __init__(self, n):\n     \
    \   unitA = (0, 0)\n        A_f = lambda a1, a2: a2 if a2 > a1 else a1\n     \
    \   super().__init__(n, unitA, A_f)\n        self.cnt = 1\n\n    def __getitem__(self,\
    \ i):\n        return super().__getitem__(i)[1]\n\n    def __setitem__(self, i,\
    \ val):\n        self.cnt += 1\n        super().__setitem__(i, (self.cnt, val))\n\
    \n    def apply(self, i, val):\n        self.cnt += 1\n        super().apply(i,\
    \ (self.cnt, val))\n\n    def range_apply(self, l, r, val):\n        self.cnt\
    \ += 1\n        super().range_apply(l, r, (self.cnt, val))\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SegmentTree/RUQ.py
  requiredBy: []
  timestamp: '2021-01-04 04:15:00+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_2_D.CommutativeDualSegTree.test.py
documentation_of: DataStructure/SegmentTree/RUQ.py
layout: document
title: RUQ
---
