---
title: MOD上での組合せ計算
documentation_of: //Combination/modinv_combination.py
---
## 使い方
`Combination(n: int, MOD: int)`  
`MOD` 上での $k!$ とその逆元を、`n` 以下の自然数 $k$ に対して前計算する。計算量 $O(n + \log(\mathrm{MOD}))$

- `inv(k: int) -> int`  
$k$ の逆元を返す。計算量 $O(1)$

- `fact(k: int) -> int`  
$k!$ を返す。計算量 $O(1)$

- `inv_fact(k: int) -> int`  
$k!$ の逆元を返す。計算量 $O(1)$

- `perm(k: int, r: int) -> int`  
${}_k\mathrm{P}_r$ を返す。計算量 $O(1)$

- `comb(k: int, r: int) -> int`  
${}_k\mathrm{C}_r$ を返す。計算量 $O(1)$

`combination(k: int, r: int, MOD: int) -> int`  
`MOD` 上での ${}_k\mathrm{C}_r$ をナイーブに計算して返す。計算量 $O(\min(r, k - r))$
