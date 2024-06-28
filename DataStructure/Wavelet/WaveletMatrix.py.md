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
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/range_kth_smallest.WaveletMatrix.test.py
    title: TestCase/LibraryChecker/range_kth_smallest.WaveletMatrix.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
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
  timestamp: '2022-08-07 15:04:38+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/1549.test.py
  - TestCase/LibraryChecker/range_kth_smallest.WaveletMatrix.test.py
  - TestCase/LibraryChecker/range_kth_smallest.CompressedWaveletMatrix.test.py
documentation_of: DataStructure/Wavelet/WaveletMatrix.py
layout: document
title: "\u30A6\u30A7\u30FC\u30D6\u30EC\u30C3\u30C8\u884C\u5217"
---
## 使い方
`CompressedWaveletMatrix(array: Sequence[int])`  
`array` から座標圧縮した Wavelet Matrix を構築する。計算量 $O(n \log n)$

- `access(i: int) -> int`  
`i` 番目 (0-indexed) の要素を返す。計算量 $O(\log n)$

- `rank(l: int, r: int, val: int) -> int`  
`array[l:r]` 内の `val` の個数を返す。計算量 $O(\log n)$

- `kth_smallest(l: int, r: int, k: int)`  
`array[l:r]` 内の `k` 番目 (0-indexed) に小さい要素を返す。計算量 $O(\log n)$

- `kth_largest(l: int, r: int, k: int)`  
`array[l:r]` 内の `k` 番目 (0-indexed) に大きい要素を返す。計算量 $O(\log n)$ 

- `range_freq(l: int, r: int, upper: int)`  
`array[l:r]` 内の `upper` よりも小さい要素の個数を返す。計算量 $O(\log n)$

- `prev_val(l: int, r: int, upper: int)`  
`array[l:r]` 内の `upper` よりも小さい最大の要素を返す。そのような要素が存在しない場合は `None` を返す。計算量 $O(\log n)$

- `next_val(l: int, r: int, lower: int) -> int`  
`array[l:r]` 内の `lower` 以上の最小の要素を返す。そのような要素が存在しない場合は `None` を返す。計算量 $O(\log n)$
