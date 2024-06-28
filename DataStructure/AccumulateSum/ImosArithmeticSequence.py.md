---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class ImosArithmeticSequence:\n    def __init__(self, n):\n        self.n\
    \ = n\n        self.imos0 = [0] * (self.n + 1)\n        self.imos1 = [0] * (self.n\
    \ + 1)\n\n    def __getitem__(self, i):\n        return self.imos0[i] + self.imos1[i]\
    \ * i\n\n    def add(self, l, r, a, d):\n        self.imos0[l] += a\n        self.imos0[r]\
    \ -= a\n        self.imos0[l] -= d * l\n        self.imos0[r] += d * l\n     \
    \   self.imos1[l] += d\n        self.imos1[r] -= d\n\n    def build(self):\n \
    \       for i in range(self.n):\n            self.imos0[i + 1] += self.imos0[i]\n\
    \            self.imos1[i + 1] += self.imos1[i]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/AccumulateSum/ImosArithmeticSequence.py
  requiredBy: []
  timestamp: '2022-09-11 12:52:50+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/AccumulateSum/ImosArithmeticSequence.py
layout: document
title: "\u3044\u3082\u3059\u6CD5 (\u7B49\u5DEE\u6570\u5217\u52A0\u7B97)"
---

## 使い方
`ImosImosArithmeticSequence(n: int)`  
大きさ $n$ のいもす法用の配列を初期構築する。計算量 $O(n)$  
その後の一連の処理としては

1. `add` 関数で等差数列加算の準備をする。
2. `build` 関数で等差数列加算を実行する。
3. `__getitem__` 関数で値を取得する。

となる。

- `add(l: int, r: int, a: int, d: int) -> None`  
区間 $[l, r)$ に対して $a, a + d, a + 2 * d, \dots , a + d * (r - l + 1)$ を足す準備をする。計算量 $O(1)$

- `build() -> None`  
`add` による等差数列加算を実行する。計算量 $O(n)$

- `__getitem__(i: int) -> int`  
$i$ 番目の要素を返す。計算量 $O(1)$
