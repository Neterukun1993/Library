---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/ModularArithmetic/chinese_remainder_theorem.py
    title: "\u4E2D\u56FD\u5270\u4F59\u5B9A\u7406"
  - icon: ':heavy_check_mark:'
    path: NumberTheory/ModularArithmetic/garner.py
    title: "Garner \u306E\u30A2\u30EB\u30B4\u30EA\u30BA\u30E0"
  - icon: ':heavy_check_mark:'
    path: NumberTheory/ModularArithmetic/linear_congruence.py
    title: "\u4E00\u6B21\u5408\u540C\u65B9\u7A0B\u5F0F"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/NTL_1_E.test.py
    title: TestCase/AOJ/NTL_1_E.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def extended_gcd(a, b):\n    if b == 0:\n        return a, 1, 0\n    else:\n\
    \        g, y, x = extended_gcd(b, a % b)\n        y -= (a // b) * x\n       \
    \ return g, x, y\n\n\ndef mod_inv(a, m):\n    _, x, _ = extended_gcd(a, m)\n \
    \   return x % m\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Basic/extended_gcd.py
  requiredBy:
  - NumberTheory/ModularArithmetic/garner.py
  - NumberTheory/ModularArithmetic/chinese_remainder_theorem.py
  - NumberTheory/ModularArithmetic/linear_congruence.py
  timestamp: '2021-05-03 14:23:41+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/NTL_1_E.test.py
documentation_of: NumberTheory/Basic/extended_gcd.py
layout: document
title: "\u62E1\u5F35\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u306E\u4E92\u9664\u6CD5"
---

## 使い方
`extended_gcd(a: int, b: int) -> Tuple[int, int, int]`  
$\gcd(a, b)$ の結果および $ax + by = \gcd(a, b)$ の整数解 $(x, y)$ を返す。計算量 $O(\log \min(a, b))$

`mod_inv(a: int, m: int) -> int`  
整数 $m$ と互いに素な整数 $a$ について $ax \equiv 1 \pmod{m}$ を満たす $x$ を返す。計算量 $O(\log \min(a, m))$
