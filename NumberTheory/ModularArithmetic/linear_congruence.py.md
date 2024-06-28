---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Basic/extended_gcd.py
    title: "\u62E1\u5F35\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u306E\u4E92\u9664\u6CD5"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/linear_congruence.unittest.test.py
    title: TestCase/unittest/linear_congruence.unittest.test.py
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
  code: "from NumberTheory.Basic.extended_gcd import extended_gcd\n\n\ndef linear_congruence(a,\
    \ b, m):\n    def gcd(a, b):\n        while b:\n            a, b = b, a % b\n\
    \        return a\n\n    if b % gcd(a, m) != 0:\n        # \u89E3\u306A\u3057\n\
    \        return False, -1, -1\n    g, x, y = extended_gcd(a, m)\n    x *= b //\
    \ g\n    cycle = m // g\n    x -= cycle * (x // cycle)\n    return True, x, cycle\n"
  dependsOn:
  - NumberTheory/Basic/extended_gcd.py
  isVerificationFile: false
  path: NumberTheory/ModularArithmetic/linear_congruence.py
  requiredBy: []
  timestamp: '2021-05-03 14:23:41+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/unittest/linear_congruence.unittest.test.py
documentation_of: NumberTheory/ModularArithmetic/linear_congruence.py
layout: document
title: "\u4E00\u6B21\u5408\u540C\u65B9\u7A0B\u5F0F"
---

## 概要
一次合同方程式 $ax \equiv b \pmod{m}$ を解くアルゴリズム。

## 使い方
`linear_congruence(a: int, b: int, m: int) -> Tuple[bool, int, int]`  
一次合同方程式 $ax \equiv b \pmod{m}$ に対して (解が存在するか, 最小の非負整数解, 解の周期) を返す。解が存在しない場合は `(False, -1, -1)` を返す。計算量 $O(\log \min(b, m))$
