---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AtCoder/abc127_f.test.py
    title: TestCase/AtCoder/abc127_f.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# from heapq import heappushpop, heappush\nfrom standard_library.heapq import\
    \ heappushpop, heappush\n\n\nclass DynamicMedian:\n    def __init__(self):\n \
    \       self.l_q = []\n        self.r_q = []\n        self.l_sum = 0\n       \
    \ self.r_sum = 0\n\n    def add(self, val):\n        if len(self.l_q) == len(self.r_q):\n\
    \            self.l_sum += val\n            val = -heappushpop(self.l_q, -val)\n\
    \            self.l_sum -= val\n            heappush(self.r_q, val)\n        \
    \    self.r_sum += val\n        else:\n            self.r_sum += val\n       \
    \     val = heappushpop(self.r_q, val)\n            self.r_sum -= val\n      \
    \      heappush(self.l_q, -val)\n            self.l_sum += val\n\n    def median_low(self):\n\
    \        if len(self.l_q) + 1 == len(self.r_q):\n            return self.r_q[0]\n\
    \        else:\n            return -self.l_q[0]\n\n    def median_high(self):\n\
    \        return self.r_q[0]\n\n    def minimum_query(self):\n        \"\"\"min(|x\
    \ - a_1| + |x - a_2| + \u22EF + |x - a_N|) s.t. any x\"\"\"\n        res1 = (len(self.l_q)\
    \ * self.median_high() - self.l_sum)\n        res2 = (self.r_sum - len(self.r_q)\
    \ * self.median_high())\n        return res1 + res2\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/misc/DynamicMedian.py
  requiredBy: []
  timestamp: '2022-01-22 18:47:07+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AtCoder/abc127_f.test.py
documentation_of: DataStructure/misc/DynamicMedian.py
layout: document
title: "\u52D5\u7684\u4E2D\u592E\u5024\u30AF\u30A8\u30EA"
---
## 概要
DynamicMedian: 集合の中央値を動的に管理するデータ構造

## 使い方
`DynamicMedian()`  
中央値を管理する空の集合を構築する。計算量 $O(1)$

- `add(val: int) -> None`  
集合に要素 `val` を追加する。集合の大きさを `n` とすると、計算量 $O(\log n)$

- `median_low() -> int`  
集合の中央値を返す。ただし、集合の大きさが偶数の場合は中央の2値の小さい方を返す。計算量 $O(1)$

- `median_low() -> int`  
集合の中央値を返す。ただし、集合の大きさが偶数の場合は中央の2値の大きい方を返す。計算量 $O(1)$

- `minimum_query() -> int`  
集合を $\{a_1, a_2, \dots, a_n \}$ としたときの $\min(|x - a_1| + |x - a_2| + ⋯ + |x - a_n|)$ を返す。$x$ は集合の中央値となる。計算量 $O(1)$
