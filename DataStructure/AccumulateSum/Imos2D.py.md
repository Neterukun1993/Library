---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_5_B.test.py
    title: TestCase/AOJ/DSL_5_B.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Imos2D:\n    def __init__(self, h, w):\n        self.h = h\n      \
    \  self.w = w\n        self.imos = [[0] * (self.w + 1) for _ in range(self.h +\
    \ 1)]\n\n    def __getitem__(self, i):\n        return self.imos[i]\n\n    def\
    \ add(self, hl, hr, wl, wr, val):\n        \"\"\"add value in range [hl, hr) *\
    \ [wl, wr)\"\"\"\n        self.imos[hl][wl] += val\n        self.imos[hr][wl]\
    \ -= val\n        self.imos[hl][wr] -= val\n        self.imos[hr][wr] += val\n\
    \n    def build(self):\n        for i in range(self.h):\n            for j in\
    \ range(self.w):\n                self.imos[i][j + 1] += self.imos[i][j]\n   \
    \     for i in range(self.h):\n            for j in range(self.w):\n         \
    \       self.imos[i + 1][j] += self.imos[i][j]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/AccumulateSum/Imos2D.py
  requiredBy: []
  timestamp: '2021-02-13 17:23:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_5_B.test.py
documentation_of: DataStructure/AccumulateSum/Imos2D.py
layout: document
title: "\u4E8C\u6B21\u5143\u3044\u3082\u3059\u6CD5"
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
