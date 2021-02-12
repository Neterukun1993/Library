---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_3_A.test.py
    title: TestCase/AOJ/DSL_3_A.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_3_D.test.py
    title: TestCase/AOJ/DSL_3_D.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/queue_operate_all_composite.test.py
    title: TestCase/LibraryChecker/queue_operate_all_composite.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SlidingWindowAggregation:\n    def __init__(self, op):\n        self.op\
    \ = op\n        self.inque = []\n        self.outque = []\n\n    def __len__(self):\n\
    \        return len(self.outque) + len(self.inque)\n\n    def _trans(self):\n\
    \        val, _ = self.inque.pop()\n        self.outque.append((val, val))\n \
    \       acc = val\n        while self.inque:\n            val, _ = self.inque.pop()\n\
    \            acc = self.op(val, acc)\n            self.outque.append((val, acc))\n\
    \n    def all_fold(self):\n        if not self.inque:\n            return self.outque[-1][1]\n\
    \        if not self.outque:\n            return self.inque[-1][1]\n        return\
    \ self.op(self.outque[-1][1], self.inque[-1][1])\n\n    def append(self, val):\n\
    \        if self.inque:\n            self.inque.append((val, self.op(self.inque[-1][1],\
    \ val)))\n        else:\n            self.inque.append((val, val))\n\n    def\
    \ popleft(self):\n        if not self.outque:\n            self._trans()\n   \
    \     val = self.outque.pop()\n        return val[0]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/misc/SlidingWindowAggregation.py
  requiredBy: []
  timestamp: '2021-01-03 19:45:45+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_3_A.test.py
  - TestCase/AOJ/DSL_3_D.test.py
  - TestCase/LibraryChecker/queue_operate_all_composite.test.py
documentation_of: DataStructure/misc/SlidingWindowAggregation.py
layout: document
title: Sliding Window Aggregation
---
