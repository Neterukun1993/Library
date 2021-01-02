---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: Combination/twelvefold_way.py
    title: Combination/twelvefold_way.py
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Combination:\n    def __init__(self, n, MOD):\n        self.f = [1]\n\
    \        for i in range(1, n + 1):\n            self.f.append(self.f[-1] * i %\
    \ MOD)\n        self.inv_f = [0] * (n + 1)\n        self.inv_f[n] = pow(self.f[n],\
    \ MOD - 2, MOD)\n        for i in reversed(range(n)):\n            self.inv_f[i]\
    \ = self.inv_f[i + 1] * (i + 1) % MOD\n        self.MOD = MOD\n\n    def inv(self,\
    \ k):\n        \"\"\"get inverse(k)\"\"\"\n        return (self.inv_f[k] * self.f[k\
    \ - 1]) % self.MOD\n\n    def fact(self, k):\n        \"\"\"get k!\"\"\"\n   \
    \     return self.f[k]\n\n    def inv_fact(self, k):\n        \"\"\"get inverse(k!)\"\
    \"\"\n        return self.inv_f[k]\n\n    def perm(self, k, r):\n        \"\"\"\
    get kPr\"\"\"\n        if k < r:\n            return 0\n        return (self.f[k]\
    \ * self.inv_f[k - r]) % self.MOD\n\n    def comb(self, k, r):\n        \"\"\"\
    get kCr\"\"\"\n        if k < r:\n            return 0\n        return (self.f[k]\
    \ * self.inv_f[k - r] * self.inv_f[r]) % self.MOD\n"
  dependsOn: []
  isVerificationFile: false
  path: Combination/modinv_combination.py
  requiredBy:
  - Combination/twelvefold_way.py
  timestamp: '2021-01-02 19:40:35+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Combination/modinv_combination.py
layout: document
redirect_from:
- /library/Combination/modinv_combination.py
- /library/Combination/modinv_combination.py.html
title: Combination/modinv_combination.py
---
