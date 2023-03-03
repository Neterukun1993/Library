---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ALDS1_9_C.PairingHeap.test.py
    title: TestCase/AOJ/ALDS1_9_C.PairingHeap.test.py
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
  code: "class PHNode:\n    def __init__(self, val):\n        self.val = val\n   \
    \     self.chi = []\n\n\nclass PairingHeap:\n    def __init__(self):\n       \
    \ self.root = None\n\n    def _meld(self, nd1, nd2):\n        if nd1 is None:\n\
    \            return nd2\n        elif nd2 is None:\n            return nd1\n \
    \       if nd1.val > nd2.val:\n            nd1, nd2 = nd2, nd1\n        nd1.chi.append(nd2)\n\
    \        return nd1\n\n    def _merge_pairs(self, ndlist):\n        newlist =\
    \ []\n        for i in range(len(ndlist) // 2):\n            newlist.append(self._meld(ndlist[i\
    \ * 2], ndlist[i * 2 + 1]))\n        if len(ndlist) % 2 == 0:\n            nd\
    \ = None\n        else:\n            nd = ndlist[-1]\n        for other in newlist:\n\
    \            nd = self._meld(nd, other)\n        return nd\n\n    def empty(self):\n\
    \        return self.root is None\n\n    @property\n    def min(self):\n     \
    \   return self.root.val\n\n    def push(self, val):\n        self.root = self._meld(self.root,\
    \ PHNode(val))\n\n    def pop(self):\n        val = self.root.val\n        self.root\
    \ = self._merge_pairs(self.root.chi)\n        return val\n\n    def meld(self,\
    \ other):\n        self.root = self._meld(self.root, other.root)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/Heap/PairingHeap.py
  requiredBy: []
  timestamp: '2021-09-13 00:09:16+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ALDS1_9_C.PairingHeap.test.py
documentation_of: DataStructure/Heap/PairingHeap.py
layout: document
title: "\u4F75\u5408\u53EF\u80FD\u30D2\u30FC\u30D7 (Pairing Heap)"
---

## 概要
ヒープ同士を計算量 $O(\log N)$ で併合可能なヒープ。

## 使い方
`PairingHeap()`  
空のヒープを作成する。計算量 $O(1)$

- `empty() -> bool`  
ヒープが空かどうかを返す。計算量 $O(1)$

- `min -> int`  
ヒープ内の最小の値を返す。計算量 $O(1)$

- `push(val: int) -> None`  
ヒープに `val` を追加する。計算量 $O(\log N)$

- `pop() -> int`  
ヒープ内の最小の値を削除してその値を返す。計算量 $O(\log N)$

- `meld(other: PairingHeap) -> None`  
ヒープに `other` を併合する。計算量 $O(\log N)$
