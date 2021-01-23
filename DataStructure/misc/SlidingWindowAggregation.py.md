---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DSL_3_A.test.py
    title: TestCase\AOJ\DSL_3_A.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DSL_3_D.test.py
    title: TestCase\AOJ\DSL_3_D.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\queue_operate_all_composite.test.py
    title: TestCase\LibraryChecker\queue_operate_all_composite.test.py
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
  code: "class SlidingWindowAggregation:\r\n    def __init__(self, op):\r\n      \
    \  self.op = op\r\n        self.inque = []\r\n        self.outque = []\r\n\r\n\
    \    def __len__(self):\r\n        return len(self.outque) + len(self.inque)\r\
    \n\r\n    def _trans(self):\r\n        val, _ = self.inque.pop()\r\n        self.outque.append((val,\
    \ val))\r\n        acc = val\r\n        while self.inque:\r\n            val,\
    \ _ = self.inque.pop()\r\n            acc = self.op(val, acc)\r\n            self.outque.append((val,\
    \ acc))\r\n\r\n    def all_fold(self):\r\n        if not self.inque:\r\n     \
    \       return self.outque[-1][1]\r\n        if not self.outque:\r\n         \
    \   return self.inque[-1][1]\r\n        return self.op(self.outque[-1][1], self.inque[-1][1])\r\
    \n\r\n    def append(self, val):\r\n        if self.inque:\r\n            self.inque.append((val,\
    \ self.op(self.inque[-1][1], val)))\r\n        else:\r\n            self.inque.append((val,\
    \ val))\r\n\r\n    def popleft(self):\r\n        if not self.outque:\r\n     \
    \       self._trans()\r\n        val = self.outque.pop()\r\n        return val[0]\r\
    \n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\misc\SlidingWindowAggregation.py
  requiredBy: []
  timestamp: '2021-01-03 19:45:45+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\DSL_3_A.test.py
  - TestCase\AOJ\DSL_3_D.test.py
  - TestCase\LibraryChecker\queue_operate_all_composite.test.py
documentation_of: DataStructure\misc\SlidingWindowAggregation.py
layout: document
title: Sliding Window Aggregation
---
