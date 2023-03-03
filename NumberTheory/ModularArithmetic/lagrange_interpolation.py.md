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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def lagrange_interpolation_naive(points, T, MOD):\n    n = len(points) -\
    \ 1\n    x, y = list(zip(*points))\n    res = 0\n    for i in range(n + 1):\n\
    \        numer = 1\n        denom = 1\n        for j in range(n + 1):\n      \
    \      if i == j:\n                continue\n            numer *= T - x[j]\n \
    \           numer %= MOD\n            denom *= x[i] - x[j]\n            denom\
    \ %= MOD\n        ci = numer * pow(denom, MOD - 2, MOD) % MOD\n        res +=\
    \ y[i] * ci\n        res %= MOD\n    return res\n\n\ndef lagrange_interpolation(y,\
    \ T, MOD):\n    n = len(y) - 1\n    T %= MOD\n    if 0 <= T <= n:\n        return\
    \ y[T]\n\n    fact = 1\n    inv_fact = [1] * (n + 1)\n    for val in range(1,\
    \ n + 1):\n        fact = fact * val % MOD\n    inv_fact[n] = pow(fact, MOD -\
    \ 2, MOD)\n    for i in reversed(range(1, n + 1)):\n        inv_fact[i - 1] =\
    \ inv_fact[i] * i % MOD\n\n    left = [1] * (n + 1)\n    for i in range(n):\n\
    \        left[i + 1] = (left[i] * (T - i)) % MOD\n\n    r = 1\n    res = 0\n \
    \   for i in reversed(range(n + 1)):\n        numer = r * left[i] % MOD\n    \
    \    denom = inv_fact[i] * inv_fact[n - i] % MOD\n        ci = numer * denom %\
    \ MOD\n        if (n - i) % 2 == 1:\n            ci *= -1\n        res = (res\
    \ + y[i] * ci) % MOD\n        r = r * (T - i) % MOD\n    return res\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/ModularArithmetic/lagrange_interpolation.py
  requiredBy: []
  timestamp: '2022-01-16 22:03:51+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: NumberTheory/ModularArithmetic/lagrange_interpolation.py
layout: document
title: "\u30E9\u30B0\u30E9\u30F3\u30B8\u30E5\u88DC\u9593"
---

## 概要
$x$ が相異なる $n + 1$ 個の点 $(x_0, y_0),\ldots,(x_n, y_n)$ 全てに対して $f(x_i) = y_i$ を満たす $n$ 次多項式 $f$ を考える。このときに $f(T)$ の値を求めるアルゴリズム。

## 使い方
`lagrange_interpolation_naive(points: Iterable[[int, int]], T: int, MOD: int) -> int`  
$N + 1$ 個の点 `points` を通る $N$ 次多項式 $f$ について、$f(T)$ の値を返す。計算量 $O(N^2)$

`lagrange_interpolation(y: Sequence[int], T: int, MOD: int) -> int`  
$N$ 次多項式 $f$ について $f(0), f(1), \ldots, f(N)$ の値を配列 `y` として与えたとき 、$f(T)$ の値を返す。計算量 $O(N + \log\mathrm{MOD})$

## Verify
問題: [ARC003-D 見たことのない多項式](https://atcoder.jp/contests/arc033/tasks/arc033_4)  
提出: https://atcoder.jp/contests/arc033/submissions/28588350