---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: DataStructure/Wavelet/BitVector.py
    title: "\u30D3\u30C3\u30C8\u30D9\u30AF\u30C8\u30EB"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/1549.test.py
    title: TestCase/AOJ/1549.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/range_kth_smallest.CompressedWaveletMatrix.test.py
    title: TestCase/LibraryChecker/range_kth_smallest.CompressedWaveletMatrix.test.py
  - icon: ':x:'
    path: TestCase/LibraryChecker/range_kth_smallest.WaveletMatrix.test.py
    title: TestCase/LibraryChecker/range_kth_smallest.WaveletMatrix.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':question:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.Wavelet.BitVector import BitVector\nfrom bisect import\
    \ bisect_left\n\n\nclass WaveletMatrix:\n    def __init__(self, array, MAXLOG=32):\n\
    \        self.MAXLOG = MAXLOG\n        self.n = len(array)\n        self.mat =\
    \ []\n        self.mid = []\n\n        for d in reversed(range(self.MAXLOG)):\n\
    \            vec = BitVector(self.n + 1)\n            ls = []\n            rs\
    \ = []\n            for i, val in enumerate(array):\n                if (val >>\
    \ d) & 1:\n                    rs.append(val)\n                    vec.set(i)\n\
    \                else:\n                    ls.append(val)\n            vec.build()\n\
    \            self.mat.append(vec)\n            self.mid.append(len(ls))\n    \
    \        array = ls + rs\n\n    def access(self, i):\n        res = 0\n      \
    \  for d in range(self.MAXLOG):\n            res <<= 1\n            if self.mat[d][i]:\n\
    \                res |= 1\n                i = self.mat[d].rank(i, 1) + self.mid[d]\n\
    \            else:\n                i = self.mat[d].rank(i, 0)\n        return\
    \ res\n\n    def rank(self, l, r, val):\n        for d in range(self.MAXLOG):\n\
    \            if val >> (self.MAXLOG - d - 1) & 1:\n                l = self.mat[d].rank(l,\
    \ 1) + self.mid[d]\n                r = self.mat[d].rank(r, 1) + self.mid[d]\n\
    \            else:\n                l = self.mat[d].rank(l, 0)\n             \
    \   r = self.mat[d].rank(r, 0)\n        return r - l\n\n    def quantile(self,\
    \ l, r, k):\n        res = 0\n        for d in range(self.MAXLOG):\n         \
    \   res <<= 1\n            cntl, cntr = self.mat[d].rank(l, 0), self.mat[d].rank(r,\
    \ 0)\n            if k >= cntr - cntl:\n                l = self.mat[d].rank(l,\
    \ 1) + self.mid[d]\n                r = self.mat[d].rank(r, 1) + self.mid[d]\n\
    \                res |= 1\n                k -= cntr - cntl\n            else:\n\
    \                l = cntl\n                r = cntr\n        return res\n\n  \
    \  def kth_smallest(self, l, r, k):\n        return self.quantile(l, r, k)\n\n\
    \    def kth_largest(self, l, r, k):\n        return self.quantile(l, r, r - l\
    \ - k - 1)\n\n    def range_freq(self, l, r, upper):\n        res = 0\n      \
    \  for d in range(self.MAXLOG):\n            if upper >> (self.MAXLOG - d - 1)\
    \ & 1:\n                res += self.mat[d].rank(r, 0) - self.mat[d].rank(l, 0)\n\
    \                l = self.mat[d].rank(l, 1) + self.mid[d]\n                r =\
    \ self.mat[d].rank(r, 1) + self.mid[d]\n            else:\n                l =\
    \ self.mat[d].rank(l, 0)\n                r = self.mat[d].rank(r, 0)\n       \
    \ return res\n\n    def prev_val(self, l, r, upper):\n        cnt = self.range_freq(l,\
    \ r, upper)\n        return None if cnt == 0 else self.kth_smallest(l, r, cnt\
    \ - 1)\n\n    def next_val(self, l, r, lower):\n        cnt = self.range_freq(l,\
    \ r, lower)\n        return None if cnt == r - l else self.kth_smallest(l, r,\
    \ cnt)\n\n\nclass CompressedWaveletMatrix:\n    def __init__(self, array):\n \
    \       self.vals = sorted(set(array))\n        self.comp = {val: idx for idx,\
    \ val in enumerate(self.vals)}\n        array = [self.comp[val] for val in array]\n\
    \        MAXLOG = len(self.vals).bit_length()\n        self.wm = WaveletMatrix(array,\
    \ MAXLOG)\n\n    def access(self, i):\n        return self.vals[self.wm.access(i)]\n\
    \n    def rank(self, l, r, val):\n        return self.wm.rank(l, r, self.comp[val])\
    \ if val in self.comp else 0\n\n    def kth_smallest(self, l, r, k):\n       \
    \ return self.vals[self.wm.kth_smallest(l, r, k)]\n\n    def kth_largest(self,\
    \ l, r, k):\n        return self.vals[self.wm.kth_largest(l, r, k)]\n\n    def\
    \ range_freq(self, l, r, upper):\n        upper = bisect_left(self.vals, upper)\n\
    \        return self.wm.range_freq(l, r, upper)\n\n    def prev_val(self, l, r,\
    \ upper):\n        upper = bisect_left(self.vals, upper)\n        res = self.wm.prev_val(l,\
    \ r, upper)\n        return None if res is None else self.vals[res]\n\n    def\
    \ next_val(self, l, r, lower):\n        lower = bisect_left(self.vals, lower)\n\
    \        res = self.wm.next_val(l, r, lower)\n        return None if res is None\
    \ else self.vals[res]\n"
  dependsOn:
  - DataStructure/Wavelet/BitVector.py
  isVerificationFile: false
  path: DataStructure/Wavelet/WaveletMatrix.py
  requiredBy: []
  timestamp: '2021-01-10 20:36:04+09:00'
  verificationStatus: LIBRARY_SOME_WA
  verifiedWith:
  - TestCase/AOJ/1549.test.py
  - TestCase/LibraryChecker/range_kth_smallest.CompressedWaveletMatrix.test.py
  - TestCase/LibraryChecker/range_kth_smallest.WaveletMatrix.test.py
documentation_of: DataStructure/Wavelet/WaveletMatrix.py
layout: document
title: "\u30A6\u30A7\u30FC\u30D6\u30EC\u30C3\u30C8\u884C\u5217"
---
