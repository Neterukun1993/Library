---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Basic/extended_gcd.py
    title: "\u62E1\u5F35\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u306E\u4E92\u9664\u6CD5"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0186.test.py
    title: TestCase/yukicoder/yuki0186.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from NumberTheory.Basic.extended_gcd import extended_gcd\n\n\ndef chinese_remainder_theorem(a,\
    \ m):\n    r, M = 0, 1\n    for i in range(len(a)):\n        g, p, q = extended_gcd(M,\
    \ m[i])\n        if (a[i] - r) % g != 0:\n            return -1, -1\n        tmp\
    \ = (a[i] - r) // g * p % (m[i] // g)\n        r += M * tmp\n        M *= m[i]\
    \ // g\n    return r % M, M\n"
  dependsOn:
  - NumberTheory/Basic/extended_gcd.py
  isVerificationFile: false
  path: NumberTheory/ModularArithmetic/chinese_remainder_theorem.py
  requiredBy: []
  timestamp: '2021-05-03 14:23:41+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki0186.test.py
documentation_of: NumberTheory/ModularArithmetic/chinese_remainder_theorem.py
layout: document
title: "\u4E2D\u56FD\u5270\u4F59\u5B9A\u7406"
---

## 概要
$m_0, m_1, \cdots, m_{n - 1}$ と $a_0, a_1, \cdots, a_{n - 1}$ について

$$\left\{\begin{array}{l}x \equiv a_0 \pmod{m_0}\\x \equiv a_1 \pmod{m_1}\\ \cdots \\x \equiv a_{n - 1} \pmod{m_{n - 1}}\end{array}\right.$$

を満たす $x$ を求めるアルゴリズム。

## 使い方
`chinese_remainder_theorem(a: Sequence[int], m: Sequence[int]) -> Tuple[int, int]`  
$i = 0, 1, \cdots, n - 1$ について $x \equiv a_i \pmod{m_i}$ を満たす $x (0 \le x \lt \mathrm{lcm}(m[i]))$ とその周期 $\mathrm{lcm}(m[i])$ を返す。そのような $x$ が存在しない場合は $(-1, -1)$ を返す。計算量 $O(n \log \mathrm{lcm}(m[i]))$
