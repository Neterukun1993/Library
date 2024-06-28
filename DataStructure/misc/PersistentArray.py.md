---
data:
  _extendedDependsOn: []
  _extendedRequiredBy:
  - icon: ':heavy_check_mark:'
    path: DataStructure/UnionFind/PersistentUnionFind.py
    title: "\u6C38\u7D9A Union Find"
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/PersistentArray.unittest.test.py
    title: TestCase/unittest/PersistentArray.unittest.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class PersistentArray:\n    LOG = 4\n    MASK = (1 << LOG) - 1\n\n    def\
    \ __init__(self,):\n        self.val = None\n        self.ch = [None] * (1 <<\
    \ self.LOG)\n\n    def set(self, i, val):\n        pa = PersistentArray()\n  \
    \      pa.val = self.val\n        pa.ch = self.ch[:]\n        if i == 0:\n   \
    \         pa.val = val\n        else:\n            pa.ch[i & self.MASK] = pa.ch[i\
    \ & self.MASK].set(i >> self.LOG, val)\n        return pa\n\n    def get(self,\
    \ i):\n        pa = self\n        while i != 0:\n            pa = pa.ch[i & self.MASK]\n\
    \            i = i >> self.LOG\n        return pa.val\n\n\ndef init_persistent_array(array):\n\
    \    LOG = 4\n    MASK = (1 << LOG) - 1\n\n    def init_set(i, val, pa):\n   \
    \     if pa is None:\n            pa = PersistentArray()\n        if i == 0:\n\
    \            pa.val = val\n        else:\n            pa.ch[i & MASK] = init_set(i\
    \ >> LOG, val, pa.ch[i & MASK])\n        return pa\n\n    pa = None\n    for i,\
    \ val in enumerate(array):\n        pa = init_set(i, val, pa)\n    return pa\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/misc/PersistentArray.py
  requiredBy:
  - DataStructure/UnionFind/PersistentUnionFind.py
  timestamp: '2021-07-18 20:19:20+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/unittest/PersistentArray.unittest.test.py
documentation_of: DataStructure/misc/PersistentArray.py
layout: document
title: "\u6C38\u7D9A\u914D\u5217"
---

## 概要
永続化された配列。つまり、代入操作前と後のバージョンを常に保持し、全バージョンに対するアクセスと更新が可能な配列。

## 使い方
`init_persistent_array(array: Sequence[Any]) -> PersistentArray`  
長さ $n$ の配列 `array` の永続配列を返す。計算量 $O(n \log n)$

永続配列のメソッド `set` と `get` によって、全バージョンに対するアクセスと更新が可能。

- `set(i: int, val: Any) -> PersistentArray`  
$i$ 番目の要素に `val` を代入した永続配列を返す。計算量 $O(\log n)$

- `get(i: int) -> Any`  
$i$ 番目の要素を返す。計算量 $O(\log n)$
