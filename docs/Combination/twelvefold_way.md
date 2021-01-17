---
title: 写像12相
documentation_of: //Combination/twelvefold_way.py
---
## 概要
ボールを箱に入れるときの場合の数を考える。このとき、ボールの区別 / 箱の区別 / 入れ方の制約 によって12パターンの数え方が存在する。

| ボール | 箱 | 入れ方に制約なし | 箱の中身は１個以下 | 箱の中身は１個以上 |
|----|----|:----:|:----:|:----:|
| 区別できる | 区別できる | `way1` | `way2` | `way3` |
| 区別できない | 区別できる | `way4` | `way5` | `way6` |
| 区別できる | 区別できない | `way7` | `way8` | `way9` |
| 区別できない | 区別できない | `way10` | `way11` | `way12` |

上図は [AOJ Balls and Boxes 1](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_A&lang=ja) からの出典

## 使い方
`way1(ball: int, box: int) -> int`  
ボールの個数 `ball` と箱の個数 `box` に対して、`way1` での場合の数を返す。

`way2` から `way12` まで同様の方法で使うことができる。ただし、コンテスト中にそのままペタリすることはあまりなく、数え上げ問題で状況整理したいときの確認で使うことが大半かも。
