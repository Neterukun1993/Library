---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure/Wavelet/PointAddRectangleSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u77E9\u5F62\u548C\u53D6\u5F97"
  - icon: ':warning:'
    path: DataStructure/Wavelet/RangeSetQuery.py
    title: "\u7A2E\u985E\u6570\u53D6\u5F97"
  - icon: ':heavy_check_mark:'
    path: DataStructure/Wavelet/RectangleSum.py
    title: "\u77E9\u5F62\u548C\u53D6\u5F97"
  - icon: ':heavy_check_mark:'
    path: DataStructure/Wavelet/WaveletMatrix.py
    title: "\u30A6\u30A7\u30FC\u30D6\u30EC\u30C3\u30C8\u884C\u5217"
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BitVector:\n    def __init__(self, n):\n        # self.BLOCK_WIDTH\
    \ = 32\n        self.BLOCK_NUM = (n + 31) >> 5\n        self.bit = [0] * self.BLOCK_NUM\n\
    \        self.count = [0] * self.BLOCK_NUM\n\n    def _popcount(self, x):\n  \
    \      x = x - ((x >> 1) & 0x55555555)\n        x = (x & 0x33333333) + ((x >>\
    \ 2) & 0x33333333)\n        x = (x + (x >> 4)) & 0x0F0F0F0F\n        x = x + (x\
    \ >> 8)\n        x = x + (x >> 16)\n        return x & 0x0000007F\n\n    def set(self,\
    \ i):\n        self.bit[i >> 5] |= 1 << (i & 31)\n\n    def access(self, i):\n\
    \        return (self.bit[i >> 5] >> (i & 31)) & 1\n\n    def build(self):\n \
    \       for i in range(self.BLOCK_NUM - 1):\n            self.count[i + 1] = self.count[i]\
    \ + self._popcount(self.bit[i])\n\n    def rank(self, r, f):\n        res = self.count[r\
    \ >> 5] + self._popcount(self.bit[r >> 5] & ((1 << (r & 31)) - 1))\n        return\
    \ res if f else r - res\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/Wavelet/BitVector.py
  requiredBy:
  - DataStructure/Wavelet/WaveletMatrix.py
  - DataStructure/Wavelet/PointAddRectangleSum.py
  - DataStructure/Wavelet/RangeSetQuery.py
  - DataStructure/Wavelet/RectangleSum.py
  timestamp: '2022-08-07 15:04:38+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/Wavelet/BitVector.py
layout: document
title: "\u30D3\u30C3\u30C8\u30D9\u30AF\u30C8\u30EB"
---
## 概要
各要素が $0$ もしくは $1$ に限定される配列の構築を $O(n)$、区間和を $O(1)$ で行えるデータ構造。通常の累積和よりも省メモリである。

## 使い方
`BitVector(n: int)`  
長さが $n$ で全要素が $0$ であるビットベクトルを構築する。計算量 $O(n)$

- `set(i: int) -> None`  
$i$ 番目の要素を $1$ に更新する。計算量 $O(1)$

- `access(i) -> int`  
$i$ 番目の値を返す。計算量 $O(1)$

- `build() -> None`  
ビットベクトルに対する累積和を構築する。計算量 $O(n)$

- `rank(r: int, f: bool) -> int`  
$[0, r)$ 番目について、`f = True` のとき $1$ の個数を、`f = False` のとき $0$ の個数を返す。計算量 $O(1)$