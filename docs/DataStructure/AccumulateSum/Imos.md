---
title: いもす法
documentation_of: //DataStructure/AccumulateSum/Imos.py
---

## 使い方
`Imos(n: int)`  
大きさ `n` のいもす法用の配列を初期構築する。計算量 $O(n)$  
その後の一連の処理としては

1. `add` 関数で区間加算の準備をする。
2. `build` 関数で区間加算を実行する。
3. `__getitem__` 関数で値を取得する。

となる。

- `add(l: int, r: int, val: int) -> None`  
`[l, r)` 番目の要素に `val` を加える準備をする。計算量 $O(1)$

- `build() -> None`  
`add` による区間加算を実行する。計算量 $O(n)$

- `__getitem__(i: int) -> int`  
`i` 番目の要素を返す。計算量 $O(1)$
