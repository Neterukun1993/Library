---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DSL_5_A.test.py
    title: TestCase\AOJ\DSL_5_A.test.py
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
  code: "class Imos:\r\n    def __init__(self, n):\r\n        self.n = n\r\n     \
    \   self.imos = [0] * (self.n + 1)\r\n\r\n    def __getitem__(self, i):\r\n  \
    \      return self.imos[i]\r\n\r\n    def add(self, l, r, val):\r\n        \"\"\
    \"add value in range [l, r)\"\"\"\r\n        self.imos[r] -= val\r\n        self.imos[l]\
    \ += val\r\n\r\n    def build(self):\r\n        for i in range(self.n):\r\n  \
    \          self.imos[i + 1] += self.imos[i]\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\AccumulateSum\Imos.py
  requiredBy: []
  timestamp: '2021-01-02 06:20:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\DSL_5_A.test.py
documentation_of: DataStructure\AccumulateSum\Imos.py
layout: document
title: "\u3044\u3082\u3059\u6CD5"
---
