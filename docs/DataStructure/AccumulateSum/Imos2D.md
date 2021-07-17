---
title: 二次元いもす法
documentation_of: //DataStructure/AccumulateSum/Imos2D.py
---

## 使い方
`Imos2D(h: int, w: int)`  
大きさ $h × w$ のいもす法用の二次元配列を初期構築する。計算量 $O(hw)$  
その後の一連の処理としては

1. `add` 関数で矩形加算の準備をする。
2. `build` 関数で矩形加算を実行する。
3. `__getitem__` 関数で値を取得する。

となる。

- `add(hl: int, hr: int, wl: int, wr: int, val: int) -> None`  
矩形範囲 $\lbrack hl, hr) × \lbrack wl, wr)$ の要素に `val` を加える準備をする。計算量 $O(1)$

- `build() -> None`  
`add` による矩形加算を実行する。計算量 $O(hw)$

- `__getitem__(i: int).__getitem__(j: int) -> int`  
$i$ 行 $j$ 列目の要素を返す。計算量 $O(1)$

## 参考
[いもす法 - いもす研 (imos laboratory)](https://imoz.jp/algorithms/imos_method.html)
