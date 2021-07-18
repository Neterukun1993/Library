---
title: Offline Dynamic Connectivity
documentation_of: //DataStructure/UnionFind/OfflineDynamicConnectivity.py
---

## 概要
無向グラフに対して、辺の追加や削除がある場合の連結判定をオフラインで実行する。

## 使い方
`OfflineDynamicConnectivity(q: int, questions: Sequence[Tuple[int, int, int]], n: int)`  
$n$ 頂点の辺のない無向グラフを初期構築する。予め $q$ 個のクエリを与えておく。計算量 $O(n + q)$  
$i$ 番目のクエリ `questions[i]` の意味は次の通りである。
```
t u v
```
時刻 $t$ のとき、頂点 $u$ と頂点 $v$ は連結か？

- `insert(t: int, u: int, v: int) -> None`  
時刻 $t$ において、頂点 $u$ と頂点 $v$ に辺を張るという操作を与える。**時刻 $t$ は、最後に `insert` や `merge` を行ったときの時刻 $t_{\mathrm{last}}$ よりも大きくすること！** 計算量 $O(1)$

- `erase(t: int, u: int, v: int) -> None`  
時刻 $t$ において、頂点 $u$ と頂点 $v$ の辺を削除するという操作を与える。**時刻 $t$ は、最後に `insert` や `merge` を行ったときの時刻 $t_{\mathrm{last}}$ よりも大きくすること！** 計算量 $O(1)$

- `construct() -> int`  
与えられた `insert` と `erase` の操作をセグメント木上に構築する。`insert` と `erase` を行った回数を $r$ 回とすると、計算量 $O(r \log q)$

- `run() -> List[bool]`  
`construct` したクエリを実行し、その結果を返す。計算量 $O(q + r\log q\log n)$
