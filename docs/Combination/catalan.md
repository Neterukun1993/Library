---
title: カタラン数
documentation_of: //Combination/catalan.py
---
## 概要

### カタラン数 (Catalan number)
カタラン数とは、様々な数え上げに現れる数列である。$n$ 番目のカタラン数の一般項は、以下の通りとなる。

$$C_n=\frac{1}{n+1}\binom{2n}{n}$$

数え上げにおいて、次のような意味付けがなされる。
- 対角線を跨がないグリッド上の最短経路
- 括弧列
- 多角形の三角形分割

### カタランの三角形 (Catalan's triangle)
カタランの三角形とは、カタラン数の一般化である。$C(n, k)$ は、$n$ 個の X と $k$ 個 Y を一列に並べたとき、全ての接頭辞について Y の個数が X の個数を超えないような、並べ方の場合の数である。一般項は、以下の通りとなる。

$$C(n, k)=\frac{n-k+1}{n+1}\binom{n+k}{n}$$

$n = k$ のとき、$C(n, n) = C_n$ となる。

### カタランの台形 (Catalan's trapezoid)
カタランの台形は、カタランの三角形の一般化である。$C_m(n, k)$ は、
$n$ 個の X と $k$ 個の Y の数を一列に並べたとき、全ての接頭辞について Y の個数が X の個数を $m - 1$ 以上超えないような、並べ方の場合の数である。一般項は、以下の通りとなる。

$m = 1$ のとき、$C_1(n, k) = C(n, k)$ となる。

## 備考
カタラン数 (グリッド上の最短経路数)

<img src="https://Neterukun1993.github.io/Library/catalan_number.png" width="400">

カタランの台形 (グリッド上の最短経路数)

<img src="https://Neterukun1993.github.io/Library/catalan_trapezoid.png" width="400">

## 使い方
`catalan(n: int) -> int`  
$n$ 番目のカタラン数を返す。計算量 $O(1)$

`catalan_trapezoid(n: int, k: int, m: int = 1) -> int`  
$C_m(n, k)$ を返す。計算量 $O(1)$
