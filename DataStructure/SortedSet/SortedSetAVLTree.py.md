---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ITP2_7_C.AVLTree.test.py
    title: TestCase/AOJ/ITP2_7_C.AVLTree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class AVLNode:\n    def __init__(self, key):\n        self.key = key\n  \
    \      self.h = 1\n        self.l, self.r, self.p = None, None, None\n\n    def\
    \ rotl(self):\n        nd = self.r\n        nd.p = self.p\n        if nd.p is\
    \ not None:\n            if nd.p.l is self: nd.p.l = nd\n            else: nd.p.r\
    \ = nd\n        self.r = nd.l\n        if self.r is not None: self.r.p = self\n\
    \        self.p = nd\n        nd.l = self\n        self.h = self.get_h()\n   \
    \     nd.h = nd.get_h()\n        return nd\n\n    def rotr(self):\n        nd\
    \ = self.l\n        nd.p = self.p\n        if nd.p is not None:\n            if\
    \ nd.p.r is self: nd.p.r = nd\n            else: nd.p.l = nd\n        self.l =\
    \ nd.r\n        if self.l is not None: self.l.p = self\n        self.p = nd\n\
    \        nd.r = self\n        self.h = self.get_h()\n        nd.h = nd.get_h()\n\
    \        return nd\n\n    def get_h(self):\n        lh = self.l.h if self.l is\
    \ not None else 0\n        rh = self.r.h if self.r is not None else 0\n      \
    \  return max(lh, rh) + 1\n\n    def get_bf(self):\n        lh = self.l.h if self.l\
    \ is not None else 0\n        rh = self.r.h if self.r is not None else 0\n   \
    \     return lh - rh\n\n\nclass SortedSetAVLTree:\n    def __init__(self):\n \
    \       self.root = None\n        self.size = 0\n\n    def __contains__(self,\
    \ key):\n        return self._search(key)\n\n    def __len__(self):\n        return\
    \ self.size\n\n    def __iter__(self):\n        def dfs(nd):\n            if nd.l\
    \ is not None:\n                yield from dfs(nd.l)\n            yield nd.key\n\
    \            if nd.r is not None:\n                yield from dfs(nd.r)\n    \
    \    if self.root is not None:\n            yield from dfs(self.root)\n\n    def\
    \ _search(self, key):\n        nd = self.root\n        while nd is not None:\n\
    \            if nd.key < key: nd = nd.r\n            elif nd.key > key: nd = nd.l\n\
    \            else: return True\n        return False\n\n    def _balance_add(self,\
    \ nd):\n        chi_bf = 0\n        while True:\n            nd.h, bf = nd.get_h(),\
    \ nd.get_bf()\n            if bf > 1:\n                if chi_bf < 0: nd.l = nd.l.rotl()\n\
    \                pv = nd.rotr()\n                if pv.p is None: self.root =\
    \ pv\n                return\n            elif bf < -1:\n                if chi_bf\
    \ > 0: nd.r = nd.r.rotr()\n                pv = nd.rotl()\n                if\
    \ pv.p is None: self.root = pv\n                return\n            elif bf ==\
    \ 0 or nd.p is None: return\n            nd = nd.p\n            chi_bf = bf\n\n\
    \    def _balance_rem(self, nd):\n        while True:\n            pv = None\n\
    \            nd.h, bf = nd.get_h(), nd.get_bf()\n            if bf > 1:\n    \
    \            if nd.l.get_bf() < 0: nd.l = nd.l.rotl()\n                pv = nd.rotr()\n\
    \            elif bf < -1:\n                if nd.r.get_bf() > 0: nd.r = nd.r.rotr()\n\
    \                pv = nd.rotl()\n            elif bf != 0: return\n\n        \
    \    if pv is not None:\n                if pv.p is None:\n                  \
    \  self.root = pv\n                    return\n                if pv.get_bf()\
    \ != 0: return\n            else: pv = nd\n            if pv.p is None: return\n\
    \            else: nd = pv.p\n\n    def add(self, key):\n        if self.root\
    \ is None:\n            self.root = AVLNode(key)\n            self.size += 1\n\
    \            return True\n\n        nd = self.root\n        while nd is not None:\n\
    \            if nd.key < key:\n                if nd.r is None:\n            \
    \        nd.r = AVLNode(key)\n                    nd.r.p = nd\n              \
    \      break\n                nd = nd.r\n            elif nd.key > key:\n    \
    \            if nd.l is None:\n                    nd.l = AVLNode(key)\n     \
    \               nd.l.p = nd\n                    break\n                nd = nd.l\n\
    \            else: return False\n        self.size += 1\n        self._balance_add(nd)\n\
    \        return True\n\n    def remove(self, key):\n        if self.root is None:\n\
    \            return False\n\n        nd = self.root\n        while nd is not None:\n\
    \            if nd.key < key: nd = nd.r\n            elif nd.key > key: nd = nd.l\n\
    \            else: break\n        else: return False\n\n        self.size -= 1\n\
    \        if nd.l is not None and nd.r is not None:\n            max_nd = nd.l\n\
    \            while max_nd.r is not None:\n                max_nd = max_nd.r\n\
    \            nd.key = max_nd.key\n            nd = max_nd\n\n        chi_nd =\
    \ nd.r if nd.r is not None else nd.l\n        if nd is self.root:\n          \
    \  self.root = chi_nd\n            if self.root is not None: self.root.p = None\n\
    \            return True\n        elif nd.p.r is nd:\n            nd.p.r = chi_nd\n\
    \            if chi_nd is not None: chi_nd.p = nd.p\n        else:\n         \
    \   nd.p.l = chi_nd\n            if chi_nd is not None: chi_nd.p = nd.p\n    \
    \    self._balance_rem(nd.p)\n        return True\n\n    def iterate(self, lower):\n\
    \        def dfs(nd):\n            if nd.l is not None and (nd.key > lower):\n\
    \                yield from dfs(nd.l)\n            if nd.key >= lower:\n     \
    \           yield nd.key\n            if nd.r is not None:\n                yield\
    \ from dfs(nd.r)\n        if self.root is not None:\n            yield from dfs(self.root)\n\
    \n    def next_val(self, lower):\n        nd = self.root\n        ret = None\n\
    \        while nd is not None:\n            if nd.key >= lower:\n            \
    \    ret = nd.key\n                nd = nd.l\n            else: nd = nd.r\n  \
    \      return ret\n\n    def prev_val(self, upper):\n        nd = self.root\n\
    \        ret = None\n        while nd is not None:\n            if nd.key < upper:\n\
    \                ret = nd.key\n                nd = nd.r\n            else: nd\
    \ = nd.l\n        return ret\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SortedSet/SortedSetAVLTree.py
  requiredBy: []
  timestamp: '2021-05-13 01:21:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ITP2_7_C.AVLTree.test.py
documentation_of: DataStructure/SortedSet/SortedSetAVLTree.py
layout: document
title: "\u9806\u5E8F\u4ED8\u304D\u96C6\u5408 (AVL Tree)"
---

## 概要
AVL Tree による順序付き集合。[B-Tree](https://neterukun1993.github.io/Library/DataStructure/SortedSet/SortedSetBTree.py) による実装の方が高速なのでそちらを使いましょう。

## 使い方
`SortedSetAVLTree()`  
空の順序付き集合を作成する。計算量 $O(1)$

- `__contains__(key: int) -> bool`  
要素 `key` が集合に属しているかどうかを返す。計算量 $O(\log N)$

- `__len__() -> int`  
集合の大きさを返す。計算量 $O(1)$

- `__iter__() -> Iterator[int]`  
要素の小さい順のイテレータオブジェクトを返す。イテレーション $1$ 回の計算量 $O(\log N)$。全 $N$ 要素のイテレーションの計算量 $O(N)$

- `add(key: int) -> bool`  
要素 `key` を集合に追加する。追加に成功した場合は `True` を、失敗した場合 (既に `key` が集合に属していた場合) は `False` を返す。計算量 $O(\log N)$

- `remove(key: int) -> bool`  
集合から `key` を削除する。削除に成功した場合は `True` を、失敗した場合 (`key` が集合に属していなかった場合) は `False` を返す。計算量 $O(\log N)$

- `iterate(lower: int) -> Iterator[int]`  
`lower` 以上の要素に対して、小さい順のイテレータオブジェクトを返す。イテレーション $1$ 回の計算量 $O(\log N)$。全 $k$ 要素のイテレーションの計算量 $O(k + \log N)$

- `next_val(lower: int) -> int`  
`lower` 以上の最小の要素を返す。そのような要素が存在しない場合は `None` を返す。計算量 $O(\log N)$

- `prev_val(upper: int) -> int`  
`upper` よりも小さい最大の要素を返す。そのような要素が存在しない場合は `None` を返す。計算量 $O(\log N)$
