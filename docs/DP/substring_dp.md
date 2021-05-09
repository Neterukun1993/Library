---
title: 部分列 DP
documentation_of: //DP/substring_dp.py
---

## 概要
小文字英字列 $S$ に対して部分列の通り数を求めるアルゴリズム。$\mathrm{nxt}$ 配列を使うことで数え上げの重複を防ぐのがポイント。

#### $\mathrm{nxt}$ 配列定義  
$\mathrm{nxt}[i][j] :=$ $S$ の $i$ 文字目以降で初めて $\mathrm{chr}(j + 97)$ が登場するときのインデックス (すべて $1$-indexed)

#### 状態遷移  
状態を $\mathrm{dp}[i] :=$ $S$ の部分列で $i$ 文字目を最後に使用するときの通り数、とする。このときの遷移式は以下の通りとなる。

$\left\{\begin{array}{l}
\mathrm{dp}[0] = 1\\
\mathrm{dp}[\mathrm{nxt}[i][j]]\mathrel{+}=dp[i]
\end{array}\right.$

## 使い方
- `calc_next(small_characters: Sequence) -> List[List[int]]`  
長さ $N$、文字種類数 $\sigma = 26$ の小文字英字列 `small_characters` について、 $\mathrm{nxt}$ 配列を返す。計算量 $O(\sigma N)$

- `substring_dp(small_characters: Sequence, MOD: int) -> int`  
長さ $N$、文字種類数 $\sigma = 26$ の小文字英字列 `small_characters` について、部分列の通り数を $\mathrm{MOD}$ で割った余りを返す。計算量 $O(\sigma N)$

## 参考
[部分列 DP --- 文字列の部分文字列を重複なく走査する DP の特集](https://qiita.com/drken/items/a207e5ae3ea2cf17f4bd)
