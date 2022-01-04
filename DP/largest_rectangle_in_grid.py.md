---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DP/largest_rectangle_in_histogram.py
    title: "\u30D2\u30B9\u30C8\u30B0\u30E9\u30E0\u4E2D\u306E\u6700\u5927\u9577\u65B9\
      \u5F62"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_3_B.test.py
    title: TestCase/AOJ/DPL_3_B.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DP.largest_rectangle_in_histogram import largest_rectangle_in_histogram\n\
    \n\ndef largest_rectangle_in_grid(grid, wall):\n    h = len(grid)\n    w = len(grid[0])\n\
    \n    hists = [[0] * w for i in range(h)]\n    for j in range(w):\n        if\
    \ grid[0][j] != wall:\n            hists[0][j] = 1\n\n    for i in range(1, h):\n\
    \        for j in range(w):\n            if grid[i][j] != wall:\n            \
    \    hists[i][j] = hists[i - 1][j] + 1\n\n    ans = 0\n    for hist in hists:\n\
    \        ans = max(largest_rectangle_in_histogram(hist), ans)\n    return ans\n"
  dependsOn:
  - DP/largest_rectangle_in_histogram.py
  isVerificationFile: false
  path: DP/largest_rectangle_in_grid.py
  requiredBy: []
  timestamp: '2021-05-10 23:34:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DPL_3_B.test.py
documentation_of: DP/largest_rectangle_in_grid.py
layout: document
title: "\u30B0\u30EA\u30C3\u30C9\u4E2D\u306E\u6700\u5927\u9577\u65B9\u5F62"
---

## 概要
グリッド中の最大長方形の面積を求めるアルゴリズム。

## 使い方
`largest_rectangle_in_grid(grid: Sequence[Sequence[T]], wall: T) -> int`  
サイズ $N \times M$ のグリッド `grid` 中の `wall` を含まない最大長方形の面積を返す。計算量 $O(NM)$
