---
title: functional graph 上の (順列上の) ダブリング
documentation_of: //Graph/misc/Doubling.py
---

## 概要
functional graph 上でダブリングを行う。

## 使い方
`Doubling(permutation: List[int], power: int = 64)`  
$N$ 頂点の functional graph について、頂点 `v` から 頂点 `permutation[v]` への移動に関するダブリング配列を構築する。`(1 << power) - 1` 回が最大の移動回数となる。`k = power` としたとき、計算量 $O(kN)$

- `dest(v: int, times: int) -> int`  
頂点 `v` から `times` 回移動したときの頂点を返す。計算量 $O(k)$

- `build_path(values: List[T], op: Callable[[T, T], T], e: T) -> None`  
頂点 `v` から 頂点 `permutation[v]` への移動時の重み `values[v]` について、畳み込み演算を構築する。演算は二項演算 `op`、単位元 `e` によって定義される。計算量 $O(kN)$

- `fold(v: int, times: int) -> T`  
頂点 `v` から `times` 回移動したときの畳み込みの結果を返す。計算量 $O(k)$

- `max_times(v: int, f: Callable[[T], bool]) -> int`  
頂点 `v` からの移動回数 `times` が `f(times) = True` を満たす最大の `times` を返す。ただし `f(e) = True` であり `f` は単調とする。計算量 $O(k)$
