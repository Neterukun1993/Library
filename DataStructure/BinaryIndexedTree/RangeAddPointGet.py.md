---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_2_E.test.py
    title: TestCase/AOJ/DSL_2_E.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BinaryIndexedTree:\n    def __init__(self, n):\n        self.size =\
    \ n\n        self.bit = [0] * (self.size + 1)\n\n    def build(self, array):\n\
    \        for i, val in enumerate(array):\n            self.bit[i + 1] = val\n\
    \        for i in range(1, self.size):\n            if i + (i & -i) > self.size:\n\
    \                continue\n            self.bit[i] -= self.bit[i + (i & -i)]\n\
    \n    def __getitem__(self, i):\n        i = i + 1\n        s = 0\n        while\
    \ i <= self.size:\n            s += self.bit[i]\n            i += i & -i\n   \
    \     return s\n\n    def _add(self, i, val):\n        while i > 0:\n        \
    \    self.bit[i] += val\n            i -= i & -i\n\n    def add(self, l, r, val):\n\
    \        \"\"\"add value in range [l, r)\"\"\"\n        self._add(r, val)\n  \
    \      self._add(l, -val)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/BinaryIndexedTree/RangeAddPointGet.py
  requiredBy: []
  timestamp: '2021-01-02 01:31:17+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_2_E.test.py
documentation_of: DataStructure/BinaryIndexedTree/RangeAddPointGet.py
layout: document
title: "\u533A\u9593\u52A0\u7B97\u30FB\u4E00\u70B9\u53D6\u5F97"
---
