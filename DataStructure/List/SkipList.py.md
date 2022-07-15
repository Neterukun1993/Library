---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: misc/xorshift.py
    title: "\u4E71\u6570\u751F\u6210 (Xorshift)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ITP2_1_C.SkipList.test.py
    title: TestCase/AOJ/ITP2_1_C.SkipList.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from misc.xorshift import xorshift32\n\n\nclass SLNode:\n    def __init__(self,\
    \ val, height):\n        self.val = val\n        self.next = [None] * height\n\
    \        self.length = [0] * height\n\n\nclass SkipList:\n    def __init__(self,\
    \ MAX_HEIGHT=20):\n        self.MAX_HEIGHT = MAX_HEIGHT\n        self.LENGTH =\
    \ 1 << MAX_HEIGHT\n        self.sentinel_nd = SLNode(-1, self.MAX_HEIGHT)\n  \
    \      self.size = 0\n        self.rand32 = xorshift32()\n\n    def __getitem__(self,\
    \ i):\n        return self._find_nd(i).next[0].val\n\n    def __setitem__(self,\
    \ i, val):\n        _find_nd(i).next[0] = val\n\n    def _find_nd(self, i):\n\
    \        nd = self.sentinel_nd\n        idx = -1\n        for r in reversed(range(self.MAX_HEIGHT)):\n\
    \            while nd.next[r] is not None and idx + nd.length[r] < i:\n      \
    \          idx += nd.length[r]\n                nd = nd.next[r]\n        return\
    \ nd\n\n    def _pick_height(self):\n        return self.MAX_HEIGHT - (self.rand32()\
    \ & (self.LENGTH - 1)).bit_length() + 1\n\n    def insert(self, i, val):\n   \
    \     if i > self.size:\n            raise IndexError\n        nd = self.sentinel_nd\n\
    \        h = self._pick_height()\n        new_nd = SLNode(val, h)\n        idx\
    \ = -1\n        for r in reversed(range(self.MAX_HEIGHT)):\n            while\
    \ nd.next[r] is not None and idx + nd.length[r] < i:\n                idx += nd.length[r]\n\
    \                nd = nd.next[r]\n            nd.length[r] += 1\n            if\
    \ r < h:\n                new_nd.next[r] = nd.next[r]\n                nd.next[r]\
    \ = new_nd\n                new_nd.length[r] = nd.length[r] - (i - idx)\n    \
    \            nd.length[r] = i - idx\n        self.size += 1\n\n    def delete(self,\
    \ i):\n        if i >= self.size:\n            raise IndexError\n        nd =\
    \ self.sentinel_nd\n        idx = -1\n        for r in reversed(range(self.MAX_HEIGHT)):\n\
    \            while nd.next[r] is not None and idx + nd.length[r] < i:\n      \
    \          idx += nd.length[r]\n                nd = nd.next[r]\n            nd.length[r]\
    \ -= 1\n            if idx + nd.length[r] + 1 == i and nd.next[r] is not None:\n\
    \                val = nd.next[r].val\n                nd.length[r] += nd.next[r].length[r]\n\
    \                deleted = nd.next[r]\n                nd.next[r] = nd.next[r].next[r]\n\
    \        del deleted\n        self.size -= 1\n\n    def dump(self):\n        res\
    \ = []\n        nd = self.sentinel_nd.next[0]\n        while nd is not None:\n\
    \            res.append(nd.val)\n            nd = nd.next[0]\n        return res\n"
  dependsOn:
  - misc/xorshift.py
  isVerificationFile: false
  path: DataStructure/List/SkipList.py
  requiredBy: []
  timestamp: '2022-01-22 19:35:09+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ITP2_1_C.SkipList.test.py
documentation_of: DataStructure/List/SkipList.py
layout: document
title: "\u5BFE\u6570\u6642\u9593\u30E9\u30F3\u30C0\u30E0\u30A2\u30AF\u30BB\u30B9/\u633F\
  \u5165/\u524A\u9664\u53EF\u80FD\u30EA\u30B9\u30C8 (\u30B9\u30AD\u30C3\u30D7\u30EA\
  \u30B9\u30C8)"
---

## 概要
要素のランダムアクセス、挿入、削除を $\mathrm{expected}\ O(H + \log N)$ で行えるリスト。

## 使い方
`SkipList()`  
空のリストを作成する。ノードの高さを $H$ (デフォルトでは $H = 20$) としたときに、計算量 $O(H)$

- `__getitem__(i: int) -> int`  
$i$ 番目の要素を返す。計算量 $\mathrm{expected}\ O(H + \log N)$

- `__setitem__(i: int, val: int) -> None`  
$i$ 番目の要素に `val` を代入する。計算量 $\mathrm{expected}\ O(H + \log N)$

- `insert(i: int, val: int) -> None`  
$i$ 番目の位置に $val$ を挿入する。計算量 $\mathrm{expected}\ O(H + \log N)$

- `delete(i: int) -> None`  
$i$ 番目の要素を削除する。計算量 $\mathrm{expected}\ O(H + \log N)$

- `dump() -> List[int]`  
リストの要素を列挙した結果を返す。計算量 $O(N)$
