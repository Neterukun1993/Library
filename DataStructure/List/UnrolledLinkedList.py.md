---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/ITP2_1_C.UnrolledLinkedList.test.py
    title: TestCase/AOJ/ITP2_1_C.UnrolledLinkedList.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class ULLNode:\n    MAX_SIZE = 4096\n\n    def __init__(self):\n        self.next\
    \ = None\n        self.list = []\n\n    def is_full(self):\n        return len(self.list)\
    \ == self.MAX_SIZE\n\n\nclass UnrolledLinkedList:\n    def __init__(self):\n \
    \       self.size = 0\n        self.root = ULLNode()\n\n    def __getitem__(self,\
    \ i):\n        nd, i = self._find_node(i)\n        return nd.list[i]\n\n    def\
    \ __setitem__(self, i, val):\n        nd, i = self._find_node(i)\n        nd.list[i]\
    \ = val\n\n    def __len__(self):\n        return self.size\n\n    def _find_node(self,\
    \ i):\n        nd = self.root\n        while i >= len(nd.list):\n            i\
    \ -= len(nd.list)\n            nd = nd.next\n        return nd, i\n\n    def insert(self,\
    \ i, val):\n        nd, i = self._find_node(i - 1)\n        nd.list.insert(i +\
    \ 1, val)\n        self.size += 1\n        if nd.is_full():\n            new =\
    \ ULLNode()\n            new.next = nd.next\n            nd.next = new\n     \
    \       nd.list, new.list = nd.list[:len(nd.list) // 2], nd.list[len(nd.list)\
    \ // 2:]\n\n    def delete(self, i):\n        nd, i = self._find_node(i)\n   \
    \     del nd.list[i]\n        self.size -= 1\n\n    def dump(self):\n        res\
    \ = []\n        nd = self.root\n        while nd is not None:\n            for\
    \ val in nd.list:\n                res.append(val)\n            nd = nd.next\n\
    \        return res\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/List/UnrolledLinkedList.py
  requiredBy: []
  timestamp: '2022-07-31 03:52:21+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/ITP2_1_C.UnrolledLinkedList.test.py
documentation_of: DataStructure/List/UnrolledLinkedList.py
layout: document
title: "\u5BFE\u6570\u6642\u9593\u30E9\u30F3\u30C0\u30E0\u30A2\u30AF\u30BB\u30B9/\u633F\
  \u5165/\u524A\u9664\u53EF\u80FD\u30EA\u30B9\u30C8 (UnrolledLinkedList)"
---

## 概要
要素のランダムアクセスを、挿入、削除を行えるリスト。

## 使い方
`UnrolledLinkedList()`  
空のリストを作成する。計算量 $O(1)$。それぞれのノードに含めることができる最大の要素数を $L(=4096)$ とする。

- `__getitem__(i: int) -> int`  
$i$ 番目の要素を返す。計算量 $O(N/L)$

- `__setitem__(i: int, val: int) -> None`  
$i$ 番目の要素に `val` を代入する。計算量 $O(N/L)$

- `__len__() -> int`  
リストの長さを返す。計算量 $O(1)$

- `insert(i: int, val: int) -> None`  
$i$ 番目の位置に `val` を挿入する。計算量 $O(N/L + L)$

- `delete(i: int) -> None`  
$i$ 番目の要素を削除する。計算量 $O(N/L + L)$

- `dump() -> List[int]`  
リストの要素を列挙した結果を返す。計算量 $O(N)$

## 参考
[Unrolled linked list - Wikipedia](https://ja.wikipedia.org/wiki/Unrolled_linked_list)
