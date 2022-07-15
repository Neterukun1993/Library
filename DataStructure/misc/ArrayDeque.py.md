---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ITP2_1_B.ArrayDeque.test.py
    title: TestCase/AOJ/ITP2_1_B.ArrayDeque.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class ArrayDeque:\n    def __init__(self):\n        self.arr_size = 1\n \
    \       self.array = [0]\n        self.n = 0\n        self.head = 0\n        self.tail\
    \ = 0\n\n    def __len__(self):\n        return self.n\n\n    def __iter__(self):\n\
    \        self._i = 0\n        return self\n\n    def __next__(self):\n       \
    \ if self._i >= self.n:\n            raise StopIteration\n        self._i += 1\n\
    \        return self.array[(self.head + self._i - 1) & (self.arr_size - 1)]\n\n\
    \    def __getitem__(self, i):\n        if i < 0:\n            i = self.n + i\n\
    \        if not (0 <= i < self.n):\n            raise IndexError\n        return\
    \ self.array[(self.head + i) & (self.arr_size - 1)]\n\n    def __setitem__(self,\
    \ i, val):\n        if i < 0:\n            i = self.n + i\n        if not (0 <=\
    \ i < self.n):\n            raise IndexError\n        self.array[(self.head +\
    \ i) & (self.arr_size - 1)] = val\n\n    def _resize(self):\n        new_arr =\
    \ [0] * ((self.n + 1) << 1)\n        for i in range(self.n):\n            new_arr[i]\
    \ = self.array[(self.head + i) & (self.arr_size - 1)]\n        self.array = new_arr\n\
    \        self.arr_size = (self.n + 1) << 1\n        self.head = 0\n        self.tail\
    \ = self.n\n\n    def append(self, val):\n        if self.n == self.arr_size -\
    \ 1:\n            self._resize()\n        self.array[self.tail] = val\n      \
    \  self.tail = (self.tail + 1) & (self.arr_size - 1)\n        self.n += 1\n\n\
    \    def appendleft(self, val):\n        if self.n == self.arr_size - 1:\n   \
    \         self._resize()\n        self.head = (self.head - 1) & (self.arr_size\
    \ - 1)\n        self.array[self.head] = val\n        self.n += 1\n\n    def pop(self):\n\
    \        if self.n == 0:\n            raise IndexError\n        self.tail = (self.tail\
    \ - 1) & (self.arr_size - 1)\n        val = self.array[self.tail]\n        self.n\
    \ -= 1\n        if self.arr_size >= 4 * self.n + 2:\n            self._resize()\n\
    \        return val\n\n    def popleft(self):\n        if self.n == 0:\n     \
    \       raise IndexError\n        val = self.array[self.head]\n        self.head\
    \ = (self.head + 1) & (self.arr_size - 1)\n        self.n -= 1\n        if self.arr_size\
    \ >= 4 * self.n + 2:\n            self._resize()\n        return val\n\n    def\
    \ clear(self):\n        self.__init__()\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/misc/ArrayDeque.py
  requiredBy: []
  timestamp: '2021-02-04 17:47:04+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ITP2_1_B.ArrayDeque.test.py
documentation_of: DataStructure/misc/ArrayDeque.py
layout: document
title: "\u4E21\u7AEF\u30AD\u30E5\u30FC (\u5FAA\u74B0\u30D0\u30C3\u30D5\u30A1/\u30E9\
  \u30F3\u30C0\u30E0\u30A2\u30AF\u30BB\u30B9$O(1)$)"
---

## 概要
ランダムアクセスが $O(1)$ で可能な両端キュー。

## 使い方
`ArrayDeque()`  
空の両端キューを構築する。計算量 $O(1)$

- `__len__() -> int`  
両端キューの大きさを返す。計算量 $O(1)$

- `__iter__() -> Iterator[Any]`  
先頭のイテレータオブジェクトを返す。計算量 $O(1)$

- `__getitem__(i: int) -> Any`  
`i` 番目の要素を返す。計算量 $O(1)$

- `__setitem__(i: int, val: Any) -> None`  
`i` 番目の要素を `val` に変更する。計算量 $O(1)$

- `append(val: Any) -> None`  
両端キューの末尾に要素 `val` を追加する。計算量 $\mathrm{amortized}\ O(1)$

- `appendleft(val: Any) -> None`  
両端キューの先頭に要素 `val` を追加する。計算量 $\mathrm{amortized}\ O(1)$

- `pop() -> Any`  
両端キューの末尾要素を削除し、その要素を返す。計算量 $\mathrm{amortized}\ O(1)$

- `popleft() -> Any`  
両端キューの先頭要素を削除し、その要素を返す。計算量 $\mathrm{amortized}\ O(1)$

- `clear() -> None`  
両端キューを空にする。計算量 $O(1)$
