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
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SegmentTreeBeats:\r\n    def __init__(self, n, INF=10**18):\r\n   \
    \     self.MAX = INF\r\n        self.MIN = -INF\r\n        self.size = 1 << (n\
    \ - 1).bit_length()\r\n        sz = self.size * 2 - 1\r\n        self.sum_ = [0]\
    \ * sz\r\n        self.max_v = [self.MIN] * sz\r\n        self.min_v = [self.MAX]\
    \ * sz\r\n        self.max_c = [1] * sz\r\n        self.min_c = [1] * sz\r\n \
    \       self.smax_v = [self.MIN] * sz\r\n        self.smin_v = [self.MAX] * sz\r\
    \n        self.lz_add = [0] * sz\r\n\r\n    def build(self, array):\r\n      \
    \  for i, val in enumerate(array, self.size - 1):\r\n            self.sum_[i]\
    \ = self.min_v[i] = self.max_v[i] = val\r\n        for i in range(self.size -\
    \ 2, -1, -1):\r\n            self.update(i)\r\n\r\n    def update(self, i):\r\n\
    \        if i >= self.size - 1: return\r\n        i1, i2 = i * 2 + 1, i * 2 +\
    \ 2\r\n        self.sum_[i] = self.sum_[i1] + self.sum_[i2]\r\n        self.max_v[i]\
    \ = max(self.max_v[i1], self.max_v[i2])\r\n        if self.max_v[i1] > self.max_v[i2]:\r\
    \n            self.max_c[i] = self.max_c[i1]\r\n            self.smax_v[i] = max(self.smax_v[i1],\
    \ self.max_v[i2])\r\n        elif self.max_v[i1] < self.max_v[i2]:\r\n       \
    \     self.max_c[i] = self.max_c[i2]\r\n            self.smax_v[i] = max(self.max_v[i1],\
    \ self.smax_v[i2])\r\n        else:\r\n            self.max_c[i] = self.max_c[i1]\
    \ + self.max_c[i2]\r\n            self.smax_v[i] = max(self.smax_v[i1], self.smax_v[i2])\r\
    \n\r\n        self.min_v[i] = min(self.min_v[i1], self.min_v[i2])\r\n        if\
    \ self.min_v[i1] < self.min_v[i2]:\r\n            self.min_c[i] = self.min_c[i1]\r\
    \n            self.smin_v[i] = min(self.smin_v[i1], self.min_v[i2])\r\n      \
    \  elif self.min_v[i1] > self.min_v[i2]:\r\n            self.min_c[i] = self.min_c[i2]\r\
    \n            self.smin_v[i] = min(self.min_v[i1], self.smin_v[i2])\r\n      \
    \  else:\r\n            self.min_c[i] = self.min_c[i1] + self.min_c[i2]\r\n  \
    \          self.smin_v[i] = min(self.smin_v[i1], self.smin_v[i2])\r\n\r\n    def\
    \ push(self, i, l, r):\r\n        i1, i2 = i * 2 + 1, i * 2 + 2\r\n        if\
    \ self.lz_add[i] != 0:\r\n            self.sum_[i] += self.lz_add[i] * (r - l)\r\
    \n            self.min_v[i] += self.lz_add[i]\r\n            self.smin_v[i] +=\
    \ self.lz_add[i]\r\n            self.max_v[i] += self.lz_add[i]\r\n          \
    \  self.smax_v[i] += self.lz_add[i]\r\n            if i < self.size - 1:\r\n \
    \               self.lz_add[i1] += self.lz_add[i]\r\n                self.lz_add[i2]\
    \ += self.lz_add[i]\r\n            self.lz_add[i] = 0\r\n        if i < self.size\
    \ - 1:\r\n            if self.max_v[i] < self.max_v[i1] + self.lz_add[i1]:\r\n\
    \                self.chmin_at(i1, self.max_v[i] - self.lz_add[i1], l, (l + r)\
    \ // 2)\r\n            if self.max_v[i] < self.max_v[i2] + self.lz_add[i2]:\r\n\
    \                self.chmin_at(i2, self.max_v[i] - self.lz_add[i2], (l + r) //\
    \ 2, r)\r\n            if self.min_v[i] > self.min_v[i1] + self.lz_add[i1]:\r\n\
    \                self.chmax_at(i1, self.min_v[i] - self.lz_add[i1], l, (l + r)\
    \ // 2)\r\n            if self.min_v[i] > self.min_v[i2] + self.lz_add[i2]:\r\n\
    \                self.chmax_at(i2, self.min_v[i] - self.lz_add[i2], (l + r) //\
    \ 2, r)\r\n\r\n    def chmin_at(self, i, x, l, r):\r\n        if self.max_v[i]\
    \ == self.min_v[i]:\r\n            self.sum_[i] = x * (r - l)\r\n            self.max_v[i]\
    \ = self.min_v[i] = x\r\n        elif self.max_v[i] == self.smin_v[i]:\r\n   \
    \         self.sum_[i] += (x - self.max_v[i]) * self.max_c[i]\r\n            self.max_v[i]\
    \ = self.smin_v[i] = x\r\n        else:\r\n            self.sum_[i] += (x - self.max_v[i])\
    \ * self.max_c[i]\r\n            self.max_v[i] = x\r\n\r\n    def chmax_at(self,\
    \ i, x, l, r):\r\n        if self.max_v[i] == self.min_v[i]:\r\n            self.sum_[i]\
    \ = x * (r - l)\r\n            self.max_v[i] = self.min_v[i] = x\r\n        elif\
    \ self.min_v[i] == self.smax_v[i]:\r\n            self.sum_[i] += (x - self.min_v[i])\
    \ * self.min_c[i]\r\n            self.min_v[i] = self.smax_v[i] = x\r\n      \
    \  else:\r\n            self.sum_[i] += (x - self.min_v[i]) * self.min_c[i]\r\n\
    \            self.min_v[i] = x\r\n\r\n    def range_chmin(self, a, b, x, i=0,\
    \ l=0, r=-1):\r\n        if r == -1: r = self.size\r\n        self.push(i, l,\
    \ r)\r\n        if r <= a or b <= l or self.max_v[i] <= x: return\r\n        if\
    \ a <= l and r <= b and self.smax_v[i] < x:\r\n            self.chmin_at(i, x,\
    \ l, r)\r\n            self.push(i, l, r)\r\n            return\r\n        self.range_chmin(a,\
    \ b, x, i * 2 + 1, l, (l + r) // 2)\r\n        self.range_chmin(a, b, x, i * 2\
    \ + 2, (l + r) // 2, r)\r\n        self.update(i)\r\n\r\n    def range_chmax(self,\
    \ a, b, x, i=0, l=0, r=-1):\r\n        if r == -1: r = self.size\r\n        self.push(i,\
    \ l, r)\r\n        if r <= a or b <= l or self.min_v[i] >= x: return\r\n     \
    \   if a <= l and r <= b and self.smin_v[i] > x:\r\n            self.chmax_at(i,\
    \ x, l, r)\r\n            self.push(i, l, r)\r\n            return\r\n       \
    \ self.range_chmax(a, b, x, i * 2 + 1, l, (l + r) // 2)\r\n        self.range_chmax(a,\
    \ b, x, i * 2 + 2, (l + r) // 2, r)\r\n        self.update(i)\r\n\r\n    def range_add(self,\
    \ a, b, x, i=0, l=0, r=-1):\r\n        if r == -1: r = self.size\r\n        self.push(i,\
    \ l, r)\r\n        if r <= a or b <= l: return\r\n        if a <= l and r <= b:\r\
    \n            self.lz_add[i] += x\r\n            self.push(i, l, r)\r\n      \
    \      return\r\n        self.range_add(a, b, x, i * 2 + 1, l, (l + r) // 2)\r\
    \n        self.range_add(a, b, x, i * 2 + 2, (l + r) // 2, r)\r\n        self.update(i)\r\
    \n\r\n    def fold_min(self, a, b, i=0, l=0, r=-1):\r\n        if r == -1: r =\
    \ self.size\r\n        self.push(i, l, r)\r\n        if r <= a or b <= l: return\
    \ self.MAX\r\n        if a <= l and r <= b: return self.min_v[i]\r\n        vl\
    \ = self.fold_min(a, b, i * 2 + 1, l, (l + r) // 2)\r\n        vr = self.fold_min(a,\
    \ b, i * 2 + 2, (l + r) // 2, r)\r\n        return min(vl, vr)\r\n\r\n    def\
    \ fold_max(self, a, b, i=0, l=0, r=-1):\r\n        if r == -1: r = self.size\r\
    \n        self.push(i, l, r)\r\n        if r <= a or b <= l: return self.MIN\r\
    \n        if a <= l and r <= b: return self.max_v[i]\r\n        vl = self.fold_max(a,\
    \ b, i * 2 + 1, l, (l + r) // 2)\r\n        vr = self.fold_max(a, b, i * 2 + 2,\
    \ (l + r) // 2, r)\r\n        return max(vl, vr)\r\n\r\n    def fold_sum(self,\
    \ a, b, i=0, l=0, r=-1):\r\n        if r == -1: r = self.size\r\n        self.push(i,\
    \ l, r)\r\n        if r <= a or b <= l: return 0\r\n        if a <= l and r <=\
    \ b: return self.sum_[i]\r\n        vl = self.fold_sum(a, b, i * 2 + 1, l, (l\
    \ + r) // 2)\r\n        vr = self.fold_sum(a, b, i * 2 + 2, (l + r) // 2, r)\r\
    \n        return vl + vr\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\SegmentTree\SegmentTreeBeats.py
  requiredBy: []
  timestamp: '2021-01-15 08:52:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure\SegmentTree\SegmentTreeBeats.py
layout: document
title: Segment Tree Beats
---
