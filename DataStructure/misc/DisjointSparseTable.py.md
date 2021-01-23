---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\static_range_sum.DisjointSparseTable.test.py
    title: TestCase\LibraryChecker\static_range_sum.DisjointSparseTable.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\staticrmq.DisjointSparseTable.test.py
    title: TestCase\LibraryChecker\staticrmq.DisjointSparseTable.test.py
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
  code: "class DisjointSparseTable:\r\n    def __init__(self, array, op):\r\n    \
    \    self.n = len(array)\r\n        self.op = op\r\n        self.row_size = self.n.bit_length()\r\
    \n        self.log_tbl = [0] * (1 << self.row_size)\r\n        for i in range(2,\
    \ 1 << self.row_size):\r\n            self.log_tbl[i] = self.log_tbl[i // 2] +\
    \ 1\r\n\r\n        self.sp_tbl = [[0] * self.n for _ in range(self.row_size)]\r\
    \n        for i, val in enumerate(array):\r\n            self.sp_tbl[0][i] = val\r\
    \n        for row in range(1, self.row_size):\r\n            shift = 1 << row\r\
    \n            l = 0\r\n            while l < self.n:\r\n                mid =\
    \ l + shift\r\n                t = min(mid, self.n)\r\n                self.sp_tbl[row][t\
    \ - 1] = array[t - 1]\r\n                for k in reversed(range(l, t - 1)):\r\
    \n                    self.sp_tbl[row][k] = self.op(array[k], self.sp_tbl[row][k\
    \ + 1])\r\n                if self.n <= t:\r\n                    break\r\n  \
    \              r = min(mid + shift, self.n)\r\n                self.sp_tbl[row][t]\
    \ = array[t]\r\n                for k in range(t + 1, r):\r\n                \
    \    self.sp_tbl[row][k] = self.op(self.sp_tbl[row][k - 1], array[k])\r\n    \
    \            l = mid + shift\r\n\r\n    def fold(self, l, r):\r\n        r -=\
    \ 1\r\n        if l == r:\r\n            return self.sp_tbl[0][l]\r\n        p\
    \ = self.log_tbl[l ^ r]\r\n        return self.op(self.sp_tbl[p][l], self.sp_tbl[p][r])\r\
    \n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\misc\DisjointSparseTable.py
  requiredBy: []
  timestamp: '2021-01-03 11:00:07+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\LibraryChecker\staticrmq.DisjointSparseTable.test.py
  - TestCase\LibraryChecker\static_range_sum.DisjointSparseTable.test.py
documentation_of: DataStructure\misc\DisjointSparseTable.py
layout: document
title: Disjoint Sparse Table
---
