---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Combination\modinv_combination.py
    title: "MOD\u4E0A\u3067\u306E\u7D44\u5408\u305B\u8A08\u7B97"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DPL_5_A.test.py
    title: TestCase\AOJ\DPL_5_A.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DPL_5_B.test.py
    title: TestCase\AOJ\DPL_5_B.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DPL_5_C.test.py
    title: TestCase\AOJ\DPL_5_C.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DPL_5_D.test.py
    title: TestCase\AOJ\DPL_5_D.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DPL_5_E.test.py
    title: TestCase\AOJ\DPL_5_E.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DPL_5_F.test.py
    title: TestCase\AOJ\DPL_5_F.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DPL_5_G.test.py
    title: TestCase\AOJ\DPL_5_G.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DPL_5_H.test.py
    title: TestCase\AOJ\DPL_5_H.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DPL_5_I.test.py
    title: TestCase\AOJ\DPL_5_I.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DPL_5_J.test.py
    title: TestCase\AOJ\DPL_5_J.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DPL_5_K.test.py
    title: TestCase\AOJ\DPL_5_K.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\DPL_5_L.test.py
    title: TestCase\AOJ\DPL_5_L.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Combination.modinv_combination import Combination\r\n\r\n\r\nMOD = 10\
    \ ** 9 + 7\r\ncomb = Combination(10 ** 6 + 10, MOD)\r\n\r\n\r\ndef way1(ball,\
    \ box):\r\n    \"\"\"ball: True / box: True / constraints: None\r\n    -> ans\
    \ = box ** ball\r\n    \"\"\"\r\n    ans = pow(box, ball, MOD)\r\n    return ans\r\
    \n\r\n\r\ndef way2(ball, box):\r\n    \"\"\"ball: True / box: True / constraints:\
    \ 1 or less\r\n    -> ans = perm(box, ball)\r\n    \"\"\"\r\n    if ball > box:\r\
    \n        return 0\r\n    return comb.perm(box, ball)\r\n\r\n\r\ndef way3(ball,\
    \ box):\r\n    \"\"\"ball: True / box: True / constraints: 1 or more\r\n    ->\
    \ ans = (\u5305\u9664\u539F\u7406)\r\n    \"\"\"\r\n    if ball < box:\r\n   \
    \     return 0\r\n    ans = 0\r\n    for i in range(box + 1):\r\n        ans +=\
    \ pow(-1, i, MOD) * comb.comb(box, i) * pow(box - i, ball, MOD)\r\n        ans\
    \ %= MOD\r\n    return ans\r\n\r\n\r\ndef way4(ball, box):\r\n    \"\"\"ball:\
    \ False / box: True / constraints: None\r\n    -> ans = comb(box + ball - 1, ball)\r\
    \n    \"\"\"\r\n    return comb.comb(ball + box - 1, ball)\r\n\r\n    # \u533A\
    \u5225\u3059\u308Bbox\u500B\u306E\u7BB1 -> \u533A\u5225\u3057\u306A\u3044(box\
    \ - 1)\u500B\u306E\u4ED5\u5207\u306B\u5909\u63DB\u3057\u3066\u89E3\u304F\r\n\r\
    \n\r\ndef way5(ball, box):\r\n    \"\"\"ball: False / box: True / constraints:\
    \ 1 or less\r\n    -> ans = comb(box, ball)\r\n    \"\"\"\r\n    if ball > box:\r\
    \n        return 0\r\n    return comb.comb(box, ball)\r\n\r\n\r\ndef way6(ball,\
    \ box):\r\n    \"\"\"ball: False / box: True / constraints: 1 or more\r\n    ->\
    \ ans = combination(ball - 1, box - 1)\r\n    \"\"\"\r\n    if ball < box:\r\n\
    \        return 0\r\n    return comb.comb(ball - 1, box - 1)\r\n\r\n    # \u8003\
    \u3048\u65B91\r\n    # \u30DC\u30FC\u30EB\u3092\u4E00\u5217\u306B\u4E26\u3079\u305F\
    \u3068\u304D\u3001(ball - 1)\u7B87\u6240\u3042\u308B\u9699\u9593\u304B\u3089\u3001\
    (box - 1)\u500B\u3092\u9078\u3076\r\n\r\n    # \u8003\u3048\u65B92\r\n    # \u3042\
    \u3089\u304B\u3058\u3081\u3001\u3059\u3079\u3066\u306E\u7BB1\u306B\u30DC\u30FC\
    \u30EB\u30921\u3064\u305A\u3064\u914D\u3063\u3066\u304A\u304F\u3068\u3001\r\n\
    \    # \u533A\u5225\u3057\u306A\u3044(ball - box)\u500B\u306E\u30DC\u30FC\u30EB\
    \u3092\u3001\u533A\u5225\u3059\u308Bbox\u500B\u306E\u7BB1\u306B\u914D\u308B\u901A\
    \u308A\u6570\u306B\u5E30\u7740\r\n    # -> way4(ball - box, box) \u3068\u540C\u7B49\
    \u306E\u554F\u984C\u3068\u306A\u308B\r\n\r\n\r\ndef way7(ball, box):\r\n    \"\
    \"\"ball: True / box: False / constraints: None\r\n    -> ans = B(ball, box) B\u306F\
    \u30D9\u30EB\u6570 / \u8A08\u7B97\u91CF O(ball * box)\r\n    \"\"\"\r\n    # B[i][j]\
    \ := S[i][j] + S[i][j - 1] + ... + S[i][0]\r\n    # S[i][j] := i\u500B(\u533A\u5225\
    \u3059\u308B)\u3092k\u30B0\u30EB\u30FC\u30D7(\u533A\u5225\u3057\u306A\u3044)\u306B\
    \u5206\u3051\u308B\u5834\u5408\u306E\u6570\r\n    S = [[0] * (box + 1) for i in\
    \ range(ball + 1)]\r\n    S[0][0] = 1\r\n    for i in range(ball):\r\n       \
    \ for j in range(box):\r\n            S[i + 1][j + 1] = S[i][j] + S[i][j + 1]\
    \ * (j + 1)\r\n            S[i + 1][j + 1] %= MOD\r\n    B_ij = sum(S[ball][0:box\
    \ + 1]) % MOD\r\n    return B_ij\r\n\r\n\r\ndef way8(ball, box):\r\n    \"\"\"\
    ball: True / box: False / constraints: 1 or less\r\n    -> ans = int(\u30DC\u30FC\
    \u30EB\u306E\u6570 <= \u7BB1\u306E\u6570)\r\n    \"\"\"\r\n    return int(ball\
    \ <= box)\r\n\r\n\r\ndef way9(ball, box):\r\n    \"\"\"ball: True / box: False\
    \ / constraints: 1 or more\r\n    -> ans = S(ball, box) S\u306F\u30B9\u30BF\u30FC\
    \u30EA\u30F3\u30B0\u6570 / \u8A08\u7B97\u91CF O(ball * box)\r\n    \"\"\"\r\n\
    \    if ball < box:\r\n        return 0\r\n\r\n    # S[i][j] := i\u500B(\u533A\
    \u5225\u3059\u308B)\u3092k\u30B0\u30EB\u30FC\u30D7(\u533A\u5225\u3057\u306A\u3044\
    )\u306B\u5206\u3051\u308B\u5834\u5408\u306E\u6570\r\n    S = [[0] * (box + 1)\
    \ for i in range(ball + 1)]\r\n    S[0][0] = 1\r\n    for i in range(ball):\r\n\
    \        for j in range(box):\r\n            S[i + 1][j + 1] = S[i][j] + S[i][j\
    \ + 1] * (j + 1)\r\n            S[i + 1][j + 1] %= MOD\r\n    return S[ball][box]\r\
    \n\r\n\r\ndef way10(ball, box):\r\n    \"\"\"ball: False / box: False / constraints:\
    \ None\r\n    ans = P(ball, box) P\u306F\u5206\u5272\u6570 / \u8A08\u7B97\u91CF\
    \ O(ball * box)\r\n    \"\"\"\r\n    # P[i][j] := \u6574\u6570i\u3092\u9806\u5E8F\
    \u3092\u533A\u5225\u305B\u305A\u306B\u300Cj\u4EE5\u4E0B\u306E\u81EA\u7136\u6570\
    \u300D\u306E\u548C\u306B\u5206\u3051\u308B\u5834\u5408\u306E\u6570\r\n    P =\
    \ [[0] * (ball + 1) for _ in range(ball + 1)]\r\n    for j in range(ball + 1):\r\
    \n        P[0][j] = 1\r\n    for i in range(ball):\r\n        for j in range(ball):\r\
    \n            if i - j >= 0:\r\n                P[i + 1][j + 1] = (P[i + 1][j]\
    \ + P[i - j][j + 1]) % MOD\r\n            else:\r\n                P[i + 1][j\
    \ + 1] = P[i + 1][j]\r\n    return P[ball][min(box, ball)]\r\n\r\n\r\ndef way11(ball,\
    \ box):\r\n    \"\"\"ball: False / box: False / constraints: 1 or less\r\n   \
    \ -> ans = int(\u30DC\u30FC\u30EB\u306E\u6570 <= \u7BB1\u306E\u6570)\r\n    \"\
    \"\"\r\n    return int(ball <= box)\r\n\r\n\r\ndef way12(ball, box):\r\n    \"\
    \"\"ball: False / box: False / constraints: 1 or more\r\n    ans = P(ball - box,\
    \ box) P\u306F\u5206\u5272\u6570 / \u8A08\u7B97\u91CF O(ball * box)\r\n    \"\"\
    \"\r\n    if ball < box:\r\n        return 0\r\n\r\n    # P[i][j] := \u6574\u6570\
    i\u3092\u9806\u5E8F\u3092\u533A\u5225\u305B\u305A\u306B\u300Cj\u4EE5\u4E0B\u306E\
    \u81EA\u7136\u6570\u300D\u306E\u548C\u306B\u5206\u3051\u308B\u5834\u5408\u306E\
    \u6570\r\n    diff = ball - box\r\n    P = [[0] * (diff + 1) for _ in range(diff\
    \ + 1)]\r\n    for j in range(diff + 1):\r\n        P[0][j] = 1\r\n    for i in\
    \ range(diff):\r\n        for j in range(diff):\r\n            if i - j >= 0:\r\
    \n                P[i + 1][j + 1] = (P[i + 1][j] + P[i - j][j + 1]) % MOD\r\n\
    \            else:\r\n                P[i + 1][j + 1] = P[i + 1][j]\r\n    return\
    \ P[diff][min(diff, box)]\r\n\r\n    # \u3042\u3089\u304B\u3058\u3081\u3001\u3059\
    \u3079\u3066\u306E\u7BB1\u306B\u30DC\u30FC\u30EB\u30921\u3064\u305A\u3064\u914D\
    \u3063\u3066\u304A\u304F\u3068\r\n    # \u533A\u5225\u3057\u306A\u3044(ball -\
    \ box)\u500B\u306E\u30DC\u30FC\u30EB\u3092\u3001\u533A\u5225\u3057\u306A\u3044\
    box\u500B\u306E\u7BB1\u306B\u914D\u308B\u901A\u308A\u6570\u306B\u5E30\u7740\r\n\
    \    # -> way11(ball - box, box) \u3068\u540C\u7B49\u306E\u554F\u984C\u3068\u306A\
    \u308B\r\n"
  dependsOn:
  - Combination\modinv_combination.py
  isVerificationFile: false
  path: Combination\twelvefold_way.py
  requiredBy: []
  timestamp: '2021-01-06 00:51:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\DPL_5_A.test.py
  - TestCase\AOJ\DPL_5_B.test.py
  - TestCase\AOJ\DPL_5_C.test.py
  - TestCase\AOJ\DPL_5_D.test.py
  - TestCase\AOJ\DPL_5_E.test.py
  - TestCase\AOJ\DPL_5_F.test.py
  - TestCase\AOJ\DPL_5_G.test.py
  - TestCase\AOJ\DPL_5_H.test.py
  - TestCase\AOJ\DPL_5_I.test.py
  - TestCase\AOJ\DPL_5_J.test.py
  - TestCase\AOJ\DPL_5_K.test.py
  - TestCase\AOJ\DPL_5_L.test.py
documentation_of: Combination\twelvefold_way.py
layout: document
title: "\u5199\u50CF12\u76F8"
---
## 概要
ボールを箱に入れるときの場合の数を考える。このとき、ボールの区別 / 箱の区別 / 入れ方の制約 によって12パターンの数え方が存在する。

| ボール | 箱 | 入れ方に制約なし | 箱の中身は１個以下 | 箱の中身は１個以上 |
|----|----|:----:|:----:|:----:|
| 区別できる | 区別できる | `way1` | `way2` | `way3` |
| 区別できない | 区別できる | `way4` | `way5` | `way6` |
| 区別できる | 区別できない | `way7` | `way8` | `way9` |
| 区別できない | 区別できない | `way10` | `way11` | `way12` |

上図は [AOJ Balls and Boxes 1](http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_A&lang=ja) からの出典

## 使い方
`way1(ball: int, box: int) -> int`  
ボールの個数 `ball` と箱の個数 `box` に対して、`way1` での場合の数を返す。

`way2` から `way12` まで同様の方法で使うことができる。ただし、コンテスト中にそのままペタリすることはあまりなく、数え上げ問題で状況整理したいときの確認で使うことが大半かも。
