---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ITP2_7_C.ScapegoataTree.test.py
    title: TestCase/AOJ/ITP2_7_C.ScapegoataTree.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import math\n\n\nclass ScapegoatNode:\n    def __init__(self, key):\n   \
    \     self.key = key\n        self.sz = 1\n        self.l, self.r, self.p = None,\
    \ None, None\n\n    def update(self):\n        self.sz = 1\n        if self.l\
    \ is not None: self.sz += self.l.sz\n        if self.r is not None: self.sz +=\
    \ self.r.sz\n\n\nclass SortedSetScapegoatTree:\n    def __init__(self):\n    \
    \    self.root = None\n        self.size = 0\n        self.q = 0\n\n    def __contains__(self,\
    \ key):\n        return self._search(key)\n\n    def __len__(self):\n        return\
    \ self.size\n\n    def __iter__(self):\n        def dfs(nd):\n            if nd.l\
    \ is not None: yield from dfs(nd.l)\n            yield nd.key\n            if\
    \ nd.r is not None: yield from dfs(nd.r)\n\n        if self.root is not None:\n\
    \            yield from dfs(self.root)\n\n    def _log32q(self):\n        return\
    \ math.log(self.q, 1.5)\n\n    def _pack_into_array(self, subroot):\n        def\
    \ dfs(nd):\n            if nd.l is not None: dfs(nd.l)\n            res.append(nd)\n\
    \            if nd.r is not None: dfs(nd.r)\n\n        res = []\n        dfs(subroot)\n\
    \        return res\n\n    def _rebuild(self, subroot):\n        def rec_build(l,\
    \ r):\n            if l == r: return None\n            mid = (l + r) // 2\n  \
    \          ndl = rec_build(l, mid)\n            ndr = rec_build(mid + 1, r)\n\
    \            array[mid].l = ndl\n            array[mid].r = ndr\n            if\
    \ ndl is not None: ndl.p = array[mid]\n            if ndr is not None: ndr.p =\
    \ array[mid]\n            array[mid].update()\n            return array[mid]\n\
    \n        array = self._pack_into_array(subroot)\n        p = subroot.p\n\n  \
    \      if p is None:\n            self.root = rec_build(0, len(array))\n     \
    \       self.root.p = None\n        elif p.r == subroot:\n            p.r = rec_build(0,\
    \ len(array))\n            p.r.p = p\n        else:\n            p.l = rec_build(0,\
    \ len(array))\n            p.l.p = p\n\n    def _search(self, key):\n        nd\
    \ = self.root\n        while nd is not None:\n            if nd.key < key: nd\
    \ = nd.r\n            elif nd.key > key: nd = nd.l\n            else: return True\n\
    \        return False\n\n    def add(self, key):\n        if self.root is None:\n\
    \            self.root = ScapegoatNode(key)\n            self.size += 1\n    \
    \        self.q += 1\n            return True\n\n        nd = self.root\n    \
    \    depth = 0\n        while nd is not None:\n            depth += 1\n      \
    \      if nd.key < key:\n                if nd.r is None:\n                  \
    \  nd.r = ScapegoatNode(key)\n                    nd.r.p = nd\n              \
    \      break\n                nd = nd.r\n            elif nd.key > key:\n    \
    \            if nd.l is None:\n                    nd.l = ScapegoatNode(key)\n\
    \                    nd.l.p = nd\n                    break\n                nd\
    \ = nd.l\n            else: return False\n\n        self.size += 1\n        self.q\
    \ += 1\n        if depth > self._log32q():\n            while 3 * nd.sz <= 2 *\
    \ nd.p.sz:\n                nd = nd.p\n            self._rebuild(nd.p)\n     \
    \   return True\n\n    def remove(self, key):\n        if self.root is None: return\
    \ False\n\n        nd = self.root\n        while nd is not None:\n           \
    \ if nd.key < key: nd = nd.r\n            elif nd.key > key: nd = nd.l\n     \
    \       else: break\n        else: return False\n\n        self.size -= 1\n  \
    \      if nd.l is not None and nd.r is not None:\n            min_nd = nd.r\n\
    \            while min_nd.l is not None:\n                min_nd = min_nd.l\n\
    \            nd.key = min_nd.key\n            nd = min_nd\n\n        chi_nd =\
    \ nd.r if nd.r is not None else nd.l\n        if nd is self.root:\n          \
    \  self.root = chi_nd\n            if self.root is not None: self.root.p = None\n\
    \        elif nd.p.r is nd:\n            nd.p.r = chi_nd\n            if chi_nd\
    \ is not None: chi_nd.p = nd.p\n        else:\n            nd.p.l = chi_nd\n \
    \           if chi_nd is not None: chi_nd.p = nd.p\n\n        if 2 * self.size\
    \ < self.q:\n            if self.root is not None:\n                self._rebuild(self.root)\n\
    \            self.q = self.size\n        return True\n\n    def iterate(self,\
    \ lower):\n        def dfs(nd):\n            if nd.l is not None and (nd.key >\
    \ lower): yield from dfs(nd.l)\n            if nd.key >= lower: yield nd.key\n\
    \            if nd.r is not None: yield from dfs(nd.r)\n\n        if self.root\
    \ is not None:\n            yield from dfs(self.root)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SortedSet/SortedSetScapegoatTree.py
  requiredBy: []
  timestamp: '2021-09-07 23:36:50+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ITP2_7_C.ScapegoataTree.test.py
documentation_of: DataStructure/SortedSet/SortedSetScapegoatTree.py
layout: document
title: "\u9806\u5E8F\u4ED8\u304D\u96C6\u5408 (\u30B9\u30B1\u30FC\u30D7\u30B4\u30FC\
  \u30C8\u6728)"
---

## 概要
スケープゴート木による順序付き集合。[B-Tree](https://neterukun1993.github.io/Library/DataStructure/SortedSet/SortedSetBTree.py) による実装の方が高速なのでそちらを使いましょう。

## 使い方
`SortedSetScapegoatTree()`  
空の順序付き集合を作成する。計算量 $O(1)$

- `__contains__(key: int) -> bool`  
要素 `key` が集合に属しているかどうかを返す。計算量 $O(\log N)$

- `__len__() -> int`  
集合の大きさを返す。計算量 $O(1)$

- `__iter__() -> Iterator[int]`  
要素の小さい順のイテレータオブジェクトを返す。イテレーション $1$ 回の計算量 $O(\log N)$。全 $N$ 要素のイテレーションの計算量 $O(N)$

- `add(key: int) -> bool`  
要素 `key` を集合に追加する。追加に成功した場合は `True` を、失敗した場合 (既に `key` が集合に属していた場合) は `False` を返す。計算量 $\mathrm{amortized}\ O(\log N)$

- `remove(key: int) -> bool`  
集合から `key` を削除する。削除に成功した場合は `True` を、失敗した場合 (`key` が集合に属していなかった場合) は `False` を返す。計算量 $\mathrm{amortized}\ O(\log N)$

- `iterate(lower: int) -> Iterator[int]`  
`lower` 以上の要素に対して、小さい順のイテレータオブジェクトを返す。イテレーション $1$ 回の計算量 $O(\log N)$。全 $k$ 要素のイテレーションの計算量 $O(k + \log N)$
