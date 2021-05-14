---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: misc/xorshift.py
    title: "\u4E71\u6570\u751F\u6210 (Xorshift)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ITP2_7_C.Treap.test.py
    title: TestCase/AOJ/ITP2_7_C.Treap.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from misc.xorshift import xorshift32\nfrom array import array\n\n\nclass\
    \ SortedSetTreap:\n    def __init__(self):\n        self.root = -1\n        self.pow_sz\
    \ = 1\n        self.rand32 = xorshift32()\n        self.stack = array(\"i\", [0])\n\
    \        self.l = array(\"i\", [-1])\n        self.r = array(\"i\", [-1])\n  \
    \      self.p = array(\"i\", [-1])\n        self.pris = array(\"I\", [self.rand32()])\n\
    \        self.keys = [0]\n\n    def __contains__(self, key):\n        return self._search(key)\n\
    \n    def __len__(self):\n        return self.pow_sz - len(self.stack)\n\n   \
    \ def __iter__(self):\n        def dfs(nd):\n            if self.l[nd] != -1:\n\
    \                yield from dfs(self.l[nd])\n            yield self.keys[nd]\n\
    \            if self.r[nd] != -1:\n                yield from dfs(self.r[nd])\n\
    \        if self.root != -1:\n            yield from dfs(self.root)\n\n    def\
    \ _new_node(self, key):\n        if self.stack:\n            nd = self.stack.pop()\n\
    \            self.keys[nd] = key\n            return nd\n        else:\n     \
    \       self.stack = array(\"i\", [nd for nd in range(self.pow_sz, self.pow_sz\
    \ << 1)])\n            self.l += array(\"i\", [-1] * self.pow_sz)\n          \
    \  self.r += array(\"i\", [-1] * self.pow_sz)\n            self.p += array(\"\
    i\", [-1] * self.pow_sz)\n            self.pris += array(\"I\", [self.rand32()\
    \ for _ in range(self.pow_sz)])\n            self.keys += [0] * self.pow_sz\n\
    \            self.pow_sz <<= 1\n            return self._new_node(key)\n\n   \
    \ def _search(self, key):\n        nd = self.root\n        while nd != -1:\n \
    \           if key < self.keys[nd]: nd = self.l[nd]\n            elif key > self.keys[nd]:\
    \ nd = self.r[nd]\n            else: return True\n        return False\n\n   \
    \ def add(self, key):\n        if self.root == -1:\n            self.root = self._new_node(key)\n\
    \            return True\n\n        nd = self.root\n        while True:\n    \
    \        if key < self.keys[nd]:\n                if self.l[nd] == -1:\n     \
    \               self.l[nd] = self._new_node(key)\n                    self.p[self.l[nd]]\
    \ = nd\n                    nd = self.l[nd]\n                    break\n     \
    \           nd = self.l[nd]\n            elif key > self.keys[nd]:\n         \
    \       if self.r[nd] == -1:\n                    self.r[nd] = self._new_node(key)\n\
    \                    self.p[self.r[nd]] = nd\n                    nd = self.r[nd]\n\
    \                    break\n                nd = self.r[nd]\n            else:\n\
    \                return False\n\n        while self.p[nd] != -1 and self.pris[self.p[nd]]\
    \ > self.pris[nd]:\n            if self.r[self.p[nd]] == nd: self._rotl(self.p[nd])\n\
    \            else: self._rotr(self.p[nd])\n        return True\n\n    def _rotl(self,\
    \ nd):\n        pv = self.r[nd]\n        self.p[pv] = self.p[nd]\n        if self.p[pv]\
    \ != -1:\n            if self.l[self.p[pv]] == nd: self.l[self.p[pv]] = pv\n \
    \           else: self.r[self.p[pv]] = pv\n        self.r[nd] = self.l[pv]\n \
    \       if self.r[nd] != -1: self.p[self.r[nd]] = nd\n        self.p[nd] = pv\n\
    \        self.l[pv] = nd\n        if nd == self.root: self.root = pv\n\n    def\
    \ _rotr(self, nd):\n        pv = self.l[nd]\n        self.p[pv] = self.p[nd]\n\
    \        if self.p[pv] != -1:\n            if self.r[self.p[pv]] == nd: self.r[self.p[pv]]\
    \ = pv\n            else: self.l[self.p[pv]] = pv\n        self.l[nd] = self.r[pv]\n\
    \        if self.l[nd] != -1: self.p[self.l[nd]] = nd\n        self.p[nd] = pv\n\
    \        self.r[pv] = nd\n        if nd == self.root: self.root = pv\n\n    def\
    \ remove(self, key):\n        if self.root == -1: return False\n\n        nd =\
    \ self.root\n        while True:\n            if nd == -1: return False\n    \
    \        elif key < self.keys[nd]: nd = self.l[nd]\n            elif key > self.keys[nd]:\
    \ nd = self.r[nd]\n            else: break\n\n        while self.l[nd] != -1 or\
    \ self.r[nd] != -1:\n            if self.l[nd] == -1: self._rotl(nd)\n       \
    \     elif self.r[nd] == -1: self._rotr(nd)\n            elif self.pris[self.l[nd]]\
    \ < self.pris[self.r[nd]]: self._rotr(nd)\n            else: self._rotl(nd)\n\n\
    \        if nd == self.root: self.root = -1\n        elif self.l[self.p[nd]] ==\
    \ nd: self.l[self.p[nd]] = -1\n        else: self.r[self.p[nd]] = -1\n       \
    \ self.stack.append(nd)\n        return True\n\n    def iterate(self, lower):\n\
    \        def dfs(nd):\n            if self.l[nd] != -1 and (self.keys[nd] > lower):\n\
    \                yield from dfs(self.l[nd])\n            if self.keys[nd] >= lower:\n\
    \                yield self.keys[nd]\n            if self.r[nd] != -1:\n     \
    \           yield from dfs(self.r[nd])\n        if self.root != -1:\n        \
    \    yield from dfs(self.root)\n\n    def next_val(self, lower):\n        ret\
    \ = None\n        nd = self.root\n        while nd != -1:\n            if self.keys[nd]\
    \ >= lower:\n                ret = self.keys[nd]\n                nd = self.l[nd]\n\
    \            else: nd = self.r[nd]\n        return ret\n\n    def prev_val(self,\
    \ upper):\n        ret = None\n        nd = self.root\n        while nd != -1:\n\
    \            if self.keys[nd] < upper:\n                ret = self.keys[nd]\n\
    \                nd = self.r[nd]\n            else: nd = self.l[nd]\n        return\
    \ ret\n"
  dependsOn:
  - misc/xorshift.py
  isVerificationFile: false
  path: DataStructure/SortedSet/SortedSetTreap.py
  requiredBy: []
  timestamp: '2021-05-14 22:52:43+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ITP2_7_C.Treap.test.py
documentation_of: DataStructure/SortedSet/SortedSetTreap.py
layout: document
title: "\u9806\u5E8F\u4ED8\u304D\u96C6\u5408 (Treap)"
---

## 概要
Treap による順序付き集合。

## 使い方
`SortedSetTreap()`  
空の順序付き集合を作成する。計算量 $O(1)$

- `__contains__(key: int) -> bool`  
要素 `key` が集合に属しているかどうかを返す。計算量 $\mathrm{expected}\ O(\log N)$

- `__len__() -> int`  
集合の大きさを返す。計算量 $O(1)$

- `__iter__() -> Iterator[int]`  
要素の小さい順のイテレータオブジェクトを返す。イテレーション $1$ 回の計算量 $\mathrm{expected}\ O(\log N)$。全 $N$ 要素のイテレーションの計算量 $O(N)$

- `add(key: int) -> bool`  
要素 `key` を集合に追加する。追加に成功した場合は `True` を、失敗した場合 (既に `key` が集合に属していた場合) は `False` を返す。計算量 $\mathrm{expected}\ O(\log N)$

- `remove(key: int) -> bool`  
集合から `key` を削除する。削除に成功した場合は `True` を、失敗した場合 (`key` が集合に属していなかった場合) は `False` を返す。計算量 $\mathrm{expected}\ O(\log N)$

- `iterate(lower: int) -> Iterator[int]`  
`lower` 以上の要素に対して、小さい順のイテレータオブジェクトを返す。イテレーション $1$ 回の計算量 $\mathrm{expected}\ O(\log N)$。全 $k$ 要素のイテレーションの計算量 $O(k + \log N)$

- `next_val(lower: int) -> int`  
`lower` 以上の最小の要素を返す。そのような要素が存在しない場合は `None` を返す。計算量 $\mathrm{expected}\ O(\log N)$

- `prev_val(upper: int) -> int`  
`upper` よりも小さい最大の要素を返す。そのような要素が存在しない場合は `None` を返す。計算量 $\mathrm{expected}\ O(\log N)$
