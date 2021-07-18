---
title: 三分探索
documentation_of: //misc/ternary_search.py
---

## 使い方
`ternary_search_max(l: float, r: float, evaluate: Callable[[float], T]) -> Tuple[float, T]`  
$l \le x \lt r$ を満たす実数 $x$ について、上に凸な関数 `evaluate(x)` が最大値となる $x$ とその最大値を返す。計算量 $O(\log(r - l))$

`ternary_search_min(l: float, r: float, evaluate: Callable[[float], Any]) -> Tuple[float, Any]`  
$l \le x \lt r$ を満たす実数 $x$ について、下に凸な関数 `evaluate(x)` が最小値となる $x$ とその最小値を返す。計算量 $O(\log(r - l))$

`ternary_search_intmax(l: int, r: int, evaluate: Callable[[int], Any]) -> Tuple[int, Any]`  
$l \le x \lt r$ を満たす整数 $x$ について、上に凸な関数 `evaluate(x)` が最大値となる $x$ とその最大値を返す。計算量 $O(\log(r - l))$

`ternary_search_intmin(l: int, r: int, evaluate: Callable[[float], Any]) -> Tuple[float, Any]`  
$l \le x \lt r$ を満たす整数 $x$ について、下に凸な関数 `evaluate(x)` が最小値となる $x$ とその最小値を返す。計算量 $O(\log(r - l))$

## 注意
- 誤差に気をつける。[No.306 さいたま2008 - yukicoder](https://yukicoder.me/problems/no/306)

- 関数に平坦な箇所があると、三分探索が正しく行えない場合がある（コードのコメントを参照）。
