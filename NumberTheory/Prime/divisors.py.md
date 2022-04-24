---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ITP1_3_D.test.py
    title: TestCase/AOJ/ITP1_3_D.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def divisors(n):\n    divs = []\n    for k in range(1, int(n ** 0.5) + 1):\n\
    \        if n % k == 0:\n            divs.append(k)\n            if k != n //\
    \ k:\n                divs.append(n // k)\n    divs = sorted(divs)\n    return\
    \ divs\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Prime/divisors.py
  requiredBy: []
  timestamp: '2021-04-30 21:12:45+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ITP1_3_D.test.py
documentation_of: NumberTheory/Prime/divisors.py
layout: document
title: "\u7D04\u6570\u5217\u6319 (\u8A66\u3057\u5272\u308A\u6CD5)"
---

## 概要
$O(\sqrt n)$ で約数列挙を行うアルゴリズム。

## 使い方
`divisors(n: int) -> List[int]`  
整数 `n` の約数を昇順列挙した結果のリストを返す。計算量 $O(\sqrt n)$
