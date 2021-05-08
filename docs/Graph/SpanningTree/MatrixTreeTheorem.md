---
title: 行列木定理
documentation_of: //Graph/SpanningTree/MatrixTreeTheorem.py
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
