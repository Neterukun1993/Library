---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Combination/modinv_combination.py
    title: "MOD\u4E0A\u3067\u306E\u7D44\u5408\u305B\u8A08\u7B97"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AtCoder/arc117_c.test.py
    title: TestCase/AtCoder/arc117_c.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Combination.modinv_combination import Combination\n\n\nclass LucasTheorem:\n\
    \    def __init__(self, p):\n        self.MOD = p\n        self.cmb = Combination(p\
    \ - 1, p)\n\n    def _p_adic(self, n):\n        res = []\n        while n > 0:\n\
    \            res.append(n % self.MOD)\n            n //= self.MOD\n        return\
    \ res\n\n    def comb(self, n, k):\n        res = 1\n        for ni, ki in zip(self._p_adic(n),\
    \ self._p_adic(k)):\n            res *= self.cmb.comb(ni, ki)\n            res\
    \ %= self.MOD\n        return res\n"
  dependsOn:
  - Combination/modinv_combination.py
  isVerificationFile: false
  path: Combination/LucasTheorem.py
  requiredBy: []
  timestamp: '2021-09-13 00:46:50+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AtCoder/arc117_c.test.py
documentation_of: Combination/LucasTheorem.py
layout: document
title: "Lucas \u306E\u5B9A\u7406"
---
## 概要
二項係数を素数で割ったときのあまりを求める。

## 使い方
`LucasTheorem(p: int)`  
素数 $p$ 上での前計算を行う。計算量 $O(p)$

- `comb(n: int, k: int) -> int`  
${}_n\mathrm{C}_k \pmod{p}$ を返す。計算量 $O(\log k)$
