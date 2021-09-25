---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/matrix_pow.unittest.test.py
    title: TestCase/unittest/matrix_pow.unittest.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def matrix_pow(A, k, MOD):\n    def matrix_mul(A, B, MOD):\n        C = [[0]\
    \ * size for _ in range(size)]\n        for i in range(size):\n            for\
    \ k in range(size):\n                for j in range(size):\n                 \
    \   C[i][j] = (C[i][j] + A[i][k] * B[k][j]) % MOD\n        return C\n\n    if\
    \ len(A) != len(A[0]):\n        raise ValueError('square matrix expected')\n\n\
    \    size = len(A)\n    B = [[0] * size for _ in range(size)]\n    for i in range(size):\n\
    \        B[i][i] = 1\n    while k > 0:\n        if k & 1:\n            B = matrix_mul(A,\
    \ B, MOD)\n        A = matrix_mul(A, A, MOD)\n        k = k // 2\n    return B\n\
    \n\ndef matvec_mul(A, vec, MOD):\n    if len(A[0]) != len(vec):\n        raise\
    \ ValueError('dimension mismatch between matrix and vector')\n\n    h, w = len(A),\
    \ len(A[0])\n    res_vec = [0] * h\n    for i in range(h):\n        for j in range(w):\n\
    \            res_vec[i] += A[i][j] * vec[j]\n            res_vec[i] %= MOD\n \
    \   return res_vec\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/misc/matrix_pow.py
  requiredBy: []
  timestamp: '2021-06-07 19:35:09+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/unittest/matrix_pow.unittest.test.py
documentation_of: NumberTheory/misc/matrix_pow.py
layout: document
title: "\u884C\u5217\u7D2F\u4E57"
---

## 概要
行列の累乗を求めるアルゴリズム。

## 使い方
`matrix_pow(A: Sequence[Sequence[int]], k: int, MOD: int) -> List[List[int]]`  
$n$ 次正方行列 $A$ について $A^k$ を返す。行列の各要素は $\mathrm{MOD}$ で割った余りをとる。計算量 $O(n^3 \log k)$

`matvec_mul(A: Sequence[Sequence[int]], vec: Sequence[int], MOD: int) -> List[int]`  
サイズ $n \times m$ の行列 $A$ と $m$ 次元のベクトル $v$ (`vec`) について $Av$ を返す。計算量 $O(nm)$
