---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: Combination/twelvefold_way.py
    title: "\u5199\u50CF12\u76F8(twelvefold way)"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_5_E.naive.test.py
    title: TestCase/AOJ/DPL_5_E.naive.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.8.7/x64/lib/python3.8/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.8.7/x64/lib/python3.8/site-packages/onlinejudge_verify/languages/python.py\"\
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
    \ * self.inv_f[k - r] * self.inv_f[r]) % self.MOD\n\n\ndef combination(k, r, MOD):\n\
    \    \"\"\"kCr O(r)\"\"\"\n    if k < r:\n        return 0\n    r = min(r, k -\
    \ r)\n    numer, denom = 1, 1\n    for l in range(r):\n        numer *= (k - l)\n\
    \        numer %= MOD\n        denom *= l + 1\n        denom %= MOD\n    return\
    \ numer * pow(denom, MOD - 2, MOD) % MOD\n"
  dependsOn: []
  isVerificationFile: false
  path: Combination/modinv_combination.py
  requiredBy:
  - Combination/twelvefold_way.py
  timestamp: '2021-01-06 00:51:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DPL_5_E.naive.test.py
documentation_of: Combination/modinv_combination.py
layout: document
title: "MOD\u4E0A\u3067\u306E\u7D44\u5408\u305B\u8A08\u7B97"
---
