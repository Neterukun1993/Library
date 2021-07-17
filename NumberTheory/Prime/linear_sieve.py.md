---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_1_C.linear_sieve.test.py
    title: TestCase/AOJ/ALDS1_1_C.linear_sieve.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def linear_sieve(n):\n    prime_list = []\n    mindiv_factor = [i for i in\
    \ range(n + 1)]\n    for i in range(2, n + 1):\n        if mindiv_factor[i] ==\
    \ i:\n            prime_list.append(i)\n        for p in prime_list:\n       \
    \     if p * i > n or p > mindiv_factor[i]:\n                break\n         \
    \   mindiv_factor[p * i] = p\n    return prime_list, mindiv_factor\n\n\ndef prime_factors(n,\
    \ mindiv_factor):\n    pf = []\n    while mindiv_factor[n] != 1:\n        pf.append(mindiv_factor[n])\n\
    \        n //= mindiv_factor[n]\n    return pf\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Prime/linear_sieve.py
  requiredBy: []
  timestamp: '2021-03-05 15:07:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_1_C.linear_sieve.test.py
documentation_of: NumberTheory/Prime/linear_sieve.py
layout: document
title: "\u7D20\u6570\u5217\u6319 + \u7D20\u56E0\u6570\u5206\u89E3 (\u7DDA\u5F62\u7BE9\
  )"
---

## 概要
$O(n)$ で素数列挙を行うアルゴリズム。副産物の最小素因数によって $O(\log n)$ で素因数分解ができる。

## 使い方
`linear_sieve(n: int) -> Tuple[List[int], List[int]]`  
整数 `n` 以下の素数のリストと、各整数について最小素因数のテーブルを返す。計算量 $O(n)$

`prime_factors(n: int, mindiv_factor: Sequence[int]) -> List[int]`  
整数 `n` を素因数分解した結果のリストを返す。線形篩によって求めた最小素因数のテーブル `mindiv_factor` を引数に取る。計算量 $O(\log n)$
