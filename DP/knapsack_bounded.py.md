---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/2370.test.py
    title: TestCase/AOJ/2370.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_1_G.test.py
    title: TestCase/AOJ/DPL_1_G.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def knapsack_bounded(w, items):\n    dp = [0] * (w + 1)\n    deq = [0] *\
    \ (w + 1)\n    deqv = [0] * (w + 1)\n\n    for value, weight, qty in items:\n\
    \        for rem in range(weight):\n            s, t = 0, 0\n            j = 0\n\
    \            while j * weight + rem <= w:\n                val = dp[j * weight\
    \ + rem] - j * value\n                while s < t and deqv[t - 1] <= val:\n  \
    \                  t -= 1\n                deq[t] = j\n                deqv[t]\
    \ = val\n                t += 1\n                dp[j * weight + rem] = deqv[s]\
    \ + j * value\n                if deq[s] == j - qty:\n                    s +=\
    \ 1\n                j += 1\n    return dp\n"
  dependsOn: []
  isVerificationFile: false
  path: DP/knapsack_bounded.py
  requiredBy: []
  timestamp: '2021-05-10 23:34:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DPL_1_G.test.py
  - TestCase/AOJ/2370.test.py
documentation_of: DP/knapsack_bounded.py
layout: document
title: "\u500B\u6570\u5236\u9650\u4ED8\u304D\u30CA\u30C3\u30D7\u30B5\u30C3\u30AF\u554F\
  \u984C"
---

## 概要
個数制限付きナップサック問題を解く。$1$ つの袋と $N$ 個の荷物について、袋に入れる荷物の重さの合計の上限を $W$、各荷物 $i$ の価値を $v_i$、重さを $w_i$、個数を $q_i$ とする。袋に入れる荷物を選ぶとき、価値の合計の最大値を求める。

以下の通りに定式化できる。

$$\begin{aligned}
\max&\quad\sum_{i=1}^{N}v_ix_i&\\
\mathrm{s.t.}&\quad\sum_{i=1}^{N}w_ix_i\leq W,\\
&\quad x_i\in\{0, 1, \cdots, q_i\}\ ,&\quad i=1,\cdots,N.\\
\end{aligned}$$

## 使い方
`knapsack_bounded(w: int, items: Iterable[Tuple[int, int, int]]) -> List[int]`  
荷物の重さの合計が $W_i (i = 0, \cdots, W)$ となるように、`items` から荷物を選んだときの最大価値のリストを返す。各荷物は (価値, 重さ, 個数) のタプルとして与える。計算量 $O(NW)$
