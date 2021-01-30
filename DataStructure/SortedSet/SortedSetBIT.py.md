---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure/SortedSet/SortedMultiSetBIT.py
    title: DataStructure/SortedSet/SortedMultiSetBIT.py
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from bisect import bisect_left\n\n\nclass SortedSetBIT:\n    def __init__(self,\
    \ cands):\n        self.array = sorted(set(cands))\n        self.comp = {val:\
    \ i for i, val in enumerate(self.array)}\n        self.size = len(self.array)\n\
    \        self.cnt = 0\n        self.bit = [0] * (self.size + 1)\n\n    def __contains__(self,\
    \ val):\n        return self.count(val, val + 1) > 0\n\n    def __len__(self):\n\
    \        return self.cnt\n\n    def _count(self, i):\n        res = 0\n      \
    \  while i > 0:\n            res += self.bit[i]\n            i -= i & -i\n   \
    \     return res\n\n    def add(self, val):\n        if val in self:\n       \
    \     return False\n        i = self.comp[val] + 1\n        while i <= self.size:\n\
    \            self.bit[i] += 1\n            i += i & -i\n        self.cnt += 1\n\
    \        return True\n\n    def remove(self, val):\n        if val not in self:\n\
    \            return False\n        i = self.comp[val] + 1\n        while i <=\
    \ self.size:\n            self.bit[i] -= 1\n            i += i & -i\n        self.cnt\
    \ -= 1\n        return True\n\n    def count(self, vl, vr):\n        l = bisect_left(self.array,\
    \ vl)\n        r = bisect_left(self.array, vr)\n        return self._count(r)\
    \ - self._count(l)\n\n    def kth_smallest(self, k):\n        if not(0 <= k <\
    \ self.cnt):\n            raise IndexError\n        idx = 0\n        k += 1\n\
    \        d = 1 << self.size.bit_length()\n        while d:\n            if idx\
    \ + d <= self.size and self.bit[idx + d] < k:\n                k -= self.bit[idx\
    \ + d]\n                idx += d\n            d >>= 1\n        return self.array[idx]\n\
    \n    def kth_largest(self, k):\n        return self.kth_smallest(self.cnt - k\
    \ - 1)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SortedSet/SortedSetBIT.py
  requiredBy:
  - DataStructure/SortedSet/SortedMultiSetBIT.py
  timestamp: '2021-01-30 18:34:52+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/SortedSet/SortedSetBIT.py
layout: document
redirect_from:
- /library/DataStructure/SortedSet/SortedSetBIT.py
- /library/DataStructure/SortedSet/SortedSetBIT.py.html
title: DataStructure/SortedSet/SortedSetBIT.py
---
