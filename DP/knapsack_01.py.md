---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_1_B.test.py
    title: TestCase/AOJ/DPL_1_B.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def knapsack_01(w, items):\n    n = len(items)\n    dp = [-1] * (w + 1)\n\
    \    dp[0] = 0\n\n    for value, weight in items:\n        for j in reversed(range(weight,\
    \ w + 1)):\n            if dp[j - weight] == -1:\n                continue\n \
    \           else:\n                dp[j] = max(dp[j], dp[j - weight] + value)\n\
    \    return max(dp)\n"
  dependsOn: []
  isVerificationFile: false
  path: DP/knapsack_01.py
  requiredBy: []
  timestamp: '2021-05-04 20:55:07+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DPL_1_B.test.py
documentation_of: DP/knapsack_01.py
layout: document
title: "0-1 \u30CA\u30C3\u30D7\u30B5\u30C3\u30AF\u554F\u984C"
---

## 概要
$0$-$1$ ナップサック問題を解く。$1$ つの袋と $N$ 個の荷物について、袋に入れる荷物の重さの合計の上限を $W$、各荷物 $i$ の価値を $v_i$、重さを $w_i$ とする。袋に入れる荷物を選ぶとき、価値の合計の最大値を求める。

以下の通りに定式化できる。

$$\begin{aligned}
\max&\quad\sum_{i=1}^{N}v_ix_i&\\
\mathrm{s.t.}&\quad\sum_{i=1}^{N}w_ix_i\leq W,\\
&\quad x_i\in\{0, 1\}\ ,&\quad i=1,\cdots,N.\\
\end{aligned}$$

## 使い方
`knapsack_01(w: int, items: Iterable[Tuple[int, int]]) -> int`  
荷物の重さの合計が `w` 以下になるように、`items` から荷物を選んだときの価値の合計の最大値を返す。各荷物は (価値, 重さ) のタプルとして与える。計算量 $O(NW)$
