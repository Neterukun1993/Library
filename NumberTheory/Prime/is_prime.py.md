---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_1_C.test.py
    title: TestCase/AOJ/ALDS1_1_C.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def is_prime(x):\n    if x == 2:\n        return True\n    if x == 1 or x\
    \ % 2 == 0:\n        return False\n    for k in range(3, int(x ** 0.5) + 1, 2):\n\
    \        if x % k == 0:\n            return False\n    return True\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Prime/is_prime.py
  requiredBy: []
  timestamp: '2021-03-05 15:07:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_1_C.test.py
documentation_of: NumberTheory/Prime/is_prime.py
layout: document
title: "\u7D20\u6570\u5224\u5B9A (\u8A66\u3057\u5272\u308A\u6CD5)"
---

## 概要
$O(\sqrt n)$ で素数判定を行うアルゴリズム。

## 使い方
`is_prime(x: int) -> bool`  
`x` の素数判定結果 (`True`: 素数である、`False`: 素数ではない) を返す。計算量 $O(\sqrt n)$
