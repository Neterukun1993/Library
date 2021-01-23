---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure\Wavelet\PointAddRectangleSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u77E9\u5F62\u548C\u53D6\u5F97"
  - icon: ':heavy_check_mark:'
    path: DataStructure\Wavelet\RectangleSum.py
    title: "\u77E9\u5F62\u548C\u53D6\u5F97"
  - icon: ':heavy_check_mark:'
    path: DataStructure\Wavelet\WaveletMatrix.py
    title: "\u30A6\u30A7\u30FC\u30D6\u30EC\u30C3\u30C8\u884C\u5217"
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BitVector:\r\n    def __init__(self, size):\r\n        # self.BLOCK_WIDTH\
    \ = 32\r\n        self.BLOCK_NUM = (size + 31) >> 5\r\n        self.bit = [0]\
    \ * self.BLOCK_NUM\r\n        self.count = [0] * self.BLOCK_NUM\r\n\r\n    def\
    \ set(self, i):\r\n        self.bit[i >> 5] |= 1 << (i & 31)\r\n\r\n    def build(self):\r\
    \n        for i in range(self.BLOCK_NUM - 1):\r\n            self.count[i + 1]\
    \ = self.count[i] + self.popcount(self.bit[i])\r\n\r\n    def popcount(self, x):\r\
    \n        x = x - ((x >> 1) & 0x55555555)\r\n        x = (x & 0x33333333) + ((x\
    \ >> 2) & 0x33333333)\r\n        x = (x + (x >> 4)) & 0x0F0F0F0F\r\n        x\
    \ = x + (x >> 8)\r\n        x = x + (x >> 16)\r\n        return x & 0x0000007F\r\
    \n\r\n    def access(self, i):\r\n        return (self.bit[i >> 5] >> (i & 31))\
    \ & 1\r\n\r\n    def rank(self, r, f):\r\n        res = self.count[r >> 5] + self.popcount(self.bit[r\
    \ >> 5] & ((1 << (r & 31)) - 1))\r\n        return res if f else r - res\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\Wavelet\BitVector.py
  requiredBy:
  - DataStructure\Wavelet\PointAddRectangleSum.py
  - DataStructure\Wavelet\RectangleSum.py
  - DataStructure\Wavelet\WaveletMatrix.py
  timestamp: '2021-01-10 20:36:04+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure\Wavelet\BitVector.py
layout: document
title: "\u30D3\u30C3\u30C8\u30D9\u30AF\u30C8\u30EB"
---
