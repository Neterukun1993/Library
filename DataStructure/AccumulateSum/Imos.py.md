---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_5_A.test.py
    title: TestCase/AOJ/DSL_5_A.test.py
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
  code: "class Imos:\n    def __init__(self, n):\n        self.n = n\n        self.imos\
    \ = [0] * (self.n + 1)\n\n    def __getitem__(self, i):\n        return self.imos[i]\n\
    \n    def add(self, l, r, val):\n        \"\"\"add value in range [l, r)\"\"\"\
    \n        self.imos[r] -= val\n        self.imos[l] += val\n\n    def build(self):\n\
    \        for i in range(self.n):\n            self.imos[i + 1] += self.imos[i]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/AccumulateSum/Imos.py
  requiredBy: []
  timestamp: '2021-01-02 06:20:11+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DSL_5_A.test.py
documentation_of: DataStructure/AccumulateSum/Imos.py
layout: document
title: "\u3044\u3082\u3059\u6CD5"
---

## 使い方
`Imos(n: int)`  
大きさ $n$ のいもす法用の配列を初期構築する。計算量 $O(n)$  
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

## 参考
[いもす法 - いもす研 (imos laboratory)](https://imoz.jp/algorithms/imos_method.html)
