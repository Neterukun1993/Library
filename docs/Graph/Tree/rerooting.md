---
title: 全方位木DP (Re-Rooting)
documentation_of: //Graph/Tree/rerooting.py
---

## 使い方
`rerooting(n, edges, unit, merge, addnode) -> List[Any]`  
- `n` 頂点の木（もしくは森）に対して、頂点属性の全方位木DPを行った結果を返す。辺は隣接リストとして `edges` で渡す。計算量 $O(n)$

- `merge` 関数は子の部分木同士の演算を表し、`unit` は演算の単位元である。これはモノイドとなる。

- `addnode` 関数は子の部分木と自身との演算を表す。  
<img src="https://Neterukun1993.github.io/Library/rerooting.png" width="400">

- 辺属性の全方位木DPをしたい場合は、あらかじめ [辺情報を頂点情報へと変換](https://neterukun1993.github.io/Library/Graph/misc/edge_to_vertex.py) しておけばよい。

## 参考
[【全方位木DP】明日使える便利な木構造のアルゴリズム](https://qiita.com/keymoon/items/2a52f1b0fb7ef67fb89e)
