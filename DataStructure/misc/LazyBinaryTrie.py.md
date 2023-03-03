---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ITP2_7_C.LazyBinaryTrie.test.py
    title: TestCase/AOJ/ITP2_7_C.LazyBinaryTrie.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/LazyBinaryTrie.unittest.test.py
    title: TestCase/unittest/LazyBinaryTrie.unittest.test.py
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
  code: "class LazyBinaryTrieNode:\n    def __init__(self):\n        self.bit0 = None\n\
    \        self.bit1 = None\n        self.lazy_val = 0\n        self.size = 0\n\n\
    \nclass LazyBinaryTrie:\n    def __init__(self, MAX_BIT_LENGTH=32):\n        self.MAX_BIT_LENGTH\
    \ = MAX_BIT_LENGTH\n        self.root = LazyBinaryTrieNode()\n\n    def __len__(self):\n\
    \        return self.root.size\n\n    def __contains__(self, val):\n        return\
    \ self._search(val)\n\n    def _propagate(self, ptr, i):\n        lazy_val = ptr.lazy_val\n\
    \        if (lazy_val >> i) & 1: ptr.bit0, ptr.bit1 = ptr.bit1, ptr.bit0\n   \
    \     if ptr.bit0 is not None: ptr.bit0.lazy_val ^= lazy_val\n        if ptr.bit1\
    \ is not None: ptr.bit1.lazy_val ^= lazy_val\n        ptr.lazy_val = 0\n\n   \
    \ def _search(self, val):\n        ptr = self.root\n        for i in reversed(range(self.MAX_BIT_LENGTH)):\n\
    \            self._propagate(ptr, i)\n            if (val >> i) & 1: ptr = ptr.bit1\n\
    \            else: ptr = ptr.bit0\n            if ptr is None: return False\n\
    \        return True\n\n    def add(self, val):\n        if self._search(val):\
    \ return False\n        ptr = self.root\n        ptr.size += 1\n        for i\
    \ in reversed(range(self.MAX_BIT_LENGTH)):\n            if (val >> i) & 1:\n \
    \               if ptr.bit1 is None: ptr.bit1 = LazyBinaryTrieNode()\n       \
    \         ptr = ptr.bit1\n            else:\n                if ptr.bit0 is None:\
    \ ptr.bit0 = LazyBinaryTrieNode()\n                ptr = ptr.bit0\n          \
    \  ptr.size += 1\n        return True\n\n    def remove(self, val):\n        if\
    \ not self._search(val): return False\n        ptr = self.root\n        ptr.size\
    \ -= 1\n        for i in reversed(range(self.MAX_BIT_LENGTH)):\n            if\
    \ (val >> i) & 1:\n                if ptr.bit1.size == 1:\n                  \
    \  ptr.bit1 = None\n                    return True\n                ptr = ptr.bit1\n\
    \            else:\n                if ptr.bit0.size == 1:\n                 \
    \   ptr.bit0 = None\n                    return True\n                ptr = ptr.bit0\n\
    \            ptr.size -= 1\n        return True\n\n    def kth_smallest(self,\
    \ k):\n        ptr = self.root\n        res = 0\n        for i in reversed(range(self.MAX_BIT_LENGTH)):\n\
    \            self._propagate(ptr, i)\n            szl = ptr.bit0.size if ptr.bit0\
    \ is not None else 0\n            if k < szl:\n                ptr = ptr.bit0\n\
    \            else:\n                res |= 1 << i\n                k -= szl\n\
    \                ptr = ptr.bit1\n        return res\n\n    def kth_largest(self,\
    \ k):\n        return self.kth_smallest(self.root.size - k - 1)\n\n    def bisect_left(self,\
    \ lower):\n        ptr = self.root\n        idx = 0\n        for i in reversed(range(self.MAX_BIT_LENGTH)):\n\
    \            if ptr is None: return idx\n            self._propagate(ptr, i)\n\
    \            if (lower >> i) & 1 == 1:\n                idx += ptr.bit0.size if\
    \ ptr.bit0 is not None else 0\n                ptr = ptr.bit1\n            else:\n\
    \                ptr = ptr.bit0\n        return idx\n\n    def bisect_right(self,\
    \ upper):\n        return self.bisect_left(upper + 1)\n\n    def get_xor_min(self,\
    \ val):\n        ptr = self.root\n        res = 0\n        for i in reversed(range(self.MAX_BIT_LENGTH)):\n\
    \            self._propagate(ptr, i)\n            if (val >> i) & 1:\n       \
    \         if ptr.bit1 is not None: ptr = ptr.bit1\n                else:\n   \
    \                 ptr = ptr.bit0\n                    res |= 1 << i\n        \
    \    else:\n                if ptr.bit0 is not None: ptr = ptr.bit0\n        \
    \        else:\n                    ptr = ptr.bit1\n                    res |=\
    \ 1 << i\n        return res\n\n    def all_xor(self, val):\n        self.root.lazy_val\
    \ ^= val\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/misc/LazyBinaryTrie.py
  requiredBy: []
  timestamp: '2021-06-19 15:29:27+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/unittest/LazyBinaryTrie.unittest.test.py
  - TestCase/AOJ/ITP2_7_C.LazyBinaryTrie.test.py
documentation_of: DataStructure/misc/LazyBinaryTrie.py
layout: document
title: "\u9045\u5EF6\u8A55\u4FA1 Binary Trie"
---

## 概要
Trie 構造で非負整数を管理するデータ構造。集合内の全要素に対する xor を行うことができる。

## 使い方
`LazyBinaryTrie(MAX_BIT_LENGTH=32)`  
空の集合を構築する。集合に格納できる 2 進数での最大桁数を `MAX_BIT_LENGTH` (これを $\sigma$ とする) で指定する。計算量 $O(1)$

- `__len__() -> int`  
集合の大きさを返す。計算量 $O(1)$

- `__contains__(val: int) -> bool`  
`val` が集合に属しているか返す。計算量 $O(\sigma)$

- `add(val: int) -> bool`  
集合に `val` を追加する。追加に成功した場合は `True` を、失敗した場合 (既に `val` が集合に属していた場合) は `False` を返す。計算量 $O(\sigma)$

- `remove(val: int) -> int`  
集合から `val` を削除する。削除に成功した場合は `True` を、失敗した場合 (`val` が集合に属していなかった場合) は `False` を返す。計算量 $O(\sigma)$

- `kth_smallest(k: int) -> int`  
集合内で `k` 番目 (0-indexed) に小さい要素を返す。計算量 $O(\sigma)$

- `kth_largest(k: int) -> int`  
集合内で `k` 番目 (0-indexed) に大きい要素を返す。計算量 $O(\sigma)$

- `bisect_left(lower: int) -> int`  
集合内で `lower` 以上の値が現れる最初のインデックスを返す。計算量 $O(\sigma)$

- `bisect_right(upper: int) -> int`  
集合内で `upper` よりも大きい値が現れる最初のインデックスを返す。計算量 $O(\sigma)$

- `get_xor_min(val: int) -> int`  
集合内の要素と `val` との bitwise-xor をとった場合に考えられる最小値を返す。計算量 $O(\sigma)$

- `all_xor(val: int) -> None`  
集合内の全要素に対して `val` の bitwise-xor を行う。計算量 $O(1)$ 
