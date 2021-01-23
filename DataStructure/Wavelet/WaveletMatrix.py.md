---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: DataStructure\Wavelet\BitVector.py
    title: "\u30D3\u30C3\u30C8\u30D9\u30AF\u30C8\u30EB"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\1549.test.py
    title: TestCase\AOJ\1549.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\range_kth_smallest.CompressedWaveletMatrix.test.py
    title: TestCase\LibraryChecker\range_kth_smallest.CompressedWaveletMatrix.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\LibraryChecker\range_kth_smallest.WaveletMatrix.test.py
    title: TestCase\LibraryChecker\range_kth_smallest.WaveletMatrix.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.Wavelet.BitVector import BitVector\r\nfrom bisect import\
    \ bisect_left\r\n\r\n\r\nclass WaveletMatrix:\r\n    def __init__(self, array,\
    \ MAXLOG=32):\r\n        self.MAXLOG = MAXLOG\r\n        self.n = len(array)\r\
    \n        self.mat = []\r\n        self.mid = []\r\n\r\n        for d in reversed(range(self.MAXLOG)):\r\
    \n            vec = BitVector(self.n + 1)\r\n            ls = []\r\n         \
    \   rs = []\r\n            for i, val in enumerate(array):\r\n               \
    \ if (val >> d) & 1:\r\n                    rs.append(val)\r\n               \
    \     vec.set(i)\r\n                else:\r\n                    ls.append(val)\r\
    \n            vec.build()\r\n            self.mat.append(vec)\r\n            self.mid.append(len(ls))\r\
    \n            array = ls + rs\r\n\r\n    def access(self, i):\r\n        res =\
    \ 0\r\n        for d in range(self.MAXLOG):\r\n            res <<= 1\r\n     \
    \       if self.mat[d][i]:\r\n                res |= 1\r\n                i =\
    \ self.mat[d].rank(i, 1) + self.mid[d]\r\n            else:\r\n              \
    \  i = self.mat[d].rank(i, 0)\r\n        return res\r\n\r\n    def rank(self,\
    \ l, r, val):\r\n        for d in range(self.MAXLOG):\r\n            if val >>\
    \ (self.MAXLOG - d - 1) & 1:\r\n                l = self.mat[d].rank(l, 1) + self.mid[d]\r\
    \n                r = self.mat[d].rank(r, 1) + self.mid[d]\r\n            else:\r\
    \n                l = self.mat[d].rank(l, 0)\r\n                r = self.mat[d].rank(r,\
    \ 0)\r\n        return r - l\r\n\r\n    def quantile(self, l, r, k):\r\n     \
    \   res = 0\r\n        for d in range(self.MAXLOG):\r\n            res <<= 1\r\
    \n            cntl, cntr = self.mat[d].rank(l, 0), self.mat[d].rank(r, 0)\r\n\
    \            if k >= cntr - cntl:\r\n                l = self.mat[d].rank(l, 1)\
    \ + self.mid[d]\r\n                r = self.mat[d].rank(r, 1) + self.mid[d]\r\n\
    \                res |= 1\r\n                k -= cntr - cntl\r\n            else:\r\
    \n                l = cntl\r\n                r = cntr\r\n        return res\r\
    \n\r\n    def kth_smallest(self, l, r, k):\r\n        return self.quantile(l,\
    \ r, k)\r\n\r\n    def kth_largest(self, l, r, k):\r\n        return self.quantile(l,\
    \ r, r - l - k - 1)\r\n\r\n    def range_freq(self, l, r, upper):\r\n        res\
    \ = 0\r\n        for d in range(self.MAXLOG):\r\n            if upper >> (self.MAXLOG\
    \ - d - 1) & 1:\r\n                res += self.mat[d].rank(r, 0) - self.mat[d].rank(l,\
    \ 0)\r\n                l = self.mat[d].rank(l, 1) + self.mid[d]\r\n         \
    \       r = self.mat[d].rank(r, 1) + self.mid[d]\r\n            else:\r\n    \
    \            l = self.mat[d].rank(l, 0)\r\n                r = self.mat[d].rank(r,\
    \ 0)\r\n        return res\r\n\r\n    def prev_val(self, l, r, upper):\r\n   \
    \     cnt = self.range_freq(l, r, upper)\r\n        return None if cnt == 0 else\
    \ self.kth_smallest(l, r, cnt - 1)\r\n\r\n    def next_val(self, l, r, lower):\r\
    \n        cnt = self.range_freq(l, r, lower)\r\n        return None if cnt ==\
    \ r - l else self.kth_smallest(l, r, cnt)\r\n\r\n\r\nclass CompressedWaveletMatrix:\r\
    \n    def __init__(self, array):\r\n        self.vals = sorted(set(array))\r\n\
    \        self.comp = {val: idx for idx, val in enumerate(self.vals)}\r\n     \
    \   array = [self.comp[val] for val in array]\r\n        MAXLOG = len(self.vals).bit_length()\r\
    \n        self.wm = WaveletMatrix(array, MAXLOG)\r\n\r\n    def access(self, i):\r\
    \n        return self.vals[self.wm.access(i)]\r\n\r\n    def rank(self, l, r,\
    \ val):\r\n        return self.wm.rank(l, r, self.comp[val]) if val in self.comp\
    \ else 0\r\n\r\n    def kth_smallest(self, l, r, k):\r\n        return self.vals[self.wm.kth_smallest(l,\
    \ r, k)]\r\n\r\n    def kth_largest(self, l, r, k):\r\n        return self.vals[self.wm.kth_largest(l,\
    \ r, k)]\r\n\r\n    def range_freq(self, l, r, upper):\r\n        upper = bisect_left(self.vals,\
    \ upper)\r\n        return self.wm.range_freq(l, r, upper)\r\n\r\n    def prev_val(self,\
    \ l, r, upper):\r\n        upper = bisect_left(self.vals, upper)\r\n        res\
    \ = self.wm.prev_val(l, r, upper)\r\n        return None if res is None else self.vals[res]\r\
    \n\r\n    def next_val(self, l, r, lower):\r\n        lower = bisect_left(self.vals,\
    \ lower)\r\n        res = self.wm.next_val(l, r, lower)\r\n        return None\
    \ if res is None else self.vals[res]\r\n"
  dependsOn:
  - DataStructure\Wavelet\BitVector.py
  isVerificationFile: false
  path: DataStructure\Wavelet\WaveletMatrix.py
  requiredBy: []
  timestamp: '2021-01-10 20:36:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\1549.test.py
  - TestCase\LibraryChecker\range_kth_smallest.CompressedWaveletMatrix.test.py
  - TestCase\LibraryChecker\range_kth_smallest.WaveletMatrix.test.py
documentation_of: DataStructure\Wavelet\WaveletMatrix.py
layout: document
title: "\u30A6\u30A7\u30FC\u30D6\u30EC\u30C3\u30C8\u884C\u5217"
---
