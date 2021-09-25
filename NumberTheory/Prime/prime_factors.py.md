---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/NTL_1_A.test.py
    title: TestCase/AOJ/NTL_1_A.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def prime_factors(n):\n    factors = []\n    for k in range(2, int(n ** 0.5)\
    \ + 1):\n        while n % k == 0:\n            factors.append(k)\n          \
    \  n = n // k\n    if n != 1:\n        factors.append(n)\n    return factors\n\
    \n\ndef prime_factors_distinct(n):\n    factors = []\n    for k in range(2, int(n\
    \ ** 0.5) + 1):\n        if n % k == 0:\n            factors.append(k)\n     \
    \       while n % k == 0:\n                n = n // k\n    if n != 1:\n      \
    \  factors.append(n)\n    return factors\n\n\ndef prime_factors_compress(n):\n\
    \    factors = []\n    for k in range(2, int(n ** 0.5) + 1):\n        cnt = 0\n\
    \        while n % k == 0:\n            cnt += 1\n            n = n // k\n   \
    \     if cnt != 0:\n            factors.append((k, cnt))\n    if n != 1:\n   \
    \     factors.append((n, 1))\n    return factors\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Prime/prime_factors.py
  requiredBy: []
  timestamp: '2021-03-05 15:07:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/NTL_1_A.test.py
documentation_of: NumberTheory/Prime/prime_factors.py
layout: document
title: "\u7D20\u56E0\u6570\u5206\u89E3 (\u8A66\u3057\u5272\u308A\u6CD5)"
---

## 概要
$O(\sqrt n)$ で素因数分解を行うアルゴリズム。

## 使い方
`prime_factors(n: int) -> List[int]`  
整数 `n` を素因数分解した結果のリストを返す。計算量 $O(\sqrt n)$

`prime_factors_distinct(n, int) -> List[int]`  
整数 `n` を素因数分解し、素因数の重複を除いた結果のリストを返す。計算量 $O(\sqrt n)$

`prime_factors_compress(n, int) -> List[Tuple[int, int]]`  
整数 `n` を素因数分解し、(素因数, 素因数の個数) の組として結果のリストを返す。計算量 $O(\sqrt n)$
