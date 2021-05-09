---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: misc/xorshift.py
    title: "\u4E71\u6570\u751F\u6210 (Xorshift)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ITP2_7_C.SkipList.test.py
    title: TestCase/AOJ/ITP2_7_C.SkipList.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from misc.xorshift import xorshift32\n\n\nclass SLSSNode:\n    Nil = None\n\
    \n    def __init__(self, val, height):\n        self.val = val\n        self.next\
    \ = [self.Nil] * height\n\n\nclass SortedSetSkipList:\n    MAX_HEIGHT = 20\n \
    \   LENGTH = 1 << MAX_HEIGHT\n    INF = 1 << 64\n    Nil = SLSSNode(INF, MAX_HEIGHT)\n\
    \    SLSSNode.Nil = Nil\n    Nil.next = [Nil] * MAX_HEIGHT\n\n    def __init__(self,\
    \ MAX_HEIGHT=20):\n        self.sentinel_nd = SLSSNode(-self.INF, self.MAX_HEIGHT)\n\
    \        self.size = 0\n        self.rand32 = xorshift32()\n\n    def __contains__(self,\
    \ key):\n        return self._search(key)\n\n    def __len__(self):\n        return\
    \ self.size\n\n    def __iter__(self):\n        nd = self.sentinel_nd\n      \
    \  while nd.next[0].val != self.INF:\n            yield nd.next[0].val\n     \
    \       nd = nd.next[0]\n\n    def _pick_height(self):\n        return self.MAX_HEIGHT\
    \ - (self.rand32() & (self.LENGTH - 1)).bit_length() + 1\n\n    def _search(self,\
    \ val):\n        nd = self.sentinel_nd\n        for r in reversed(range(self.MAX_HEIGHT)):\n\
    \            while nd.next[r].val < val:\n                nd = nd.next[r]\n  \
    \      if nd.next[r].val == val:\n            return True\n        return False\n\
    \n    def add(self, val):\n        nd = self.sentinel_nd\n        stack = []\n\
    \n        h = self._pick_height()\n        for r in reversed(range(self.MAX_HEIGHT)):\n\
    \            while nd.next[r].val < val:\n                nd = nd.next[r]\n  \
    \          if nd.next[r].val == val:\n                return False\n         \
    \   elif r < h:\n                stack.append(nd)\n\n        nd = SLSSNode(val,\
    \ h)\n        for r, st_nd in enumerate(reversed(stack)):\n            nd.next[r]\
    \ = st_nd.next[r]\n            st_nd.next[r] = nd\n        self.size += 1\n  \
    \      return True\n\n    def remove(self, val):\n        del_nd = self.Nil\n\
    \        nd = self.sentinel_nd\n        for r in reversed(range(self.MAX_HEIGHT)):\n\
    \            while nd.next[r].val < val:\n                nd = nd.next[r]\n  \
    \          if nd.next[r].val == val:\n                del_nd = nd.next[r]\n  \
    \              nd.next[r] = nd.next[r].next[r]\n        if del_nd is self.Nil:\n\
    \            return False\n        self.size -= 1\n        return True\n\n   \
    \ def iterate(self, lower):\n        nd = self.sentinel_nd\n        for r in reversed(range(self.MAX_HEIGHT)):\n\
    \            while nd.next[r].val < lower:\n                nd = nd.next[r]\n\
    \        while nd.next[0].val != self.INF:\n            yield nd.next[0].val\n\
    \            nd = nd.next[0]\n\n    def next_val(self, lower):\n        nd = self.sentinel_nd\n\
    \        for r in reversed(range(self.MAX_HEIGHT)):\n            while nd.next[r].val\
    \ < lower:\n                nd = nd.next[r]\n        return None if nd.next[r].val\
    \ == self.INF else nd.next[r].val\n\n    def prev_val(self, upper):\n        nd\
    \ = self.sentinel_nd\n        for r in reversed(range(self.MAX_HEIGHT)):\n   \
    \         while nd.next[r].val < upper:\n                nd = nd.next[r]\n   \
    \     return None if nd.val == -self.INF else nd.val\n"
  dependsOn:
  - misc/xorshift.py
  isVerificationFile: false
  path: DataStructure/SortedSet/SortedSetSkipList.py
  requiredBy: []
  timestamp: '2021-05-09 21:08:49+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ITP2_7_C.SkipList.test.py
documentation_of: DataStructure/SortedSet/SortedSetSkipList.py
layout: document
title: "\u9806\u5E8F\u4ED8\u304D\u96C6\u5408 (\u30B9\u30AD\u30C3\u30D7\u30EA\u30B9\
  \u30C8)"
---

## 概要
スキップリストによる順序付き集合。[B-Tree](https://neterukun1993.github.io/Library/DataStructure/SortedSet/SortedSetBTree.py) による実装の方が高速なのでそちらを使いましょう。

## 使い方
`SortedSetSkipList()`  
空の順序付き集合を作成する。ノードの高さを $H$ (デフォルトでは $H = 20$) としたときに、計算量 $O(H)$

- `__contains__(key: int) -> bool`  
要素 `key` が集合に属しているかどうかを返す。計算量 $\mathrm{expected}\ O(H + \log N)$

- `__len__() -> int`  
集合の大きさを返す。計算量 $O(1)$

- `__iter__() -> Iterator[int]`  
要素の小さい順のイテレータオブジェクトを返す。オブジェクト生成の計算量 $O(1)$。イテレーション1回の計算量 $O(1)$

- `add(key: int) -> bool`  
要素 `key` を集合に追加する。追加に成功した場合は `True` を、失敗した場合 (既に `key` が集合に属していた場合) は `False` を返す。計算量 $\mathrm{expected}\ O(H + \log N)$

- `remove(key: int) -> bool`  
集合から `key` を削除する。削除に成功した場合は `True` を、失敗した場合 (`key` が集合に属していなかった場合) は `False` を返す。計算量 $\mathrm{expected}\ O(H + \log N)$

- `iterate(lower: int) -> Iterator[int]`  
`lower` 以上の要素に対して、小さい順のイテレータオブジェクトを返す。オブジェクト生成の計算量 $\mathrm{expected}\ O(H + \log N)$。イテレーション1回の計算量 $O(1)$

- `next_val(lower: int) -> int`  
`lower` 以上の最小の要素を返す。そのような要素が存在しない場合は `None` を返す。 $\mathrm{expected}\ O(H + \log N)$

- `prev_val(upper: int) -> int`  
`upper` よりも小さい最大の要素を返す。そのような要素が存在しない場合は `None` を返す。 $\mathrm{expected}\ O(H + \log N)$
