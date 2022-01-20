---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: Graph/misc/k_shortest_walk.py
    title: "\u4E0A\u4F4D $k$ \u500B\u306E\u30A6\u30A9\u30FC\u30AF"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_9_C.PersistentLeftistHeap.test.py
    title: TestCase/AOJ/ALDS1_9_C.PersistentLeftistHeap.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class LeftistHeap:\n    E = None\n\n    def __new__(cls, *args):\n      \
    \  if cls.E is None:\n            cls.E = super().__new__(cls)\n        return\
    \ super().__new__(cls) if args else cls.E\n\n    def __init__(self, rank=0, key=None,\
    \ value=None, a=None, b=None):\n        self.rank = rank\n        self.key = key\n\
    \        self.value = value\n        self.a = a\n        self.b = b\n\n    def\
    \ __bool__(self):\n        return self is not LeftistHeap.E\n\n    def __lt__(self,\
    \ other):\n        return self.key < other.key\n\n    @staticmethod\n    def _make(key,\
    \ value, a, b):\n        if a.rank >= b.rank:\n            a, b = b, a\n     \
    \   return LeftistHeap(a.rank + 1, key, value, b, a)\n\n    @staticmethod\n  \
    \  def merge(hl, hr):\n        if not hl:\n            return hr\n        elif\
    \ not hr:\n            return hl\n        elif hl.key <= hr.key:\n           \
    \ return LeftistHeap._make(hl.key, hl.value, hl.a,\n                         \
    \            LeftistHeap.merge(hl.b, hr))\n        else:\n            return LeftistHeap._make(hr.key,\
    \ hr.value, hr.a,\n                                     LeftistHeap.merge(hl,\
    \ hr.b))\n\n    def insert(self, key, value):\n        new = LeftistHeap(1, key,\
    \ value, LeftistHeap.E, LeftistHeap.E)\n        return LeftistHeap.merge(new,\
    \ self)\n\n    @property\n    def find_min(self):\n        if self is LeftistHeap.E:\n\
    \            raise IndexError(\"find from empty heap\")\n        return self.key,\
    \ self.value\n\n    def delete_min(self):\n        if self is LeftistHeap.E:\n\
    \            raise IndexError(\"delete from empty heap\")\n        return self.merge(self.a,\
    \ self.b)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/Heap/PersistentLeftistHeap.py
  requiredBy:
  - Graph/misc/k_shortest_walk.py
  timestamp: '2022-01-20 19:40:17+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_9_C.PersistentLeftistHeap.test.py
documentation_of: DataStructure/Heap/PersistentLeftistHeap.py
layout: document
title: "\u4F75\u5408\u53EF\u80FD\u6C38\u7D9A\u30D2\u30FC\u30D7 (Persistent Leftist\
  \ Heap)"
---

## 概要
大きさが $N$ と $M$ のヒープ同士を計算量 $O(\log (N+M))$ で併合可能な永続ヒープ。ヒープの要素は (キー, 値) の組み合わせで表現され、キーの小さい要素が優先度が高い。キーは重複を許す。

## 使い方
`LeftistHeap()`  
空のヒープを作成する。計算量 $O(1)$

- `__bool__() -> bool`  
ヒープが空かどうか返す。計算量 $O(1)$

- `__lt__(other: LeftistHeap) -> bool`  
ヒープ同士をキーの値で比較し、`other` よりも小さければ `True` を返す。そうでなければ `False` を返す。計算量 $O(1)$

- `insert(key: int, val: int) -> LeftistHeap`  
ヒープに (キー、 値) の組を持つ要素を追加したときのヒープを返す。ヒープの大きさを $N$ とすると、計算量 $O(\log N)$

- `find_min -> Tuple[int, int]`  
ヒープ内の最小のキーを持つ要素の (キー, 値) の組を返す。計算量 $O(1)$

- `delete_min() -> LeftistHeap`  
ヒープ内の最小のキーを持つ要素を $1$ つ削除したときのヒープを返す。ヒープの大きさを $N$ とすると、計算量 $O(\log N)$

`LeftistHeap.merge(hl: LeftistHeap, hr: LeftistHeap) -> LeftistHeap`  
ヒープ `hl` と `hr` を併合したときのヒープを返す。それぞれのヒープの大きさを $N, M$ とすると、計算量 $O(\log(N+M))$
