---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_5_A.test.py
    title: TestCase/AOJ/DSL_5_A.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Imos:\n    def __init__(self, n):\n        self.n = n\n        self.imos\
    \ = [0] * (self.n + 1)\n\n    def __getitem__(self, i):\n        return self.imos[i]\n\
    \n    def add(self, l, r, val):\n        \"\"\"add value in range [l, r)\"\"\"\
    \n        self.imos[r] -= val\n        self.imos[l] += val\n\n    def build(self):\n\
    \        for i in range(self.n):\n            self.imos[i + 1] += self.imos[i]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/AccumulateSum/Imos.py
  requiredBy: []
  timestamp: '2021-01-02 06:20:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_5_A.test.py
documentation_of: DataStructure/AccumulateSum/Imos.py
layout: document
title: "\u3044\u3082\u3059\u6CD5"
---
