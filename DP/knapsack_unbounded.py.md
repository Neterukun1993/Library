---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_1_C.test.py
    title: TestCase/AOJ/DPL_1_C.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def knapsack_unbounded(w, items):\n    dp = [-1] * (w + 1)\n    dp[0] = 0\n\
    \n    for value, weight in items:\n        for j in range(weight, w + 1):\n  \
    \          if dp[j - weight] == -1:\n                continue\n            else:\n\
    \                dp[j] = max(dp[j], dp[j - weight] + value)\n    return dp\n"
  dependsOn: []
  isVerificationFile: false
  path: DP/knapsack_unbounded.py
  requiredBy: []
  timestamp: '2021-05-10 23:34:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DPL_1_C.test.py
documentation_of: DP/knapsack_unbounded.py
layout: document
title: "\u500B\u6570\u5236\u9650\u306A\u3057\u30CA\u30C3\u30D7\u30B5\u30C3\u30AF\u554F\
  \u984C"
---

## 概要
個数制限なしナップサック問題を解く。$1$ つの袋と $N$ 個の荷物について、袋に入れる荷物の重さの合計の上限を $W$、各荷物 $i$ の価値を $v_i$、重さを $w_i$ とする。袋に入れる荷物を選ぶとき、価値の合計の最大値を求める。ただし、同じ種類の荷物をいくつでも選ぶことができる。

以下の通りに定式化できる。

$$\begin{aligned}
\max&\quad\sum_{i=1}^{N}v_ix_i&\\
\mathrm{s.t.}&\quad\sum_{i=1}^{N}w_ix_i\leq W,\\
&\quad x_i\ge 0 ,\ x_i \in \mathbb{N}　&\quad i=1,\cdots,N.\\
\end{aligned}$$

## 使い方
`knapsack_unbounded(w: int, items: Iterable[Tuple[int, int]]) -> List[int]`  
荷物の重さの合計が $W_i (i = 0, \cdots, W)$ となるように、`items` から荷物を選んだときの最大価値のリストを返す。各荷物は (価値, 重さ) のタプルとして与える。計算量 $O(NW)$
