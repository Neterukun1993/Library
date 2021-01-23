---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: Combination\twelvefold_way.py
    title: "\u5199\u50CF12\u76F8"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DPL_5_E.naive.test.py
    title: TestCase\AOJ\DPL_5_E.naive.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\yukicoder\yuki0117.test.py
    title: TestCase\yukicoder\yuki0117.test.py
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
  code: "class Combination:\r\n    def __init__(self, n, MOD):\r\n        self.f =\
    \ [1]\r\n        for i in range(1, n + 1):\r\n            self.f.append(self.f[-1]\
    \ * i % MOD)\r\n        self.inv_f = [0] * (n + 1)\r\n        self.inv_f[n] =\
    \ pow(self.f[n], MOD - 2, MOD)\r\n        for i in reversed(range(n)):\r\n   \
    \         self.inv_f[i] = self.inv_f[i + 1] * (i + 1) % MOD\r\n        self.MOD\
    \ = MOD\r\n\r\n    def inv(self, k):\r\n        \"\"\"get inverse(k)\"\"\"\r\n\
    \        return (self.inv_f[k] * self.f[k - 1]) % self.MOD\r\n\r\n    def fact(self,\
    \ k):\r\n        \"\"\"get k!\"\"\"\r\n        return self.f[k]\r\n\r\n    def\
    \ inv_fact(self, k):\r\n        \"\"\"get inverse(k!)\"\"\"\r\n        return\
    \ self.inv_f[k]\r\n\r\n    def perm(self, k, r):\r\n        \"\"\"get kPr\"\"\"\
    \r\n        if k < r:\r\n            return 0\r\n        return (self.f[k] * self.inv_f[k\
    \ - r]) % self.MOD\r\n\r\n    def comb(self, k, r):\r\n        \"\"\"get kCr\"\
    \"\"\r\n        if k < r:\r\n            return 0\r\n        return (self.f[k]\
    \ * self.inv_f[k - r] * self.inv_f[r]) % self.MOD\r\n\r\n\r\ndef combination(k,\
    \ r, MOD):\r\n    \"\"\"kCr O(r)\"\"\"\r\n    if k < r:\r\n        return 0\r\n\
    \    r = min(r, k - r)\r\n    numer, denom = 1, 1\r\n    for l in range(r):\r\n\
    \        numer *= (k - l)\r\n        numer %= MOD\r\n        denom *= l + 1\r\n\
    \        denom %= MOD\r\n    return numer * pow(denom, MOD - 2, MOD) % MOD\r\n"
  dependsOn: []
  isVerificationFile: false
  path: Combination\modinv_combination.py
  requiredBy:
  - Combination\twelvefold_way.py
  timestamp: '2021-01-06 00:51:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\DPL_5_E.naive.test.py
  - TestCase\yukicoder\yuki0117.test.py
documentation_of: Combination\modinv_combination.py
layout: document
title: "MOD\u4E0A\u3067\u306E\u7D44\u5408\u305B\u8A08\u7B97"
---
## 使い方
`Combination(n: int, MOD: int)`  
$\mathrm{MOD}$ 上での $k!$ とその逆元を、$k = 0,\dots,n$ の範囲で前計算する。計算量 $\mathrm{O}(n + \log(\mathrm{MOD}))$
- `inv(k: int) -> int`  
$k$ の逆元を返す。計算量 $\mathrm{O}(1)$
- `fact(k: int) -> int`  
$k!$ を返す。計算量 $\mathrm{O}(1)$
- `inv_fact(k: int) -> int`  
$k!$ の逆元を返す。計算量 $\mathrm{O}(1)$
- `perm(k: int, r: int) -> int`  
${}_k\mathrm{P}_r$ を返す。計算量 $\mathrm{O}(1)$
- `comb(k: int, r: int) -> int`  
${}_k\mathrm{C}_r$ を返す。計算量 $\mathrm{O}(1)$

`combination(k: int, r: int, MOD: int) -> int`  
$\mathrm{MOD}$ 上での ${}_k\mathrm{C}_r$ をナイーブに計算して返す。計算量 $\mathrm{O}(\min(r, k - r))$
