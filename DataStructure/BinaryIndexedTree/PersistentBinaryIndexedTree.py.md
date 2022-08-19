---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class PersistentBinaryIndexedTree:\n    def __init__(self, n, root=None):\n\
    \        self.root = root\n        self.n = n\n        self.size = 1 << n.bit_length()\n\
    \n    def build(self, array):\n        n = len(array)\n        bit = [[None, None,\
    \ array[i - 1] if 0 <= i - 1 < n else 0] for i in range(self.size)]\n        for\
    \ i in range(1, self.size):\n            if i + (i & -i) < self.size:\n      \
    \          bit[i + (i & -i)][2] += bit[i][2]\n        bit[0] = tuple(bit[0])\n\
    \        for k in range(self.size.bit_length() - 1):\n            for i in range(1\
    \ << k, self.size, 1 << (k + 1)):\n                if k == 0:\n              \
    \      bit[i] = tuple(bit[i])\n                else:\n                    l, r\
    \ = i - (1 << (k - 1)), i + (1 << (k - 1))\n                    bit[i][0], bit[i][1]\
    \ = bit[l], bit[r]\n                    bit[i] = tuple(bit[i])\n        self.root\
    \ = bit[self.size >> 1]\n\n    def _sum(self, i):\n        s = 0\n        nd =\
    \ self.root\n        idx = self.size >> 1\n        for h in reversed(range(self.size.bit_length()\
    \ - 2)):\n            if i < idx:\n                nd = nd[0]\n              \
    \  idx -= 1 << h\n            else:\n                s += nd[2]\n            \
    \    nd = nd[1]\n                idx += 1 << h\n        if i >= idx:\n       \
    \     s += nd[2]\n        return s\n\n    def _add_rec(self, i, idx, diff, val,\
    \ nd):\n        if i == idx:\n            return (nd[0], nd[1], nd[2] + val)\n\
    \        elif i < idx:\n            ndl = self._add_rec(i, idx - diff, diff >>\
    \ 1, val, nd[0])\n            if idx - (idx & (-idx)) < i:\n                return\
    \ (ndl, nd[1], nd[2] + val)\n            return (ndl, nd[1], nd[2])\n        else:\n\
    \            ndr = self._add_rec(i, idx + diff, diff >> 1, val, nd[1])\n     \
    \       return (nd[0], ndr, nd[2])\n\n    def sum(self, l, r):\n        return\
    \ self._sum(r) - self._sum(l)\n\n    def add(self, i, val):\n        i += 1\n\
    \        idx = self.size >> 1\n        root = self._add_rec(i, idx, idx >> 1,\
    \ val, self.root)\n        return PersistentBinaryIndexedTree(self.n, root)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/BinaryIndexedTree/PersistentBinaryIndexedTree.py
  requiredBy: []
  timestamp: '2021-02-14 13:08:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/BinaryIndexedTree/PersistentBinaryIndexedTree.py
layout: document
title: "\u6C38\u7D9ABinary Indexed Tree"
---

## 概要
Binary Indexed Tree を永続化したデータ構造。定数倍が重い。

## 使い方
`PersistentBinaryIndexedTree(n: int, root=None)`  
長さ $n$ の Persistent Binary Indexed Tree を構築する。計算量 $O(1)$

- `build(array: Sequence[int]) -> None`  
Persistent Binary Indexed Tree を `array` で初期化する。`add` や `sum` を実行出す前に、必ず `build` しておくこと。たとえ全ての要素が $0$ である場合も、`[0] * n` を与えて `build` しておくこと。計算量 $O(n)$

- `add(i: int, val: int) -> PersistentBinaryIndexedTree`  
$i$ 番目の要素に `val` を加えた Persistent Binry Indexed Tree を返す。計算量 $O(\log n)$

- `sum(l: int, r: int) -> int`  
$\lbrack l, r)$ 番目の要素の総和を返す。計算量 $O(\log n)$
