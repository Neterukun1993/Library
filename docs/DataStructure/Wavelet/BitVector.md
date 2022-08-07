---
title: ビットベクトル
documentation_of: //DataStructure/Wavelet/BitVector.py
---
## 概要
各要素が $0$ もしくは $1$ に限定される配列の構築を $O(n)$、区間和を $O(1)$ で行えるデータ構造。通常の累積和よりも省メモリである。

## 使い方
`BitVector(n: int)`  
長さが $n$ で全要素が $0$ であるビットベクトルを構築する。計算量 $O(n)$

- `set(i: int) -> None`  
$i$ 番目の要素を $1$ に更新する。計算量 $O(1)$

- `access(i) -> int`  
$i$ 番目の値を返す。計算量 $O(1)$

- `build() -> None`  
ビットベクトルに対する累積和を構築する。計算量 $O(n)$

- `rank(r: int, f: bool) -> int`  
$[0, r)$ 番目について、`f = True` のとき $1$ の個数を、`f = False` のとき $0$ の個数を返す。計算量 $O(1)$