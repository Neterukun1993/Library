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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def ternary_search_max(l, r, evaluate):\n    EPS = 10 ** (-6)\n    while\
    \ r - l > EPS:\n        midl = l + (r - l) / 3\n        midr = r - (r - l) / 3\n\
    \        if evaluate(midl) < evaluate(midr):\n            l = midl\n        else:\n\
    \            r = midr\n    return l, evaluate(l)\n\n\ndef ternary_search_min(l,\
    \ r, evaluate):\n    EPS = 10 ** (-6)\n    while r - l > EPS:\n        midl =\
    \ l + (r - l) / 3\n        midr = r - (r - l) / 3\n        if evaluate(midl) >\
    \ evaluate(midr):\n            l = midl\n        else:\n            r = midr\n\
    \    return l, evaluate(l)\n\n\ndef ternary_search_intmax(l, r, evaluate):\n \
    \   while (r - l) > 1:\n        mid = (r + l) // 2\n        # \u51F8\u306E\u5DE6\
    \u5074\u306B\u5E73\u5766\u304C\u5B58\u5728\u3059\u308B\u3068\u304D\u306F\u4E0D\
    \u7B49\u53F7\u306B = \u3092\u3064\u3051\u308B\u3002\n        # \u51F8\u306E\u5DE6\
    \u53F3\u306B\u5E73\u5766\u304C\u5B58\u5728\u3059\u308B\u3068\u304D\u306F\u89E3\
    \u3051\u306A\u3044\u3002\n        if evaluate(mid) - evaluate(mid - 1) > 0:\n\
    \            l = mid\n        else:\n            r = mid\n    return l, evaluate(l)\n\
    \n\ndef ternary_search_intmin(l, r, evaluate):\n    while (r - l) > 1:\n     \
    \   mid = (r + l) // 2\n        # \u51F8\u306E\u53F3\u5074\u306B\u5E73\u5766\u304C\
    \u5B58\u5728\u3059\u308B\u3068\u304D\u306F\u4E0D\u7B49\u53F7\u306B = \u3092\u3064\
    \u3051\u308B\u3002\n        # \u51F8\u306E\u5DE6\u53F3\u306B\u5E73\u5766\u304C\
    \u5B58\u5728\u3059\u308B\u3068\u304D\u306F\u89E3\u3051\u306A\u3044\u3002\n   \
    \     if evaluate(mid) - evaluate(mid - 1) < 0:\n            l = mid\n       \
    \ else:\n            r = mid\n    return l, evaluate(l)\n"
  dependsOn: []
  isVerificationFile: false
  path: misc/ternary_search.py
  requiredBy: []
  timestamp: '2021-06-19 15:29:27+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: misc/ternary_search.py
layout: document
title: "\u4E09\u5206\u63A2\u7D22"
---

## 使い方
`ternary_search_max(l: float, r: float, evaluate: Callable[[float], T]) -> Tuple[float, T]`  
$l \le x \lt r$ を満たす実数 $x$ について、上に凸な関数 `evaluate(x)` が最大値となる $x$ とその最大値を返す。計算量 $O(\log(r - l))$

`ternary_search_min(l: float, r: float, evaluate: Callable[[float], Any]) -> Tuple[float, Any]`  
$l \le x \lt r$ を満たす実数 $x$ について、下に凸な関数 `evaluate(x)` が最小値となる $x$ とその最小値を返す。計算量 $O(\log(r - l))$

`ternary_search_intmax(l: int, r: int, evaluate: Callable[[int], Any]) -> Tuple[int, Any]`  
$l \le x \lt r$ を満たす整数 $x$ について、上に凸な関数 `evaluate(x)` が最大値となる $x$ とその最大値を返す。計算量 $O(\log(r - l))$

`ternary_search_intmin(l: int, r: int, evaluate: Callable[[float], Any]) -> Tuple[float, Any]`  
$l \le x \lt r$ を満たす整数 $x$ について、下に凸な関数 `evaluate(x)` が最小値となる $x$ とその最小値を返す。計算量 $O(\log(r - l))$

## 注意
- 誤差に気をつける。[No.306 さいたま2008 - yukicoder](https://yukicoder.me/problems/no/306)

- 関数に平坦な箇所があると、三分探索が正しく行えない場合がある（コードのコメントを参照）。
