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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class SegmentTreeBeats:\n    def __init__(self, n, INF=10**18):\n       \
    \ self.MAX = INF\n        self.MIN = -INF\n        self.size = 1 << (n - 1).bit_length()\n\
    \        sz = self.size * 2 - 1\n        self.sum_ = [0] * sz\n        self.max_v\
    \ = [self.MIN] * sz\n        self.min_v = [self.MAX] * sz\n        self.max_c\
    \ = [1] * sz\n        self.min_c = [1] * sz\n        self.smax_v = [self.MIN]\
    \ * sz\n        self.smin_v = [self.MAX] * sz\n        self.lz_add = [0] * sz\n\
    \n    def build(self, array):\n        for i, val in enumerate(array, self.size\
    \ - 1):\n            self.sum_[i] = self.min_v[i] = self.max_v[i] = val\n    \
    \    for i in range(self.size - 2, -1, -1):\n            self.update(i)\n\n  \
    \  def update(self, i):\n        if i >= self.size - 1: return\n        i1, i2\
    \ = i * 2 + 1, i * 2 + 2\n        self.sum_[i] = self.sum_[i1] + self.sum_[i2]\n\
    \        self.max_v[i] = max(self.max_v[i1], self.max_v[i2])\n        if self.max_v[i1]\
    \ > self.max_v[i2]:\n            self.max_c[i] = self.max_c[i1]\n            self.smax_v[i]\
    \ = max(self.smax_v[i1], self.max_v[i2])\n        elif self.max_v[i1] < self.max_v[i2]:\n\
    \            self.max_c[i] = self.max_c[i2]\n            self.smax_v[i] = max(self.max_v[i1],\
    \ self.smax_v[i2])\n        else:\n            self.max_c[i] = self.max_c[i1]\
    \ + self.max_c[i2]\n            self.smax_v[i] = max(self.smax_v[i1], self.smax_v[i2])\n\
    \n        self.min_v[i] = min(self.min_v[i1], self.min_v[i2])\n        if self.min_v[i1]\
    \ < self.min_v[i2]:\n            self.min_c[i] = self.min_c[i1]\n            self.smin_v[i]\
    \ = min(self.smin_v[i1], self.min_v[i2])\n        elif self.min_v[i1] > self.min_v[i2]:\n\
    \            self.min_c[i] = self.min_c[i2]\n            self.smin_v[i] = min(self.min_v[i1],\
    \ self.smin_v[i2])\n        else:\n            self.min_c[i] = self.min_c[i1]\
    \ + self.min_c[i2]\n            self.smin_v[i] = min(self.smin_v[i1], self.smin_v[i2])\n\
    \n    def push(self, i, l, r):\n        i1, i2 = i * 2 + 1, i * 2 + 2\n      \
    \  if self.lz_add[i] != 0:\n            self.sum_[i] += self.lz_add[i] * (r -\
    \ l)\n            self.min_v[i] += self.lz_add[i]\n            self.smin_v[i]\
    \ += self.lz_add[i]\n            self.max_v[i] += self.lz_add[i]\n           \
    \ self.smax_v[i] += self.lz_add[i]\n            if i < self.size - 1:\n      \
    \          self.lz_add[i1] += self.lz_add[i]\n                self.lz_add[i2]\
    \ += self.lz_add[i]\n            self.lz_add[i] = 0\n        if i < self.size\
    \ - 1:\n            if self.max_v[i] < self.max_v[i1] + self.lz_add[i1]:\n   \
    \             self.chmin_at(i1, self.max_v[i] - self.lz_add[i1], l, (l + r) //\
    \ 2)\n            if self.max_v[i] < self.max_v[i2] + self.lz_add[i2]:\n     \
    \           self.chmin_at(i2, self.max_v[i] - self.lz_add[i2], (l + r) // 2, r)\n\
    \            if self.min_v[i] > self.min_v[i1] + self.lz_add[i1]:\n          \
    \      self.chmax_at(i1, self.min_v[i] - self.lz_add[i1], l, (l + r) // 2)\n \
    \           if self.min_v[i] > self.min_v[i2] + self.lz_add[i2]:\n           \
    \     self.chmax_at(i2, self.min_v[i] - self.lz_add[i2], (l + r) // 2, r)\n\n\
    \    def chmin_at(self, i, x, l, r):\n        if self.max_v[i] == self.min_v[i]:\n\
    \            self.sum_[i] = x * (r - l)\n            self.max_v[i] = self.min_v[i]\
    \ = x\n        elif self.max_v[i] == self.smin_v[i]:\n            self.sum_[i]\
    \ += (x - self.max_v[i]) * self.max_c[i]\n            self.max_v[i] = self.smin_v[i]\
    \ = x\n        else:\n            self.sum_[i] += (x - self.max_v[i]) * self.max_c[i]\n\
    \            self.max_v[i] = x\n\n    def chmax_at(self, i, x, l, r):\n      \
    \  if self.max_v[i] == self.min_v[i]:\n            self.sum_[i] = x * (r - l)\n\
    \            self.max_v[i] = self.min_v[i] = x\n        elif self.min_v[i] ==\
    \ self.smax_v[i]:\n            self.sum_[i] += (x - self.min_v[i]) * self.min_c[i]\n\
    \            self.min_v[i] = self.smax_v[i] = x\n        else:\n            self.sum_[i]\
    \ += (x - self.min_v[i]) * self.min_c[i]\n            self.min_v[i] = x\n\n  \
    \  def range_chmin(self, a, b, x, i=0, l=0, r=-1):\n        if r == -1: r = self.size\n\
    \        self.push(i, l, r)\n        if r <= a or b <= l or self.max_v[i] <= x:\
    \ return\n        if a <= l and r <= b and self.smax_v[i] < x:\n            self.chmin_at(i,\
    \ x, l, r)\n            self.push(i, l, r)\n            return\n        self.range_chmin(a,\
    \ b, x, i * 2 + 1, l, (l + r) // 2)\n        self.range_chmin(a, b, x, i * 2 +\
    \ 2, (l + r) // 2, r)\n        self.update(i)\n\n    def range_chmax(self, a,\
    \ b, x, i=0, l=0, r=-1):\n        if r == -1: r = self.size\n        self.push(i,\
    \ l, r)\n        if r <= a or b <= l or self.min_v[i] >= x: return\n        if\
    \ a <= l and r <= b and self.smin_v[i] > x:\n            self.chmax_at(i, x, l,\
    \ r)\n            self.push(i, l, r)\n            return\n        self.range_chmax(a,\
    \ b, x, i * 2 + 1, l, (l + r) // 2)\n        self.range_chmax(a, b, x, i * 2 +\
    \ 2, (l + r) // 2, r)\n        self.update(i)\n\n    def range_add(self, a, b,\
    \ x, i=0, l=0, r=-1):\n        if r == -1: r = self.size\n        self.push(i,\
    \ l, r)\n        if r <= a or b <= l: return\n        if a <= l and r <= b:\n\
    \            self.lz_add[i] += x\n            self.push(i, l, r)\n           \
    \ return\n        self.range_add(a, b, x, i * 2 + 1, l, (l + r) // 2)\n      \
    \  self.range_add(a, b, x, i * 2 + 2, (l + r) // 2, r)\n        self.update(i)\n\
    \n    def fold_min(self, a, b, i=0, l=0, r=-1):\n        if r == -1: r = self.size\n\
    \        self.push(i, l, r)\n        if r <= a or b <= l: return self.MAX\n  \
    \      if a <= l and r <= b: return self.min_v[i]\n        vl = self.fold_min(a,\
    \ b, i * 2 + 1, l, (l + r) // 2)\n        vr = self.fold_min(a, b, i * 2 + 2,\
    \ (l + r) // 2, r)\n        return min(vl, vr)\n\n    def fold_max(self, a, b,\
    \ i=0, l=0, r=-1):\n        if r == -1: r = self.size\n        self.push(i, l,\
    \ r)\n        if r <= a or b <= l: return self.MIN\n        if a <= l and r <=\
    \ b: return self.max_v[i]\n        vl = self.fold_max(a, b, i * 2 + 1, l, (l +\
    \ r) // 2)\n        vr = self.fold_max(a, b, i * 2 + 2, (l + r) // 2, r)\n   \
    \     return max(vl, vr)\n\n    def fold_sum(self, a, b, i=0, l=0, r=-1):\n  \
    \      if r == -1: r = self.size\n        self.push(i, l, r)\n        if r <=\
    \ a or b <= l: return 0\n        if a <= l and r <= b: return self.sum_[i]\n \
    \       vl = self.fold_sum(a, b, i * 2 + 1, l, (l + r) // 2)\n        vr = self.fold_sum(a,\
    \ b, i * 2 + 2, (l + r) // 2, r)\n        return vl + vr\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SegmentTree/SegmentTreeBeats.py
  requiredBy: []
  timestamp: '2021-01-15 08:52:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/SegmentTree/SegmentTreeBeats.py
layout: document
title: Segment Tree Beats
---
