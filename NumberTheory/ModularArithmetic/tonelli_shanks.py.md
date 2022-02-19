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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from random import randint\n\n\ndef euler_criterion(a, p):\n    res = pow(a,\
    \ (p - 1) // 2, p)\n    return 1 if res == 1 else res - p\n\n\ndef tonelli_shanks(a,\
    \ p):\n    a %= p\n    if p == 2:\n        return a\n    if a == 0:\n        return\
    \ 0\n    if euler_criterion(a, p) == -1:\n        return -1\n\n    z = randint(1,\
    \ p - 1)\n    while euler_criterion(z, p) == 1:\n        z = randint(1, p - 1)\n\
    \n    # p - 1 = (2 ** m) * q\n    q, m = p - 1, 0\n    while q & 1 == 0:\n   \
    \     q //= 2\n        m += 1\n\n    c, t = pow(z, q, p), pow(a, q, p)\n    res\
    \ = pow(a, (q + 1) // 2, p)\n    if t == 0:\n        return 0\n\n    m -= 2\n\
    \    while t != 1:\n        while pow(t, 2 ** m, p) == 1:\n            c = c *\
    \ c % p\n            m -= 1\n        res = res * c % p\n        c = c * c % p\n\
    \        t = t * c % p\n        m -= 1\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/ModularArithmetic/tonelli_shanks.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: NumberTheory/ModularArithmetic/tonelli_shanks.py
layout: document
title: "\u5E73\u65B9\u5270\u4F59 (Tonelli-Shanks)"
---

## 概要
整数 $a$ と素数 $p$ が与えられたとき $x^2 \equiv a \pmod{p}$ を満たす $x$ を求めるアルゴリズム。

## 使い方
`tonelli_shanks(a: int, p: int) -> int`  
$x^2 \equiv a \pmod{p}$ を満たす $x$ を返す。そのような $x$ が存在しない場合は `-1` を返す。計算量 $O(\log^2 p)$
