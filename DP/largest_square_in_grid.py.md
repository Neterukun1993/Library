---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_3_A.test.py
    title: TestCase/AOJ/DPL_3_A.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def largest_square_in_grid(grid, wall):\n    h = len(grid)\n    w = len(grid[0])\n\
    \    dp = [[0] * (w + 1) for i in range(h + 1)]\n\n    ans = 0\n    for i in range(h):\n\
    \        for j in range(w):\n            if grid[i][j] == wall:\n            \
    \    dp[i + 1][j + 1] = 0\n            else:\n                dp[i + 1][j + 1]\
    \ = min(dp[i][j], dp[i + 1][j], dp[i][j + 1]) + 1\n                ans = max(dp[i\
    \ + 1][j + 1], ans)\n    return ans ** 2\n"
  dependsOn: []
  isVerificationFile: false
  path: DP/largest_square_in_grid.py
  requiredBy: []
  timestamp: '2021-05-10 23:34:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DPL_3_A.test.py
documentation_of: DP/largest_square_in_grid.py
layout: document
title: "\u30B0\u30EA\u30C3\u30C9\u4E2D\u306E\u6700\u5927\u6B63\u65B9\u5F62"
---

## 概要
グリッド中の最大正方形の面積を求めるアルゴリズム。

## 使い方
`largest_square_in_grid(grid: Sequence[Sequence[T]], wall: T) -> int`  
サイズ $N \times M$ のグリッド `grid` 中の `wall` を含まない最大正方形の面積を返す。計算量 $O(NM)$
