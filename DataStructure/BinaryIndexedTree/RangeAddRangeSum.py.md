---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_2_G.test.py
    title: TestCase/AOJ/DSL_2_G.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_5_E.test.py
    title: TestCase/AOJ/GRL_5_E.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BinaryIndexedTree:\n    def __init__(self, n):\n        self.size =\
    \ n\n        self.bit0 = [0] * (self.size + 1)\n        self.bit1 = [0] * (self.size\
    \ + 1)\n\n    def _add(self, bit, i, val):\n        i = i + 1\n        while i\
    \ <= self.size:\n            bit[i] += val\n            i += i & -i\n\n    def\
    \ _sum(self, bit, i):\n        s = 0\n        while i > 0:\n            s += bit[i]\n\
    \            i -= i & -i\n        return s\n\n    def add(self, l, r, val):\n\
    \        \"\"\"add value in range [l, r)\"\"\"\n        self._add(self.bit0, l,\
    \ -val * l)\n        self._add(self.bit0, r, val * r)\n        self._add(self.bit1,\
    \ l, val)\n        self._add(self.bit1, r, -val)\n\n    def sum(self, l, r):\n\
    \        \"\"\"sum of values in range [l, r)\"\"\"\n        return self._sum(self.bit0,\
    \ r) + r * self._sum(self.bit1, r)\\\n               - self._sum(self.bit0, l)\
    \ - l * self._sum(self.bit1, l)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/BinaryIndexedTree/RangeAddRangeSum.py
  requiredBy: []
  timestamp: '2021-01-02 01:52:07+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_2_G.test.py
  - TestCase/AOJ/GRL_5_E.test.py
documentation_of: DataStructure/BinaryIndexedTree/RangeAddRangeSum.py
layout: document
title: "\u533A\u9593\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
---
