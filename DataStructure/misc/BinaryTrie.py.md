---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/set_xor_min.test.py
    title: TestCase/LibraryChecker/set_xor_min.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class BinaryTrieNode:\n    def __init__(self):\n        self.bit0 = None\n\
    \        self.bit1 = None\n        self.size = 0\n\n\nclass BinaryTrie:\n    def\
    \ __init__(self, MAX_BIT_LENGTH=32):\n        self.MAX_BIT_LENGTH = MAX_BIT_LENGTH\n\
    \        self.root = BinaryTrieNode()\n\n    def _generate_bit(self, val):\n \
    \       for i in reversed(range(self.MAX_BIT_LENGTH)):\n            yield (val\
    \ >> i) & 1\n\n    def search(self, val: int) -> bool:\n        ptr = self.root\n\
    \        for bit in self._generate_bit(val):\n            if bit:\n          \
    \      ptr = ptr.bit1\n            else:\n                ptr = ptr.bit0\n   \
    \         if ptr is None:\n                return False\n        return True\n\
    \n    def insert(self, val: int) -> bool:\n        if self.search(val):\n    \
    \        return False\n        ptr = self.root\n        ptr.size += 1\n      \
    \  for bit in self._generate_bit(val):\n            if bit:\n                if\
    \ ptr.bit1 is None:\n                    ptr.bit1 = BinaryTrieNode()\n       \
    \         ptr = ptr.bit1\n            else:\n                if ptr.bit0 is None:\n\
    \                    ptr.bit0 = BinaryTrieNode()\n                ptr = ptr.bit0\n\
    \            ptr.size += 1\n        return True\n\n    def delete(self, val: int)\
    \ -> bool:\n        if not self.search(val):\n            return False\n     \
    \   ptr = self.root\n        ptr.size -= 1\n        for bit in self._generate_bit(val):\n\
    \            if bit:\n                if ptr.bit1.size == 1:\n               \
    \     ptr.bit1 = None\n                    return True\n                ptr =\
    \ ptr.bit1\n            else:\n                if ptr.bit0.size == 1:\n      \
    \              ptr.bit0 = None\n                    return True\n            \
    \    ptr = ptr.bit0\n            ptr.size -= 1\n        return True\n\n    def\
    \ get_xor_min(self, xor_val: int) -> int:\n        ptr = self.root\n        res\
    \ = 0\n        i = self.MAX_BIT_LENGTH\n        for bit in self._generate_bit(xor_val):\n\
    \            i -= 1\n            if bit:\n                if ptr.bit1 is not None:\n\
    \                    ptr = ptr.bit1\n                else:\n                 \
    \   ptr = ptr.bit0\n                    res |= 1 << i\n            else:\n   \
    \             if ptr.bit0 is not None:\n                    ptr = ptr.bit0\n \
    \               else:\n                    ptr = ptr.bit1\n                  \
    \  res |= 1 << i\n        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/misc/BinaryTrie.py
  requiredBy: []
  timestamp: '2021-02-05 19:21:17+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/set_xor_min.test.py
documentation_of: DataStructure/misc/BinaryTrie.py
layout: document
title: Binary Trie
---

## 概要
Trie 構造で非負整数を管理するデータ構造。

## 使い方
`BinaryTrie(MAX_BIT_LENGTH=32)`  
空の集合を構築する。集合に格納できる 2 進数での最大桁数を `MAX_BIT_LENGTH` (これを $\sigma$ とする) で指定する。計算量 $O(1)$

- `search(val: int) -> bool`  
`val` が集合に属しているか返す。計算量 $O(\sigma)$

- `insert(val: int) -> bool`  
集合に `val` を追加する。追加に成功した場合は `True` を、失敗した場合 (既に `val` が集合に属していた場合) は `False` を返す。計算量 $O(\sigma)$

- `delete() -> int`  
集合から `val` を削除する。削除に成功した場合は `True` を、失敗した場合 (`val` が集合に属していなかった場合) は `False` を返す。計算量 $O(\sigma)$

- `get_xor_min(xor_val: int) -> int`  
集合内の要素と `xor_val` との bitwise-xor をとった場合に考えられる最小値を返す。計算量 $O(\sigma)$
