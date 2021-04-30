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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class PersistentSegmentTree:\n    def __init__(self, n, op, e, root=None):\n\
    \        self.op = op\n        self.e = e\n        self.root = root\n        self.n\
    \ = n\n        self.log = (n - 1).bit_length()\n        self.size = 2 ** self.log\n\
    \n    def build(self, array):\n        array = [(None, None, array[i] if i < self.n\
    \ else self.e) for i in range(self.size)]\n        for h in range(self.log):\n\
    \            tmp = []\n            for i in range(1 << (self.log - h - 1)):\n\
    \                nd = self.make_parent(array[i << 1 | 0], array[i << 1 | 1])\n\
    \                tmp.append(nd)\n            array, tmp = tmp, array\n       \
    \ self.root = array[0]\n\n    def __getitem__(self, i):\n        nd = self.root\n\
    \        for h in range(self.log):\n            if (i >> (self.log - h - 1)) &\
    \ 1:\n                nd = nd[1]\n            else:\n                nd = nd[0]\n\
    \        return nd[2]\n\n    def update(self, i, val):\n        nd = self.root\n\
    \        stack = [nd]\n        for h in range(self.log):\n            if (i >>\
    \ (self.log - h - 1)) & 1:\n                nd = nd[1]\n            else:\n  \
    \              nd = nd[0]\n            stack.append(nd)\n        nd = (None, None,\
    \ val)\n        for ndc, ndp in zip(stack[::-1], stack[::-1][1:]):\n         \
    \   if ndp[0] is ndc:\n                nd = self.make_parent(nd, ndp[1])\n   \
    \         else:\n                nd = self.make_parent(ndp[0], nd)\n        return\
    \ PersistentSegmentTree(self.size, self.op, self.e, nd)\n\n    def make_parent(self,\
    \ ndl, ndr):\n        return (ndl, ndr, self.op(ndl[2], ndr[2]))\n\n    def all_fold(self):\n\
    \        return self.root[2]\n\n    def fold(self, l, r):\n        return self._fold(l,\
    \ r, 0, self.n, self.root)\n\n    def _fold(self, a, b, l, r, nd):\n        if\
    \ r <= a or b <= l:\n            return self.e\n        if a <= l and r <= b:\n\
    \            return nd[2]\n        vl = self._fold(a, b, l, (l + r) >> 1, nd[0])\n\
    \        vr = self._fold(a, b, (l + r) >> 1, r, nd[1])\n        return self.op(vl,\
    \ vr)\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SegmentTree/PersistentSegmentTree.py
  requiredBy: []
  timestamp: '2021-02-14 13:08:01+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/SegmentTree/PersistentSegmentTree.py
layout: document
title: "\u6C38\u7D9A\u30BB\u30B0\u30E1\u30F3\u30C8\u6728"
---

## 概要
Segment Tree を永続化したデータ構造。定数倍が重い。

## 使い方
`PersistentSegmentTree(n: int, op: Callable[[Any, Any], Any], e: Any, root=None)`  
長さ `n` の Persistent Segment Tree を構築する。計算量 $O(1)$

- `build(array: Sequence[Any]) -> None`  
Persistent Segment Tree を `array` で初期化する。計算量 $O(n)$

- `__getitem__(i: int) -> Any`  
`i` 番目の要素を返す。計算量 $O(1)$

- `update(i: int, val: Any) -> PersistentSegmentTree`  
`i` 番目の要素を `val` に更新した Persistent Segment Tree を返す。計算量 $O(\log n)$

- `all_fold() -> Any`  
$[0, n)$ 番目の要素の畳み込み結果を返す。計算量 $O(1)$

- `fold(l: int, r: int) -> Any`  
$[l, r)$ 番目の要素の畳み込み結果を返す。計算量 $O(\log n)$
