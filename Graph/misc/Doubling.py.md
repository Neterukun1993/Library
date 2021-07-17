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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class Doubling:\n    def __init__(self, permutation, power=64):\n       \
    \ self.n = len(permutation)\n        self.perm = permutation\n        self.power\
    \ = power\n        self._build()\n\n    def _build(self):\n        self.next =\
    \ [[0] * self.n for i in range(self.power)]\n        for v in range(self.n):\n\
    \            self.next[0][v] = self.perm[v]\n        for k in range(self.power\
    \ - 1):\n            for v in range(self.n):\n                self.next[k + 1][v]\
    \ = self.next[k][self.next[k][v]]\n\n    def dest(self, v, times):\n        for\
    \ k in range(self.power):\n            if (times >> k) & 1:\n                v\
    \ = self.next[k][v]\n        return v\n\n    def build_path(self, values, op=max,\
    \ e=-10**18):\n        self.op = op\n        self.e = e\n        self.data = [[e]\
    \ * self.n for i in range(self.power)]\n        for v in range(self.n):\n    \
    \        self.data[0][v] = self.op(self.e, values[v])\n        for k in range(self.power\
    \ - 1):\n            for v in range(self.n):\n                self.data[k + 1][v]\
    \ = self.op(self.data[k][v],\n                                              self.data[k][self.next[k][v]])\n\
    \n    def fold(self, v, times):\n        res = self.e\n        for k in range(self.power):\n\
    \            if (times >> k) & 1:\n                res = self.op(res, self.data[k][v])\n\
    \                v = self.next[k][v]\n        return res\n\n    def max_times(self,\
    \ v, f):\n        res = self.e\n        times = 0\n        for k in reversed(range(self.power)):\n\
    \            if f(self.op(res, self.data[k][v])):\n                res = self.op(res,\
    \ self.data[k][v])\n                times += 1 << k\n                v = self.next[k][v]\n\
    \        return times\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/misc/Doubling.py
  requiredBy: []
  timestamp: '2021-06-04 23:50:40+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: Graph/misc/Doubling.py
layout: document
title: "functional graph \u4E0A\u306E (\u9806\u5217\u4E0A\u306E) \u30C0\u30D6\u30EA\
  \u30F3\u30B0"
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
