---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "class AccumulateSumLR:\n    def __init__(self, array, op, e):\n        self.op\
    \ = op\n        self.e = e\n        n = len(array)\n        self.left = [self.e]\
    \ * (n + 1)\n        self.right = [self.e] * (n + 1)\n        for i in range(n):\n\
    \            self.left[i + 1] = self.op(self.left[i], array[i])\n        for i\
    \ in reversed(range(n)):\n            self.right[i] = self.op(self.right[i + 1],\
    \ array[i])\n\n    def left_fold(self, upper):\n        \"\"\"fold of [0, upper)\"\
    \"\"\n        return self.left[upper]\n\n    def right_fold(self, lower):\n  \
    \      \"\"\"fold of [lower, n)\"\"\"\n        return self.right[lower]\n\n  \
    \  def fold(self, ex_idx):\n        \"\"\"fold all of the elements except for\
    \ array[ex_idx]\"\"\"\n        return self.op(self.left[ex_idx], self.right[ex_idx\
    \ + 1])\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/AccumulateSum/AccumulateSumLR.py
  requiredBy: []
  timestamp: '2021-01-04 02:54:49+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: DataStructure/AccumulateSum/AccumulateSumLR.py
layout: document
title: "\u5DE6\u53F3\u304B\u3089\u306E\u7D2F\u7A4D\u548C"
---
## 使い方
`AccumulateSumLR(array: List[Any], op: Callable[[Any, Any], Any], e: Any)`  
`array` の累積和を構築する。このときの累積は二項演算 `op`、単位元 `e` によって演算される。`array` のサイズを $n$ としたとき、計算量 $\mathrm{O}(n)$
- `left_fold(upper: int) -> Any`  
$\lbrack 0, upper)$ 番目の要素の累積を返す。計算量 $\mathrm{O}(1)$
- `right_fold(upper: int) -> Any`  
$\lbrack lower, n)$ 番目の要素の累積を返す。計算量 $\mathrm{O}(1)$
- `fold(ex_idx: int) -> Any`  
$ex\_idx$ 番目を除いたすべての要素の累積を返す。計算量 $\mathrm{O}(1)$
