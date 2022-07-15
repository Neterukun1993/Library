---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/unittest/substring_dp.unittest.test.py
    title: TestCase/unittest/substring_dp.unittest.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def calc_next(small_characters):\n    n = len(small_characters)\n    nxt\
    \ = [[-1] * 26 for i in range(n + 1)]\n\n    for i in reversed(range(n)):\n  \
    \      for val in range(26):\n            if val == ord(small_characters[i]) -\
    \ 97:\n                nxt[i][val] = i + 1\n            else:\n              \
    \  nxt[i][val] = nxt[i + 1][val]\n    return nxt\n\n\ndef substring_dp(small_characters,\
    \ MOD):\n    n = len(small_characters)\n    nxt = calc_next(small_characters)\n\
    \    dp = [0] * (n + 1)\n    dp[0] = 1\n\n    for i in range(n):\n        for\
    \ val in range(26):\n            if nxt[i][val] == -1:\n                continue\n\
    \            dp[nxt[i][val]] += dp[i]\n            dp[nxt[i][val]] %= MOD\n\n\
    \    ans = 0\n    for i in range(n + 1):  # \u7A7A\u6587\u5B57 (i = 0 \u306E\u3068\
    \u304D) \u3082\u542B\u3081\u308B\u3002\n        ans += dp[i]\n        ans %= MOD\n\
    \    return ans\n"
  dependsOn: []
  isVerificationFile: false
  path: DP/substring_dp.py
  requiredBy: []
  timestamp: '2021-05-09 19:23:25+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/unittest/substring_dp.unittest.test.py
documentation_of: DP/substring_dp.py
layout: document
title: "\u90E8\u5206\u5217 DP"
---

## 概要
小文字英字列 $S$ に対して部分列の通り数を求めるアルゴリズム。$\mathrm{nxt}$ 配列を使うことで数え上げの重複を防ぐのがポイント。

#### $\mathrm{nxt}$ 配列定義  
$\mathrm{nxt}[i][j] :=$ $S$ の $i$ 文字目以降で初めて $\mathrm{chr}(j + 97)$ が登場するときのインデックス (すべて $1$-indexed)

#### 状態遷移  
状態を $\mathrm{dp}[i] :=$ $S$ の部分列で $i$ 文字目を最後に使用するときの通り数、とする。このときの遷移式は以下の通りとなる。

$\left\{\begin{array}{l}
\mathrm{dp}[0] = 1\\
\mathrm{dp}[\mathrm{nxt}[i][j]]\mathrel{+}=dp[i]
\end{array}\right.$

## 使い方
- `calc_next(small_characters: Sequence) -> List[List[int]]`  
長さ $N$、文字種類数 $\sigma = 26$ の小文字英字列 `small_characters` について、 $\mathrm{nxt}$ 配列を返す。計算量 $O(\sigma N)$

- `substring_dp(small_characters: Sequence, MOD: int) -> int`  
長さ $N$、文字種類数 $\sigma = 26$ の小文字英字列 `small_characters` について、部分列の通り数を $\mathrm{MOD}$ で割った余りを返す。計算量 $O(\sigma N)$

## 参考
[部分列 DP --- 文字列の部分文字列を重複なく走査する DP の特集](https://qiita.com/drken/items/a207e5ae3ea2cf17f4bd)
