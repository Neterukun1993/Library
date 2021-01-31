---
data:
  _extendedDependsOn:
  - icon: ':warning:'
    path: DataStructure/SortedSet/SortedSetBIT.py
    title: "\u9806\u5E8F\u4ED8\u304D\u96C6\u5408 (Binary Indexed Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki0649.SortedMultiSetBIT.test.py
    title: TestCase/yukicoder/yuki0649.SortedMultiSetBIT.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/yukicoder/yuki1110.SortedMultiSetBIT.test.py
    title: TestCase/yukicoder/yuki1110.SortedMultiSetBIT.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.SortedSet.SortedSetBIT import SortedSetBIT\n\n\nclass\
    \ SortedMultiSetBIT(SortedSetBIT):\n    def __init__(self, cands):\n        super().__init__(cands)\n\
    \n    def add(self, val):\n        i = self.comp[val] + 1\n        while i <=\
    \ self.size:\n            self.bit[i] += 1\n            i += i & -i\n        self.cnt\
    \ += 1\n        return True\n"
  dependsOn:
  - DataStructure/SortedSet/SortedSetBIT.py
  isVerificationFile: false
  path: DataStructure/SortedSet/SortedMultiSetBIT.py
  requiredBy: []
  timestamp: '2021-01-30 18:42:14+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/yukicoder/yuki0649.SortedMultiSetBIT.test.py
  - TestCase/yukicoder/yuki1110.SortedMultiSetBIT.test.py
documentation_of: DataStructure/SortedSet/SortedMultiSetBIT.py
layout: document
title: "\u9806\u5E8F\u4ED8\u304D\u591A\u91CD\u96C6\u5408 (Binary Indexed Tree)"
---
## 概要
Binary Indexed Tree による順序付き多重集合。集合に属する可能性のある要素を、あらかじめ与える必要があることに注意。

## 使い方
`SortedMultiSetBIT(cands: Iterable[int])`  
`cands` 内の要素を元として含むことが可能な、空の順序付き多重集合を作成する。`n = len(cands)` とすると、計算量 $O(n \log n)$

- `__contains__(val: int) -> bool`  
要素 `val` が集合に属しているかどうかを返す。計算量 $O(\log n)$

- `__len__() -> int`  
集合の大きさを返す。計算量 $O(1)$

- `add(val: int) -> bool`  
要素 `val` を集合に追加し、`True` を返す。`val` が `cands` の要素ではない場合は例外 `KeyError` が発生するので注意。計算量 $O(\log n)$

- `remove(val: int) -> bool`  
集合から `val` を `1` つだけ削除する。削除に成功した場合は `True` を、失敗した場合 (`val` が集合に属していなかった場合) は `False` を返す。計算量 $O(\log n)$

- `count(vl: int, vr: int) -> int`  
集合内の `vl` 以上かつ `vr` 未満である要素の数を返す。計算量 $O(\log n)$

- `kth_smallest(k: int) -> int`  
集合内で `k` 番目 (0-indexed) に小さい値を返す。計算量 $O(\log n)$

- `kth_largest(k: int) -> int`  
集合内で `k` 番目 (0-indexed) に大きい値を返す。計算量 $O(\log n)$