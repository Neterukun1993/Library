---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/system_of_linear_equations.test.py
    title: TestCase/LibraryChecker/system_of_linear_equations.test.py
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
  code: "MOD = 998244353\n\n\ndef linear_equations(matrix, vector):\n    n = len(matrix)\n\
    \    m = len(matrix[0])\n\n    if len(vector) != n:\n        raise RuntimeError('The\
    \ number of rows of the matrix and the length of the vector must be the same.')\n\
    \    if any(len(row) != m for row in matrix):\n        raise RuntimeError('The\
    \ number of columns of the matrix must be the same.')\n\n    # \u62E1\u5927\u4FC2\
    \u6570\u884C\u5217\u3092\u4F5C\u6210\n    A = [matrix[i] + [vector[i]] for i in\
    \ range(n)]\n\n    # \u30D4\u30DC\u30C3\u30C8\u3068\u3057\u3066\u9078\u629E\u3055\
    \u308C\u305F\u5217\u3068\u9078\u629E\u3055\u308C\u306A\u304B\u3063\u305F\u5217\
    \n    pivot_cols = []\n    no_pivot_cols = []\n\n    # \u6383\u304D\u51FA\u3057\
    \u6CD5\n    def _gauss_jordan():\n        rank = 0\n        for col in range(m):\n\
    \            # \u30D4\u30DC\u30C3\u30C8\u3092\u63A2\u3059\n            pivot =\
    \ -1\n            for row in range(rank, n):\n                if A[row][col] !=\
    \ 0:\n                    pivot = row\n                    break\n\n         \
    \   # \u30D4\u30DC\u30C3\u30C8\u304C\u306A\u3044\u5834\u5408\u306B\u306F\u6B21\
    \u306E\u5217\u306B\n            if pivot == -1:\n                no_pivot_cols.append(col)\n\
    \                continue\n            pivot_cols.append(col)\n\n            #\
    \ \u884C\u3092\u30B9\u30EF\u30C3\u30D7\n            A[pivot], A[rank] = A[rank],\
    \ A[pivot]\n\n            # \u30D4\u30DC\u30C3\u30C8\u306E\u5024\u3092 1 \u306B\
    \u3059\u308B\n            inv = pow(A[rank][col], MOD - 2, MOD)\n            for\
    \ col2 in range(m + 1):\n                A[rank][col2] *= inv\n              \
    \  A[rank][col2] %= MOD\n\n            # \u30D4\u30DC\u30C3\u30C8\u306E\u3042\u308B\
    \u5217\u306E\u5024\u304C\u3059\u3079\u3066 0 \u306B\u306A\u308B\u3088\u3046\u306B\
    \u6383\u304D\u51FA\u3059\n            for row in range(n):\n                if\
    \ row == rank or A[row][col] == 0:\n                    continue\n           \
    \     fac = A[row][col]\n                for col2 in range(m + 1):\n         \
    \           A[row][col2] -= A[rank][col2] * fac\n                    A[row][col2]\
    \ %= MOD\n\n            rank += 1\n\n        return rank\n\n    rank = _gauss_jordan()\n\
    \    for row in range(rank, n):\n        if A[row][m] != 0:\n            # \u89E3\
    \u304C\u5B58\u5728\u3057\u306A\u3044\u5834\u5408\n            return -1, [], []\n\
    \n    dimension = m - rank  # \u89E3\u304C\u4E00\u610F\u306E\u5834\u5408\u306F\
    \ 0, \u89E3\u304C\u7121\u6570\u306B\u5B58\u5728\u3059\u308B\u5834\u5408\u306F\
    \ 1 \u4EE5\u4E0A\n\n    # \u89E3\u30921\u3064\u6C42\u3081\u308B\n    result =\
    \ [0] * m\n    for i in range(rank):\n        result[pivot_cols[i]] = A[i][m]\n\
    \n    # \u57FA\u5E95\u30D9\u30AF\u30C8\u30EB\u3092\u6C42\u3081\u308B\n    basis_vectors\
    \ = []\n\n    for i in no_pivot_cols:\n        vec = [0] * m\n        vec[i] =\
    \ 1\n        for j in range(rank):\n            vec[pivot_cols[j]] = -A[j][i]\
    \ % MOD\n        basis_vectors.append(vec)\n\n    return dimension, result, basis_vectors\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/ModularArithmetic/linear_equations.py
  requiredBy: []
  timestamp: '2024-08-18 03:37:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/system_of_linear_equations.test.py
documentation_of: NumberTheory/ModularArithmetic/linear_equations.py
layout: document
title: "\u9023\u7ACB\u4E00\u6B21\u65B9\u7A0B\u5F0F"
---

## 概要
連立一次方程式 $Ax \equiv b \pmod{998244353}$ を解く。

## 使い方
`linear_equations(matrix: Sequence[Sequence[int]], vector: Sequence[int]) -> List[int, List[int], List[List[int]]]`  
$N \times M$ の係数行列 $A$ (`matrix`) と $N$ 次元ベクトル $b$ (`vector`) を与えたとき、$Ax \equiv b \pmod{998244353}$ を満たす $M$ 次元ベクトル $x$ (`result`) を返す。
$x$ が存在しない場合は `dimension` は `-1` を返す。$x$ が一意に定まる場合は `dimension` は `0` を返す。$x$ が無数に存在する場合は `dimension` は 1 以上を返す。
