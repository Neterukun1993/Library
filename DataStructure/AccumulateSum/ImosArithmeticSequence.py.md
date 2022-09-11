---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class ImosArithmeticSequence:\n    def __init__(self, n):\n        self.n\
    \ = n\n        self.imos0 = [0] * (self.n + 1)\n        self.imos1 = [0] * (self.n\
    \ + 1)\n\n    def __getitem__(self, i):\n        return self.imos0[i] + self.imos1[i]\
    \ * i\n\n    def add(self, l, r, a, d):\n        self.imos0[l] += a\n        self.imos0[r]\
    \ -= a\n        self.imos0[l] -= d * l\n        self.imos0[r] += d * l\n     \
    \   self.imos1[l] += d\n        self.imos1[r] -= d\n\n    def build(self):\n \
    \       for i in range(self.n):\n            self.imos0[i + 1] += self.imos0[i]\n\
    \            self.imos1[i + 1] += self.imos1[i]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/AccumulateSum/ImosArithmeticSequence.py
  requiredBy: []
  timestamp: '2022-09-11 12:52:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/AccumulateSum/ImosArithmeticSequence.py
layout: document
redirect_from:
- /library/DataStructure/AccumulateSum/ImosArithmeticSequence.py
- /library/DataStructure/AccumulateSum/ImosArithmeticSequence.py.html
title: DataStructure/AccumulateSum/ImosArithmeticSequence.py
---
