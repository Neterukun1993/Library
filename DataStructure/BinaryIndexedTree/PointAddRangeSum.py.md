---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure/BinaryIndexedTree/inversion_number.py
    title: DataStructure/BinaryIndexedTree/inversion_number.py
  - icon: ':heavy_check_mark:'
    path: DataStructure/Wavelet/PointAddRectangleSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u77E9\u5F62\u548C\u53D6\u5F97"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_2_B.BIT.test.py
    title: TestCase/AOJ/DSL_2_B.BIT.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/GRL_5_D.test.py
    title: TestCase/AOJ/GRL_5_D.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/point_add_range_sum.test.py
    title: TestCase/LibraryChecker/point_add_range_sum.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/vertex_add_path_sum.test.py
    title: TestCase/LibraryChecker/vertex_add_path_sum.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/vertex_add_subtree_sum.test.py
    title: TestCase/LibraryChecker/vertex_add_subtree_sum.test.py
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
    \                continue\n            self.bit[i + (i & -i)] += self.bit[i]\n\
    \n    def _sum(self, i):\n        s = 0\n        while i > 0:\n            s +=\
    \ self.bit[i]\n            i -= i & -i\n        return s\n\n    def add(self,\
    \ i, val):\n        i += 1\n        while i <= self.size:\n            self.bit[i]\
    \ += val\n            i += i & -i\n\n    def sum(self, l, r):\n        \"\"\"\
    sum of values in range [l, r)\"\"\"\n        return self._sum(r) - self._sum(l)\n\
    \n    def bisect_left(self, val):\n        \"\"\"minimum idx s.t. sum[0, idx)\
    \ >= val\"\"\"\n        if val <= 0:\n            return 0\n        idx = 0\n\
    \        k = 1 << self.size.bit_length()\n        while k:\n            if idx\
    \ + k <= self.size and self.bit[idx + k] < val:\n                val -= self.bit[idx\
    \ + k]\n                idx += k\n            k >>= 1\n        return idx + 1\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/BinaryIndexedTree/PointAddRangeSum.py
  requiredBy:
  - DataStructure/Wavelet/PointAddRectangleSum.py
  - DataStructure/BinaryIndexedTree/inversion_number.py
  timestamp: '2021-01-02 01:05:58+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_2_B.BIT.test.py
  - TestCase/AOJ/GRL_5_D.test.py
  - TestCase/LibraryChecker/point_add_range_sum.test.py
  - TestCase/LibraryChecker/vertex_add_path_sum.test.py
  - TestCase/LibraryChecker/vertex_add_subtree_sum.test.py
documentation_of: DataStructure/BinaryIndexedTree/PointAddRangeSum.py
layout: document
redirect_from:
- /library/DataStructure/BinaryIndexedTree/PointAddRangeSum.py
- /library/DataStructure/BinaryIndexedTree/PointAddRangeSum.py.html
title: DataStructure/BinaryIndexedTree/PointAddRangeSum.py
---
