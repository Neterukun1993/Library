---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/IntervalHeap.unittest.test.py
    title: TestCase/unittest/IntervalHeap.unittest.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class IntervalHeap:\n    def __init__(self):\n        self.hp = []\n\n  \
    \  @property\n    def min(self):\n        return self.hp[0]\n\n    @property\n\
    \    def max(self):\n        if len(self) == 1:\n            return self.hp[0]\n\
    \        return self.hp[1]\n\n    def __len__(self):\n        return len(self.hp)\n\
    \n    def push(self, val):\n        self.hp.append(val)\n        k = len(self)\
    \ - 1\n        self._heap_up(k)\n\n    def pop_min(self):\n        if len(self)\
    \ == 0:\n            raise IndexError('pop from empty list')\n        if len(self)\
    \ < 2:\n            return self.hp.pop()\n        self.hp[0], self.hp[-1] = self.hp[-1],\
    \ self.hp[0]\n        res = self.hp.pop()\n        k = self._heap_down(0)\n  \
    \      self._heap_up(k)\n        return res\n\n    def pop_max(self):\n      \
    \  if len(self) == 0:\n            raise IndexError('pop from empty list')\n \
    \       if len(self) < 3:\n            return self.hp.pop()\n        self.hp[1],\
    \ self.hp[-1] = self.hp[-1], self.hp[1]\n        res = self.hp.pop()\n       \
    \ k = self._heap_down(1)\n        self._heap_up(k)\n        return res\n\n   \
    \ def _heap_down(self, k):\n        if k & 1:\n            while 2 * k + 1 < len(self):\n\
    \                chi_k = 2 * k + 3\n                if len(self) <= chi_k or self.hp[chi_k\
    \ - 2] > self.hp[chi_k]:\n                    chi_k -= 2\n                if chi_k\
    \ < len(self) and self.hp[k] < self.hp[chi_k]:\n                    self.hp[k],\
    \ self.hp[chi_k] = self.hp[chi_k], self.hp[k]\n                    k = chi_k\n\
    \                else:\n                    break\n        else:\n           \
    \ while 2 * k + 2 < len(self):\n                chi_k = 2 * k + 4\n          \
    \      if len(self) <= chi_k or self.hp[chi_k - 2] < self.hp[chi_k]:\n       \
    \             chi_k -= 2\n                if chi_k < len(self) and self.hp[k]\
    \ > self.hp[chi_k]:\n                    self.hp[k], self.hp[chi_k] = self.hp[chi_k],\
    \ self.hp[k]\n                    k = chi_k\n                else:\n         \
    \           break\n        return k\n\n    def _heap_up(self, k):\n        if\
    \ k | 1 < len(self) and self.hp[k & ~1] > self.hp[k | 1]:\n            self.hp[k\
    \ & ~1], self.hp[k | 1] = self.hp[k | 1], self.hp[k & ~1]\n            k ^= 1\n\
    \        while k != 0:\n            par_k = ((k >> 1) - 1) & ~1\n            if\
    \ self.hp[par_k] <= self.hp[k]:\n                break\n            self.hp[par_k],\
    \ self.hp[k] = self.hp[k], self.hp[par_k]\n            k = par_k\n        while\
    \ k != 1:\n            par_k = (((k >> 1) - 1) & ~1) | 1\n            if self.hp[par_k]\
    \ >= self.hp[k]:\n                break\n            self.hp[par_k], self.hp[k]\
    \ = self.hp[k], self.hp[par_k]\n            k = par_k\n        return k\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/Heap/IntervalHeap.py
  requiredBy: []
  timestamp: '2021-05-08 17:40:31+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/unittest/IntervalHeap.unittest.test.py
documentation_of: DataStructure/Heap/IntervalHeap.py
layout: document
title: Interval Heap
---
## 概要
最小値と最大値を同時に管理するヒープ。

## 使い方
`IntervalHeap()`  
空のヒープを作成する。計算量 $O(1)$
- `min -> int`  
ヒープ内の最小の値を返す。計算量 $O(1)$
- `max -> int`  
ヒープ内の最大の値を返す。計算量 $O(1)$
- `__len__() -> int`  
ヒープの大きさを返す。計算量 $O(1)$
- `push(val: int)`  
ヒープに `val` を追加する。計算量 $(\log N)$
- `pop_min() -> int`  
ヒープ内の最小の値を削除してその値を返す。計算量 $(\log N)$
- `pop_max() -> int`  
ヒープ内の最大の値を削除してその値を返す。計算量 $(\log N)$
