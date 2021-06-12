---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure/Wavelet/PointAddRectangleSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u77E9\u5F62\u548C\u53D6\u5F97"
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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BitVector:\n    def __init__(self, size):\n        # self.BLOCK_WIDTH\
    \ = 32\n        self.BLOCK_NUM = (size + 31) >> 5\n        self.bit = [0] * self.BLOCK_NUM\n\
    \        self.count = [0] * self.BLOCK_NUM\n\n    def set(self, i):\n        self.bit[i\
    \ >> 5] |= 1 << (i & 31)\n\n    def build(self):\n        for i in range(self.BLOCK_NUM\
    \ - 1):\n            self.count[i + 1] = self.count[i] + self.popcount(self.bit[i])\n\
    \n    def popcount(self, x):\n        x = x - ((x >> 1) & 0x55555555)\n      \
    \  x = (x & 0x33333333) + ((x >> 2) & 0x33333333)\n        x = (x + (x >> 4))\
    \ & 0x0F0F0F0F\n        x = x + (x >> 8)\n        x = x + (x >> 16)\n        return\
    \ x & 0x0000007F\n\n    def access(self, i):\n        return (self.bit[i >> 5]\
    \ >> (i & 31)) & 1\n\n    def rank(self, r, f):\n        res = self.count[r >>\
    \ 5] + self.popcount(self.bit[r >> 5] & ((1 << (r & 31)) - 1))\n        return\
    \ res if f else r - res\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/Wavelet/BitVector.py
  requiredBy:
  - DataStructure/Wavelet/WaveletMatrix.py
  - DataStructure/Wavelet/PointAddRectangleSum.py
  - DataStructure/Wavelet/RectangleSum.py
  timestamp: '2021-01-10 20:36:04+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/Wavelet/BitVector.py
layout: document
title: "\u30D3\u30C3\u30C8\u30D9\u30AF\u30C8\u30EB"
---
