---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ITP2_7_C.AATree.test.py
    title: TestCase/AOJ/ITP2_7_C.AATree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class AANode:\n    Nil = None\n\n    def __init__(self, key):\n        self.key\
    \ = key\n        self.lv = 1\n        self.l, self.r, self.p = self.Nil, self.Nil,\
    \ self.Nil\n\n    def skew(self):\n        if self.l.lv == self.lv:\n        \
    \    pv = self._rotr()\n            return pv\n        return self\n\n    def\
    \ split(self):\n        if self.r.r.lv == self.lv:\n            pv = self._rotl()\n\
    \            pv.lv += 1\n            return pv\n        return self\n\n    def\
    \ skew_split(self):\n        pv = self\n        if pv.l.lv == pv.lv:\n       \
    \     pv = pv._rotr()\n        if pv.r.r.lv == pv.lv:\n            pv = pv._rotl()\n\
    \            pv.lv += 1\n        return pv\n\n    def _rotl(self):\n        pv\
    \ = self.r\n        pv.p = self.p\n        if pv.p is not self.Nil:\n        \
    \    if pv.p.l is self: pv.p.l = pv\n            else: pv.p.r = pv\n        self.r\
    \ = pv.l\n        if self.r is not self.Nil: self.r.p = self\n        self.p =\
    \ pv\n        pv.l = self\n        return pv\n\n    def _rotr(self):\n       \
    \ pv = self.l\n        pv.p = self.p\n        if pv.p is not self.Nil:\n     \
    \       if pv.p.r is self: pv.p.r = pv\n            else: pv.p.l = pv\n      \
    \  self.l = pv.r\n        if self.l is not self.Nil: self.l.p = self\n       \
    \ self.p = pv\n        pv.r = self\n        return pv\n\n\nclass SortedSetAATree:\n\
    \    Nil = AANode(-1)\n    AANode.Nil = Nil\n    Nil.lv = 0\n    Nil.l, Nil.r,\
    \ Nil.p = Nil, Nil, Nil\n\n    def __init__(self):\n        self.root = self.Nil\n\
    \        self.size = 0\n\n    def __contains__(self, key):\n        return self._search(key)\n\
    \n    def __len__(self):\n        return self.size\n\n    def __iter__(self):\n\
    \        def dfs(nd):\n            if nd.l is not self.Nil:\n                yield\
    \ from dfs(nd.l)\n            yield nd.key\n            if nd.r is not self.Nil:\n\
    \                yield from dfs(nd.r)\n        if self.root is not self.Nil:\n\
    \            yield from dfs(self.root)\n\n    def _search(self, key):\n      \
    \  nd = self.root\n        while nd is not self.Nil:\n            if nd.key <\
    \ key: nd = nd.r\n            elif nd.key > key: nd = nd.l\n            else:\
    \ return True\n        return False\n\n    def _balance_del(self, nd):\n     \
    \   while nd is not self.Nil:\n            if nd.l.lv < nd.lv - 1 or nd.r.lv <\
    \ nd.lv - 1:\n                nd.lv -= 1\n                if nd.r.lv > nd.lv:\n\
    \                    nd.r.lv = nd.lv\n                nd = nd.skew()\n       \
    \         nd.r = nd.r.skew()\n                nd.r.r = nd.r.r.skew()\n       \
    \         nd = nd.split()\n                nd.r = nd.r.split()\n            self.root\
    \ = nd\n            nd = nd.p\n\n    def add(self, key):\n        if self.root\
    \ is self.Nil:\n            self.root = AANode(key)\n            self.size +=\
    \ 1\n            return True\n\n        nd = self.root\n        while nd is not\
    \ self.Nil:\n            if nd.key < key:\n                if nd.r is self.Nil:\n\
    \                    nd.r = AANode(key)\n                    self.size += 1\n\
    \                    nd.r.p = nd\n                    if nd.lv + 1 == nd.p.lv:\n\
    \                        return True\n                    break\n            \
    \    nd = nd.r\n            elif nd.key > key:\n                if nd.l is self.Nil:\n\
    \                    nd.l = AANode(key)\n                    self.size += 1\n\
    \                    nd.l.p = nd\n                    break\n                nd\
    \ = nd.l\n            else: return False\n\n        while nd is not self.Nil:\n\
    \            nd = nd.skew_split()\n            self.root = nd\n            nd\
    \ = nd.p\n        return True\n\n    def remove(self, key):\n        if self.root\
    \ is self.Nil: return False\n\n        nd = self.root\n        while nd is not\
    \ self.Nil:\n            if nd.key < key: nd = nd.r\n            elif nd.key >\
    \ key: nd = nd.l\n            else: break\n        else: return False\n\n    \
    \    self.size -= 1\n        if nd.l is not self.Nil and nd.r is not self.Nil:\n\
    \            min_nd = nd.r\n            while min_nd.l is not self.Nil:\n    \
    \            min_nd = min_nd.l\n            nd.key = min_nd.key\n            nd\
    \ = min_nd\n\n        chi_nd = nd.r if nd.r is not self.Nil else nd.l\n      \
    \  if nd is self.root:\n            self.root = chi_nd\n            if self.root\
    \ is not self.Nil: self.root.p = self.Nil\n            return True\n        elif\
    \ nd.p.r is nd:\n            nd.p.r = chi_nd\n            if chi_nd is not self.Nil:\
    \ chi_nd.p = nd.p\n        else:\n            nd.p.l = chi_nd\n            if\
    \ chi_nd is not self.Nil: chi_nd.p = nd.p\n        self._balance_del(nd.p)\n \
    \       return True\n\n    def iterate(self, lower):\n        def dfs(nd):\n \
    \           if nd.l is not self.Nil and (nd.key > lower):\n                yield\
    \ from dfs(nd.l)\n            if nd.key >= lower:\n                yield nd.key\n\
    \            if nd.r is not self.Nil:\n                yield from dfs(nd.r)\n\
    \        if self.root is not self.Nil:\n            yield from dfs(self.root)\n\
    \n    def next_key(self, lower):\n        nd = self.root\n        ret = None\n\
    \        while nd is not self.Nil:\n            if nd.key >= lower:\n        \
    \        ret = nd.key\n                nd = nd.l\n            else: nd = nd.r\n\
    \        return ret\n\n    def prev_key(self, upper):\n        nd = self.root\n\
    \        ret = None\n        while nd is not self.Nil:\n            if nd.key\
    \ < upper:\n                ret = nd.key\n                nd = nd.r\n        \
    \    else: nd = nd.l\n        return ret\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SortedSet/SortedSetAATree.py
  requiredBy: []
  timestamp: '2021-05-12 01:32:34+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ITP2_7_C.AATree.test.py
documentation_of: DataStructure/SortedSet/SortedSetAATree.py
layout: document
title: "\u9806\u5E8F\u4ED8\u304D\u96C6\u5408 (AA Tree)"
---

## 概要
AA Tree による順序付き集合。[B-Tree](https://neterukun1993.github.io/Library/DataStructure/SortedSet/SortedSetBTree.py) による実装の方が高速なのでそちらを使いましょう。

## 使い方
`SortedSetAATree()`  
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
