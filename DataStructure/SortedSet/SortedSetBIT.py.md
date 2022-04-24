---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure/SortedSet/SortedMultiSetBIT.py
    title: "\u9806\u5E8F\u4ED8\u304D\u591A\u91CD\u96C6\u5408 (Binary Indexed Tree)"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ITP2_7_B.BIT.test.py
    title: TestCase/AOJ/ITP2_7_B.BIT.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
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
    \ - 1)\n\n    def prev_val(self, upper):\n        upper = bisect_left(self.array,\
    \ upper)\n        k = self._count(upper) - 1\n        return None if k == -1 else\
    \ self.kth_smallest(k)\n\n    def next_val(self, lower):\n        lower = bisect_left(self.array,\
    \ lower)\n        k = self._count(lower)\n        return None if k == self.cnt\
    \ else self.kth_smallest(k)\n\n    def all_dump(self):\n        res = self.bit[:]\n\
    \        for i in reversed(range(1, self.size)):\n            if i + (i & -i)\
    \ > self.size:\n                continue\n            res[i + (i & -i)] -= res[i]\n\
    \        return [self.array[i] for i, flag in enumerate(res[1:]) if flag]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SortedSet/SortedSetBIT.py
  requiredBy:
  - DataStructure/SortedSet/SortedMultiSetBIT.py
  timestamp: '2021-02-06 18:04:37+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ITP2_7_B.BIT.test.py
documentation_of: DataStructure/SortedSet/SortedSetBIT.py
layout: document
title: "\u9806\u5E8F\u4ED8\u304D\u96C6\u5408 (Binary Indexed Tree)"
---
## 概要
Binary Indexed Tree による順序付き集合。集合に属する可能性のある要素を、あらかじめ与える必要があることに注意。

## 使い方
`SortedSetBIT(cands: Iterable[int])`  
`cands` 内の要素を元として含むことが可能な、空の順序付き集合を作成する。`n = len(cands)` とすると、計算量 $O(n \log n)$

- `__contains__(val: int) -> bool`  
要素 `val` が集合に属しているかどうかを返す。計算量 $O(\log n)$

- `__len__() -> int`  
集合の大きさを返す。計算量 $O(1)$

- `add(val: int) -> bool`  
要素 `val` を集合に追加する。追加に成功した場合は `True` を、失敗した場合 (既に `val` が集合に属していた場合) は `False` を返す。`val` が `cands` の要素ではない場合は例外 `KeyError` が発生するので注意。計算量 $O(\log n)$

- `remove(val: int) -> bool`  
集合から `val` を削除する。削除に成功した場合は `True` を、失敗した場合 (`val` が集合に属していなかった場合) は `False` を返す。計算量 $O(\log n)$

- `count(vl: int, vr: int) -> int`  
集合内の `vl` 以上かつ `vr` 未満である要素の数を返す。計算量 $O(\log n)$

- `kth_smallest(k: int) -> int`  
集合内で `k` 番目 (0-indexed) に小さい要素を返す。計算量 $O(\log n)$

- `kth_largest(k: int) -> int`  
集合内で `k` 番目 (0-indexed) に大きい要素を返す。計算量 $O(\log n)$

- `prev_val(upper: int) -> int`  
集合内で `upper` よりも小さい最大の要素を返す。そのような要素が存在しない場合は `None` を返す。計算量 $O(\log n)$

- `next_val(lower: int) -> int`  
集合内で `lower` 以上の最小の要素を返す。そのような要素が存在しない場合は `None` を返す。計算量 $O(\log n)$

- `dump() -> List[int]`  
集合内の全ての要素を小さい順に返す。計算量 $O(n)$
