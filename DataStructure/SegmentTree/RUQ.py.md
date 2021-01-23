---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: DataStructure\SegmentTree\CommutativeDualSegmentTree.py
    title: "\u53EF\u63DB\u53CC\u5BFE\u30BB\u30B0\u30E1\u30F3\u30C8\u6728"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DSL_2_D.CommutativeDualSegTree.test.py
    title: TestCase\AOJ\DSL_2_D.CommutativeDualSegTree.test.py
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
  code: "from DataStructure.SegmentTree.CommutativeDualSegmentTree import CommutativeDualSegmentTree\r\
    \n\r\n\r\nclass RUQ(CommutativeDualSegmentTree):\r\n    def __init__(self, n):\r\
    \n        unitA = (0, 0)\r\n        A_f = lambda a1, a2: a2 if a2 > a1 else a1\r\
    \n        super().__init__(n, unitA, A_f)\r\n        self.cnt = 1\r\n\r\n    def\
    \ __getitem__(self, i):\r\n        return super().__getitem__(i)[1]\r\n\r\n  \
    \  def __setitem__(self, i, val):\r\n        self.cnt += 1\r\n        super().__setitem__(i,\
    \ (self.cnt, val))\r\n\r\n    def apply(self, i, val):\r\n        self.cnt +=\
    \ 1\r\n        super().apply(i, (self.cnt, val))\r\n\r\n    def range_apply(self,\
    \ l, r, val):\r\n        self.cnt += 1\r\n        super().range_apply(l, r, (self.cnt,\
    \ val))\r\n"
  dependsOn:
  - DataStructure\SegmentTree\CommutativeDualSegmentTree.py
  isVerificationFile: false
  path: DataStructure\SegmentTree\RUQ.py
  requiredBy: []
  timestamp: '2021-01-04 04:15:00+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\DSL_2_D.CommutativeDualSegTree.test.py
documentation_of: DataStructure\SegmentTree\RUQ.py
layout: document
title: RUQ
---
