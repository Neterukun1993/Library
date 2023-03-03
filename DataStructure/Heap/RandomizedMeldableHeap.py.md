---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: misc/xorshift.py
    title: "\u4E71\u6570\u751F\u6210 (Xorshift)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_9_C.RandomizedMeldableHeap.test.py
    title: TestCase/AOJ/ALDS1_9_C.RandomizedMeldableHeap.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from misc.xorshift import xorshift32\n\n\nrand32 = xorshift32()\n\n\nclass\
    \ RMHNode:\n    def __init__(self, val):\n        self.l = None\n        self.r\
    \ = None\n        self.val = val\n\n\nclass RandomizedMeldableHeap:\n    def __init__(self):\n\
    \        self.root = None\n\n    def _meld(self, a, b):\n        if a is None:\
    \ return b\n        if b is None: return a\n        if b.val < a.val: a, b = b,\
    \ a\n        if rand32() & 1:\n            a.l = self._meld(a.l, b)\n        else:\n\
    \            a.r = self._meld(a.r, b)\n        return a\n\n    @ property\n  \
    \  def min(self):\n        return self.root.val\n\n    def push(self, val):\n\
    \        nd = RMHNode(val)\n        self.root = self._meld(self.root, nd)\n\n\
    \    def pop(self):\n        rt = self.root\n        self.root = self._meld(rt.l,\
    \ rt.r)\n        return rt.val\n\n    def meld(self, other):\n        self.root\
    \ = self._meld(self.root, other.root)\n\n    def empty(self):\n        return\
    \ self.root is None\n"
  dependsOn:
  - misc/xorshift.py
  isVerificationFile: false
  path: DataStructure/Heap/RandomizedMeldableHeap.py
  requiredBy: []
  timestamp: '2021-01-19 22:36:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_9_C.RandomizedMeldableHeap.test.py
documentation_of: DataStructure/Heap/RandomizedMeldableHeap.py
layout: document
title: "\u4F75\u5408\u53EF\u80FD\u30D2\u30FC\u30D7 (Randomized Meldable Heap)"
---
## 概要
ヒープ同士を計算量 $O(\log N)$ で併合可能なヒープ。

## 使い方
`LeftistHeap()`  
空のヒープを作成する。計算量 $O(1)$

- `min -> int`  
ヒープ内の最小の値を返す。計算量 $O(1)$

- `push(val: int) -> None`  
ヒープに `val` を追加する。計算量 $\mathrm{expected}\ O(\log N)$

- `pop() -> int`  
ヒープ内の最小の値を削除してその値を返す。計算量 $\mathrm{expected}\ O(\log N)$

- `meld(other: RandomizedMeldableHeap) -> None`  
ヒープに `other` を併合する。計算量 $\mathrm{expected}\ O(\log N)$

- `empty() -> bool`  
ヒープが空かどうかを返す。計算量 $O(1)$
