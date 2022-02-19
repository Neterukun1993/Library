---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_3_A.BootstrappedFoldableQueue.test.py
    title: TestCase/AOJ/DSL_3_A.BootstrappedFoldableQueue.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DSL_3_D.BootstrappedFoldableQueue.test.py
    title: TestCase/AOJ/DSL_3_D.BootstrappedFoldableQueue.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/queue_operate_all_composite.BootstrappedFoldableQueue.test.py
    title: TestCase/LibraryChecker/queue_operate_all_composite.BootstrappedFoldableQueue.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class ListStack:\n    def __init__(self, head=None, tail=None):\n       \
    \ self._head = head\n        self._tail = tail\n\n    def __bool__(self):\n  \
    \      return self._tail is not None\n\n    def __iter__(self):\n        ptr =\
    \ self\n        while ptr:\n            yield ptr.head()\n            ptr = ptr.tail()\n\
    \n    def cons(self, value):\n        return ListStack(value, self)\n\n    def\
    \ head(self):\n        if not self:\n            raise IndexError(\"head from\
    \ empty list\")\n        return self._head\n\n    def tail(self):\n        if\
    \ not self:\n            raise IndexError(\"tail from empty list\")\n        return\
    \ self._tail\n\n    def reverse(self):\n        ret = ListStack()\n        for\
    \ x in self:\n            ret = ret.cons(x)\n        return ret\n\n    def concat(self,\
    \ other):\n        ret = other\n        for x in self.reverse():\n           \
    \ ret = ret.cons(x)\n        return ret\n\n\nclass Suspension:\n    def __init__(self,\
    \ func):\n        self.func = func\n\n    def force(self):\n        if callable(self.func):\n\
    \            self.func = self.func()\n        return self.func\n\n\nclass PhysicistsQueue:\n\
    \    def __init__(self, w=None, fsize=0, f=None, rsize=0, r=None):\n        self.working\
    \ = ListStack() if w is None else w\n        self.fsize = fsize\n        self.f\
    \ = Suspension(lambda: ListStack()) if f is None else f\n        self.rsize =\
    \ rsize\n        self.r = ListStack() if r is None else r\n\n    def __bool__(self):\n\
    \        return self.fsize != 0\n\n    def _checkw(self):\n        if not self.working:\n\
    \            return PhysicistsQueue(self.f.force(), self.fsize, self.f,\n    \
    \                               self.rsize, self.r)\n        else:\n         \
    \   return self\n\n    def _check(self):\n        if self.rsize <= self.fsize:\n\
    \            return self._checkw()\n        f = self.f.force()\n        susp =\
    \ Suspension(lambda: f.concat(self.r.reverse()))\n        return PhysicistsQueue(f,\
    \ self.fsize + self.rsize, susp,\n                               0, ListStack())._checkw()\n\
    \n    def snoc(self, value):\n        return PhysicistsQueue(self.working, self.fsize,\
    \ self.f,\n                               self.rsize + 1, self.r.cons(value))._check()\n\
    \n    def head(self):\n        if not self.working:\n            raise IndexError(\"\
    head from empty queue\")\n        return self.working.head()\n\n    def tail(self):\n\
    \        if not self.working:\n            raise IndexError(\"tail from empty\
    \ queue\")\n        susp = Suspension(lambda: self.f.force().tail())\n       \
    \ return PhysicistsQueue(self.working.tail(), self.fsize - 1, susp,\n        \
    \                       self.rsize, self.r)._check()\n\n\nclass BootstrappedFoldableQueue:\n\
    \    def __init__(self, op,\n                 fmsize=0, f=None, m=None, m_agg=None,\
    \ rsize=0, r=None):\n        self.op = op\n        self.fmsize = fmsize\n    \
    \    self.f = ListStack() if f is None else f\n        self.m = PhysicistsQueue()\
    \ if m is None else m\n        self.m_agg = self if m_agg is None else m_agg\n\
    \        self.rsize = rsize\n        self.r = ListStack() if r is None else r\n\
    \n    def __len__(self):\n        return self.fmsize + self.rsize\n\n    def _check_q(self):\n\
    \        def reverse(list_stack):\n            agg = list_stack.head()[0]\n  \
    \          ret = ListStack().cons((agg, agg))\n            for value, _ in list_stack.tail():\n\
    \                agg = self.op(value, agg)\n                ret = ret.cons((value,\
    \ agg))\n            return ret\n\n        if self.fmsize >= self.rsize:\n   \
    \         return self._check_f()\n        else:\n            susp = Suspension(lambda:\
    \ reverse(self.r))\n            return BootstrappedFoldableQueue(self.op, self.fmsize\
    \ + self.rsize,\n                                             self.f, self.m.snoc(susp),\n\
    \                                             self.m_agg.snoc(self.r.head()[1]),\n\
    \                                             0, ListStack())._check_f()\n\n \
    \   def _check_f(self):\n        if not self.m and not self.f:\n            return\
    \ BootstrappedFoldableQueue(self.op)\n        if not self.f:\n            return\
    \ BootstrappedFoldableQueue(self.op, self.fmsize,\n                          \
    \                   self.m.head().force(),\n                                 \
    \            self.m.tail(), self.m_agg.tail(),\n                             \
    \                self.rsize, self.r)\n        return self\n\n    def all_fold(self):\n\
    \        if not self:\n            raise IndexError(\"fold from empty queue\"\
    )\n        agg = self.f.head()[1]\n        agg = self.op(agg, self.m_agg.all_fold())\
    \ if self.m_agg else agg\n        agg = self.op(agg, self.r.head()[1]) if self.r\
    \ else agg\n        return agg\n\n    def snoc(self, value):\n        if not self:\n\
    \            return BootstrappedFoldableQueue(self.op, 1,\n                  \
    \                           ListStack().cons((value, value)),\n              \
    \                               PhysicistsQueue(), self, 0,\n                \
    \                             ListStack())\n        else:\n            agg = self.op(self.r.head()[1],\
    \ value) if self.r else value\n            elem = (value, agg)\n            return\
    \ BootstrappedFoldableQueue(self.op, self.fmsize, self.f,\n                  \
    \                           self.m, self.m_agg,\n                            \
    \                 self.rsize + 1,\n                                          \
    \   self.r.cons(elem))._check_q()\n\n    def head(self):\n        if not self:\n\
    \            raise IndexError(\"head from empty queue\")\n        return self.f.head()[0]\n\
    \n    def tail(self):\n        if not self:\n            raise IndexError(\"tail\
    \ from empty queue\")\n        return BootstrappedFoldableQueue(self.op, self.fmsize\
    \ - 1,\n                                         self.f.tail(), self.m, self.m_agg,\n\
    \                                         self.rsize, self.r)._check_q()\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/misc/BootstrappedFoldableQueue.py
  requiredBy: []
  timestamp: '2022-02-20 01:21:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/queue_operate_all_composite.BootstrappedFoldableQueue.test.py
  - TestCase/AOJ/DSL_3_A.BootstrappedFoldableQueue.test.py
  - TestCase/AOJ/DSL_3_D.BootstrappedFoldableQueue.test.py
documentation_of: DataStructure/misc/BootstrappedFoldableQueue.py
layout: document
title: "\u6C38\u7D9A Sliding Window Aggregation"
---

## 概要
Sliding Window Aggregation を永続化したデータ構造。

## 使い方
`BootstrappedFoldableQueue[T](op: Callable[[T, T], T])`  
空のキューを構築する。`op` は畳み込みの二項演算。計算量 $O(1)$

- `__len__() -> int`  
キューの大きさを返す。計算量 $O(1)$

- `all_fold() -> T`  
キュー全体の畳み込み結果を返す。計算量 $O(1)$

- `snoc(val: T) -> BootstrappedFoldableQueue[T]`  
キューの末尾に要素 `val` を追加する。計算量 $O(1)$

- `head() -> T`  
キューの先頭の要素を返す。計算量 $O(1)$

- `tail() -> BootstrappedFoldableQueue[T]`  
キューの先頭要素を削除したキューを返す。計算量 $\mathrm{amortized}\ O(1)$
