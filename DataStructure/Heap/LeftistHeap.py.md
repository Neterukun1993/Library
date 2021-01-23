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
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class LHNode:\r\n    def __init__(self, val):\r\n        self.l = None\r\n\
    \        self.r = None\r\n        self.min_dep = 1\r\n        self.val = val\r\
    \n        self.add = 0\r\n\r\n    def lazy_propagate(self):\r\n        if self.l\
    \ is not None: self.l.add += self.add\r\n        if self.r is not None: self.r.add\
    \ += self.add\r\n        self.val += self.add\r\n        self.add = 0\r\n\r\n\r\
    \nclass LeftistHeap:\r\n    def __init__(self):\r\n        self.root = None\r\n\
    \r\n    def _meld(self, a, b):\r\n        if a is None: return b\r\n        if\
    \ b is None: return a\r\n        if b.val + b.add < a.val + a.add: a, b = b, a\r\
    \n        a.lazy_propagate()\r\n        a.r = self._meld(a.r, b)\r\n        if\
    \ a.l is None or a.l.min_dep < a.r.min_dep: a.l, a.r = a.r, a.l\r\n        a.min_dep\
    \ = 1 if a.r is None else a.r.min_dep + 1\r\n        return a\r\n\r\n    @ property\r\
    \n    def min(self):\r\n        self.root.lazy_propagate()\r\n        return self.root.val\r\
    \n\r\n    def push(self, val):\r\n        nd = LHNode(val)\r\n        self.root\
    \ = self._meld(self.root, nd)\r\n\r\n    def pop(self):\r\n        rt = self.root\r\
    \n        rt.lazy_propagate()\r\n        self.root = self._meld(rt.l, rt.r)\r\n\
    \        return rt.val\r\n\r\n    def meld(self, other):\r\n        self.root\
    \ = self._meld(self.root, other.root)\r\n\r\n    def add(self, val):\r\n     \
    \   self.root.add += val\r\n\r\n    def empty(self):\r\n        return self.root\
    \ is None\r\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure\Heap\LeftistHeap.py
  requiredBy: []
  timestamp: '2021-01-18 00:25:59+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure\Heap\LeftistHeap.py
layout: document
title: "\u4F75\u5408\u53EF\u80FD\u30D2\u30FC\u30D7 (Leftist Heap)"
---
## 使い方
`LeftistHeap()`  
空のヒープを作成する。計算量 $\mathrm{O}(1)$
- `min -> Any`  
ヒープ内の最小の値を返す。計算量 $\mathrm{O}(1)$
- `push(val: Any) -> None`  
ヒープに `val` を追加する。計算量 $\mathrm{O}(\log n)$
- `pop() -> Any`  
ヒープ内の最小の値を削除してその値を返す。計算量 $\mathrm{O}(\log n)$
- `meld(other: SkewHeap) -> None`  
ヒープに `other` を併合する。計算量 $\mathrm{O}(\log n)$
- `add(val: Any) -> None`  
ヒープ内のすべての要素に `val` を加算する。計算量 $\mathrm{O}(1)$
- `empty() -> bool`  
ヒープが空かどうかを返す。計算量 $\mathrm{O}(1)$
