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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class MatrixTreeTheorem:\n    def __init__(self, n):\n        self.n = n\n\
    \        self.lap_mat = [[0] * n for i in range(n)]\n\n    def _determinant(self,\
    \ mat, MOD):\n        n = len(mat)\n        det, rank = 1, 0\n        for col\
    \ in range(n):\n            pivot = -1\n            for row in range(col, n):\n\
    \                if mat[row][col] != 0:\n                    pivot = row\n   \
    \                 break\n            if pivot == -1:\n                return 0\n\
    \            if pivot != rank:\n                mat[rank], mat[pivot] = mat[pivot],\
    \ mat[rank]\n                det *= -1\n            det *= mat[rank][rank]\n \
    \           det %= MOD\n            inv = pow(mat[rank][rank], MOD - 2, MOD)\n\
    \            for col2 in range(col, n):\n                mat[rank][col2] = mat[rank][col2]\
    \ * inv % MOD\n            for row in range(rank + 1, n):\n                fac\
    \ = mat[row][col]\n                for col2 in range(col, n):\n              \
    \      mat[row][col2] -= mat[rank][col2] * fac\n                    mat[row][col2]\
    \ %= MOD\n            rank += 1\n        return det\n\n    def add_edge(self,\
    \ u, v):\n        self.lap_mat[u][u] += 1\n        self.lap_mat[v][v] += 1\n \
    \       self.lap_mat[u][v] -= 1\n        self.lap_mat[v][u] -= 1\n\n    def count_st(self,\
    \ MOD):\n        mat = [[val for val in rows[:-1]] for rows in self.lap_mat[:-1]]\n\
    \        return self._determinant(mat, MOD)\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/SpanningTree/MatrixTreeTheorem.py
  requiredBy: []
  timestamp: '2021-05-08 15:33:29+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/SpanningTree/MatrixTreeTheorem.py
layout: document
title: "\u884C\u5217\u6728\u5B9A\u7406"
---

## 概要
全域木の通り数を求めるアルゴリズム。行列木定理「無向グラフ $G$ の全域木の通り数は、$G$ のラプラシアン行列の任意の余因子に等しい」を用いて求める。

## 使い方
`MatrixTreeTheorem(n: int)`  
頂点数 `n` の空グラフを構築 (ラプラシアン行列を初期化) する。計算量 $O(N^2)$

- `add_edge(u, v) -> None`  
頂点 `u` と頂点 `v` 間に辺を追加する。計算量 $O(1)$

- `count_st(MOD: int) -> None`  
全域木の通り数を `MOD` で割った余りを返す。計算量 $O(N^3)$
