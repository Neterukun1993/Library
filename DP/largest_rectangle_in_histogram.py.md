---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DP/largest_rectangle_in_grid.py
    title: "\u30B0\u30EA\u30C3\u30C9\u4E2D\u306E\u6700\u5927\u9577\u65B9\u5F62"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_3_C.test.py
    title: TestCase/AOJ/DPL_3_C.test.py
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
  code: "def largest_rectangle_in_histogram(heights):\n    heights = heights + [-1]\
    \  # sentinel\n    ans = 0\n    stack = []\n    for i, height in enumerate(heights):\n\
    \        idx = i\n        while True:\n            if not stack or stack[-1][0]\
    \ <= height:\n                stack.append((height, idx))\n                break\n\
    \            else:\n                h, l = stack.pop()\n                ans =\
    \ max(h * (i - l), ans)\n                idx = l\n    return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: DP/largest_rectangle_in_histogram.py
  requiredBy:
  - DP/largest_rectangle_in_grid.py
  timestamp: '2021-05-07 04:49:50+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DPL_3_C.test.py
documentation_of: DP/largest_rectangle_in_histogram.py
layout: document
title: "\u30D2\u30B9\u30C8\u30B0\u30E9\u30E0\u4E2D\u306E\u6700\u5927\u9577\u65B9\u5F62"
---

## 概要
ヒストグラム中の最大長方形の面積を求めるアルゴリズム。スタックを用いた方法により、ビンの数の線形時間で計算できる。

## 使い方
`largest_rectangle_in_histogram(heights: Sequence[int]) -> int`  
$N$ 個のビン `heights` を持つヒストグラム中の最大長方形の面積を返す。計算量 $O(N)$
