---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/deque_operate_all_composite.test.py
    title: TestCase/LibraryChecker/deque_operate_all_composite.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class FoldableDeque:\n    def __init__(self, op):\n        self.op = op\n\
    \        self.front = []\n        self.back = []\n\n    def __len__(self):\n \
    \       return len(self.front) + len(self.back)\n\n    def _trans(self):\n   \
    \     half = len(self) // 2\n        if len(self.front) == 0:\n            stack\
    \ = []\n            while self:\n                stack.append(self.back.pop()[0])\n\
    \            for i in range(half, len(stack)):\n                self.append(stack[i])\n\
    \            for i in reversed(range(0, half)):\n                self.appendleft(stack[i])\n\
    \        else:\n            stack = []\n            while self:\n            \
    \    stack.append(self.front.pop()[0])\n            for i in range(half, len(stack)):\n\
    \                self.appendleft(stack[i])\n            for i in reversed(range(0,\
    \ half)):\n                self.append(stack[i])\n\n    def fold_all(self):\n\
    \        if not self.front:\n            return self.back[-1][1]\n        if not\
    \ self.back:\n            return self.front[-1][1]\n        return self.op(self.back[-1][1],\
    \ self.front[-1][1])\n\n    def append(self, val):\n        if self.front:\n \
    \           self.front.append((val, self.op(self.front[-1][1], val)))\n      \
    \  else:\n            self.front.append((val, val))\n\n    def appendleft(self,\
    \ val):\n        if self.back:\n            self.back.append((val, self.op(val,\
    \ self.back[-1][1])))\n        else:\n            self.back.append((val, val))\n\
    \n    def pop(self):\n        if not self.front:\n            self._trans()\n\
    \        val = self.front.pop()\n        return val[0]\n\n    def popleft(self):\n\
    \        if not self.back:\n            self._trans()\n        val = self.back.pop()\n\
    \        return val[0]\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/misc/FoldableDeque.py
  requiredBy: []
  timestamp: '2022-09-12 01:37:24+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/deque_operate_all_composite.test.py
documentation_of: DataStructure/misc/FoldableDeque.py
layout: document
title: Foldable Deque
---

## 概要
両端キューの操作をサポートし、両端キュー全体の畳み込みを $O(1)$ で行えるデータ構造。畳み込みは半群を要請する。

## 使い方
`FoldableDeque(op: Callable[[Any, Any], Any])`  
空の両端キューを構築する。`op` は畳み込みの二項演算。計算量 $O(1)$

- `__len__() -> int`  
両端キューの大きさを返す。計算量 $O(1)$

- `all_fold() -> Any`  
両端キュー全体の畳み込み結果を返す。計算量 $O(1)$

- `append(val: Any) -> None`  
キューの末尾に要素 `val` を追加する。計算量 $O(1)$

- `append(val: Any) -> None`  
キューの先頭に要素 `val` を追加する。計算量 $O(1)$

- `pop() -> Any`  
キューの末尾要素を削除し、その要素を返す。計算量 $\mathrm{amortized}\ O(1)$

- `popleft() -> Any`  
キューの先頭要素を削除し、その要素を返す。計算量 $\mathrm{amortized}\ O(1)$
