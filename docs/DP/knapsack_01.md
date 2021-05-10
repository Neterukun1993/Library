---
title: 0-1 ナップサック問題
documentation_of: //DP/knapsack_01.py
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
`knapsack_01(w: int, items: Iterable[Tuple[int, int]]) -> List[int]`  
荷物の重さの合計が $W_i (i = 0, \cdots, W)$ となるように、`items` から荷物を選んだときの最大価値のリストを返す。各荷物は (価値, 重さ) のタプルとして与える。計算量 $O(NW)$
