---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/persistent_queue.test.py
    title: TestCase/LibraryChecker/persistent_queue.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class LinkedList:\n\n    class LazyConcatLinkedList:\n        def __init__(self,\
    \ left, right):\n            self.l = left\n            self.r = right\n\n   \
    \     def evaluate(self):\n            l = self.l.pop()\n            return LinkedList.concat(l,\
    \ self.r)\n\n    class LazyReverseLinkedList:\n        def __init__(self, ll):\n\
    \            self.head = ll.head\n            self.tail = ll.tail\n\n        def\
    \ evaluate(self):\n            head, tail = self.head, self.tail\n           \
    \ ret = LinkedList.push(None, head)\n            while tail is not None:\n   \
    \             head, tail = tail.head, tail.tail\n                ret = LinkedList.push(ret,\
    \ head)\n            return ret\n\n    def __init__(self, head=None, tail=None):\n\
    \        self.head = head\n        self.tail = tail\n\n    def top(self):\n  \
    \      return self.head\n\n    def pop(self):\n        if self.tail is not None:\n\
    \            self.tail = self.tail.evaluate()\n        return self.tail\n\n  \
    \  def evaluate(self):\n        return self\n\n    @classmethod\n    def push(cls,\
    \ ll, head):\n        return LinkedList(head, ll)\n\n    @classmethod\n    def\
    \ reverse(cls, ll):\n        return cls.LazyReverseLinkedList(ll)\n\n    @classmethod\n\
    \    def concat(cls, ll_left, ll_right):\n        if ll_left is None:\n      \
    \      return ll_right.evaluate()\n        return LinkedList(ll_left.head,\n \
    \                         cls.LazyConcatLinkedList(ll_left, ll_right))\n\n\nclass\
    \ BankersQueue:\n    def __init__(self, f=None, r=None, fsize=0, rsize=0):\n \
    \       self.f = f\n        self.r = r\n        self.fsize = fsize\n        self.rsize\
    \ = rsize\n\n    def _normalize(self):\n        if self.fsize >= self.rsize:\n\
    \            return self\n        else:\n            lazy_rotate = LinkedList.concat(self.f,\
    \ LinkedList.reverse(self.r))\n            return BankersQueue(lazy_rotate,\n\
    \                                None,\n                                self.fsize\
    \ + self.rsize,\n                                0)\n\n    def front(self):\n\
    \        return self.f.top()\n\n    def push(self, val):\n        return BankersQueue(self.f,\n\
    \                            LinkedList.push(self.r, val),\n                 \
    \           self.fsize,\n                            self.rsize + 1)._normalize()\n\
    \n    def pop(self):\n        return BankersQueue(self.f.pop(),\n            \
    \                self.r,\n                            self.fsize - 1,\n      \
    \                      self.rsize)._normalize()\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/misc/BankersQueue.py
  requiredBy: []
  timestamp: '2021-06-27 18:25:48+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/persistent_queue.test.py
documentation_of: DataStructure/misc/BankersQueue.py
layout: document
title: "\u6C38\u7D9A Queue (Banker's Queue)"
---

## 概要
Queue を永続化したデータ構造。

## 使い方
`BankersQueue()`  
空の Banker's Queue を構築する。計算量 $O(1)$

- `front() -> Any`  
Banker's Queue の先頭の要素を返す。計算量 $O(1)$

- `push(val: Any) -> BankersQueue`  
末尾に要素 `val` を追加した Banker's Queue を返す。計算量 $\mathrm{amortized} O(1)$

- `pop() -> BankersQueue`  
先頭の要素を削除した Banker's Queue を返す。計算量 $\mathrm{amortized} O(1)$

## 参考
[銀行家の Queue (37zigen さん)](https://37zigen.com/bankers-queue/)
