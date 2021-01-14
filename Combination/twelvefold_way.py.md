---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Combination/modinv_combination.py
    title: "MOD\u4E0A\u3067\u306E\u7D44\u5408\u305B\u8A08\u7B97"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_5_A.test.py
    title: TestCase/AOJ/DPL_5_A.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_5_B.test.py
    title: TestCase/AOJ/DPL_5_B.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_5_C.test.py
    title: TestCase/AOJ/DPL_5_C.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_5_D.test.py
    title: TestCase/AOJ/DPL_5_D.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_5_E.test.py
    title: TestCase/AOJ/DPL_5_E.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_5_F.test.py
    title: TestCase/AOJ/DPL_5_F.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_5_G.test.py
    title: TestCase/AOJ/DPL_5_G.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_5_H.test.py
    title: TestCase/AOJ/DPL_5_H.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_5_I.test.py
    title: TestCase/AOJ/DPL_5_I.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_5_J.test.py
    title: TestCase/AOJ/DPL_5_J.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_5_K.test.py
    title: TestCase/AOJ/DPL_5_K.test.py
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_5_L.test.py
    title: TestCase/AOJ/DPL_5_L.test.py
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.8.7/x64/lib/python3.8/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.8.7/x64/lib/python3.8/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from Combination.modinv_combination import Combination\n\n\nMOD = 10 ** 9\
    \ + 7\ncomb = Combination(10 ** 6 + 10, MOD)\n\n\ndef way1(ball, box):\n    \"\
    \"\"ball: True / box: True / constraints: None\n    -> ans = box ** ball\n   \
    \ \"\"\"\n    ans = pow(box, ball, MOD)\n    return ans\n\n\ndef way2(ball, box):\n\
    \    \"\"\"ball: True / box: True / constraints: 1 or less\n    -> ans = perm(box,\
    \ ball)\n    \"\"\"\n    if ball > box:\n        return 0\n    return comb.perm(box,\
    \ ball)\n\n\ndef way3(ball, box):\n    \"\"\"ball: True / box: True / constraints:\
    \ 1 or more\n    -> ans = (\u5305\u9664\u539F\u7406)\n    \"\"\"\n    if ball\
    \ < box:\n        return 0\n    ans = 0\n    for i in range(box + 1):\n      \
    \  ans += pow(-1, i, MOD) * comb.comb(box, i) * pow(box - i, ball, MOD)\n    \
    \    ans %= MOD\n    return ans\n\n\ndef way4(ball, box):\n    \"\"\"ball: False\
    \ / box: True / constraints: None\n    -> ans = comb(box + ball - 1, ball)\n \
    \   \"\"\"\n    return comb.comb(ball + box - 1, ball)\n\n    # \u533A\u5225\u3059\
    \u308Bbox\u500B\u306E\u7BB1 -> \u533A\u5225\u3057\u306A\u3044(box - 1)\u500B\u306E\
    \u4ED5\u5207\u306B\u5909\u63DB\u3057\u3066\u89E3\u304F\n\n\ndef way5(ball, box):\n\
    \    \"\"\"ball: False / box: True / constraints: 1 or less\n    -> ans = comb(box,\
    \ ball)\n    \"\"\"\n    if ball > box:\n        return 0\n    return comb.comb(box,\
    \ ball)\n\n\ndef way6(ball, box):\n    \"\"\"ball: False / box: True / constraints:\
    \ 1 or more\n    -> ans = combination(ball - 1, box - 1)\n    \"\"\"\n    if ball\
    \ < box:\n        return 0\n    return comb.comb(ball - 1, box - 1)\n\n    # \u8003\
    \u3048\u65B91\n    # \u30DC\u30FC\u30EB\u3092\u4E00\u5217\u306B\u4E26\u3079\u305F\
    \u3068\u304D\u3001(ball - 1)\u7B87\u6240\u3042\u308B\u9699\u9593\u304B\u3089\u3001\
    (box - 1)\u500B\u3092\u9078\u3076\n\n    # \u8003\u3048\u65B92\n    # \u3042\u3089\
    \u304B\u3058\u3081\u3001\u3059\u3079\u3066\u306E\u7BB1\u306B\u30DC\u30FC\u30EB\
    \u30921\u3064\u305A\u3064\u914D\u3063\u3066\u304A\u304F\u3068\u3001\n    # \u533A\
    \u5225\u3057\u306A\u3044(ball - box)\u500B\u306E\u30DC\u30FC\u30EB\u3092\u3001\
    \u533A\u5225\u3059\u308Bbox\u500B\u306E\u7BB1\u306B\u914D\u308B\u901A\u308A\u6570\
    \u306B\u5E30\u7740\n    # -> way4(ball - box, box) \u3068\u540C\u7B49\u306E\u554F\
    \u984C\u3068\u306A\u308B\n\n\ndef way7(ball, box):\n    \"\"\"ball: True / box:\
    \ False / constraints: None\n    -> ans = B(ball, box) B\u306F\u30D9\u30EB\u6570\
    \ / \u8A08\u7B97\u91CF O(ball * box)\n    \"\"\"\n    # B[i][j] := S[i][j] + S[i][j\
    \ - 1] + ... + S[i][0]\n    # S[i][j] := i\u500B(\u533A\u5225\u3059\u308B)\u3092\
    k\u30B0\u30EB\u30FC\u30D7(\u533A\u5225\u3057\u306A\u3044)\u306B\u5206\u3051\u308B\
    \u5834\u5408\u306E\u6570\n    S = [[0] * (box + 1) for i in range(ball + 1)]\n\
    \    S[0][0] = 1\n    for i in range(ball):\n        for j in range(box):\n  \
    \          S[i + 1][j + 1] = S[i][j] + S[i][j + 1] * (j + 1)\n            S[i\
    \ + 1][j + 1] %= MOD\n    B_ij = sum(S[ball][0:box + 1]) % MOD\n    return B_ij\n\
    \n\ndef way8(ball, box):\n    \"\"\"ball: True / box: False / constraints: 1 or\
    \ less\n    -> ans = int(\u30DC\u30FC\u30EB\u306E\u6570 <= \u7BB1\u306E\u6570\
    )\n    \"\"\"\n    return int(ball <= box)\n\n\ndef way9(ball, box):\n    \"\"\
    \"ball: True / box: False / constraints: 1 or more\n    -> ans = S(ball, box)\
    \ S\u306F\u30B9\u30BF\u30FC\u30EA\u30F3\u30B0\u6570 / \u8A08\u7B97\u91CF O(ball\
    \ * box)\n    \"\"\"\n    if ball < box:\n        return 0\n\n    # S[i][j] :=\
    \ i\u500B(\u533A\u5225\u3059\u308B)\u3092k\u30B0\u30EB\u30FC\u30D7(\u533A\u5225\
    \u3057\u306A\u3044)\u306B\u5206\u3051\u308B\u5834\u5408\u306E\u6570\n    S = [[0]\
    \ * (box + 1) for i in range(ball + 1)]\n    S[0][0] = 1\n    for i in range(ball):\n\
    \        for j in range(box):\n            S[i + 1][j + 1] = S[i][j] + S[i][j\
    \ + 1] * (j + 1)\n            S[i + 1][j + 1] %= MOD\n    return S[ball][box]\n\
    \n\ndef way10(ball, box):\n    \"\"\"ball: False / box: False / constraints: None\n\
    \    ans = P(ball, box) P\u306F\u5206\u5272\u6570 / \u8A08\u7B97\u91CF O(ball\
    \ * box)\n    \"\"\"\n    # P[i][j] := \u6574\u6570i\u3092\u9806\u5E8F\u3092\u533A\
    \u5225\u305B\u305A\u306B\u300Cj\u4EE5\u4E0B\u306E\u81EA\u7136\u6570\u300D\u306E\
    \u548C\u306B\u5206\u3051\u308B\u5834\u5408\u306E\u6570\n    P = [[0] * (ball +\
    \ 1) for _ in range(ball + 1)]\n    for j in range(ball + 1):\n        P[0][j]\
    \ = 1\n    for i in range(ball):\n        for j in range(ball):\n            if\
    \ i - j >= 0:\n                P[i + 1][j + 1] = (P[i + 1][j] + P[i - j][j + 1])\
    \ % MOD\n            else:\n                P[i + 1][j + 1] = P[i + 1][j]\n  \
    \  return P[ball][min(box, ball)]\n\n\ndef way11(ball, box):\n    \"\"\"ball:\
    \ False / box: False / constraints: 1 or less\n    -> ans = int(\u30DC\u30FC\u30EB\
    \u306E\u6570 <= \u7BB1\u306E\u6570)\n    \"\"\"\n    return int(ball <= box)\n\
    \n\ndef way12(ball, box):\n    \"\"\"ball: False / box: False / constraints: 1\
    \ or more\n    ans = P(ball - box, box) P\u306F\u5206\u5272\u6570 / \u8A08\u7B97\
    \u91CF O(ball * box)\n    \"\"\"\n    if ball < box:\n        return 0\n\n   \
    \ # P[i][j] := \u6574\u6570i\u3092\u9806\u5E8F\u3092\u533A\u5225\u305B\u305A\u306B\
    \u300Cj\u4EE5\u4E0B\u306E\u81EA\u7136\u6570\u300D\u306E\u548C\u306B\u5206\u3051\
    \u308B\u5834\u5408\u306E\u6570\n    diff = ball - box\n    P = [[0] * (diff +\
    \ 1) for _ in range(diff + 1)]\n    for j in range(diff + 1):\n        P[0][j]\
    \ = 1\n    for i in range(diff):\n        for j in range(diff):\n            if\
    \ i - j >= 0:\n                P[i + 1][j + 1] = (P[i + 1][j] + P[i - j][j + 1])\
    \ % MOD\n            else:\n                P[i + 1][j + 1] = P[i + 1][j]\n  \
    \  return P[diff][min(diff, box)]\n\n    # \u3042\u3089\u304B\u3058\u3081\u3001\
    \u3059\u3079\u3066\u306E\u7BB1\u306B\u30DC\u30FC\u30EB\u30921\u3064\u305A\u3064\
    \u914D\u3063\u3066\u304A\u304F\u3068\n    # \u533A\u5225\u3057\u306A\u3044(ball\
    \ - box)\u500B\u306E\u30DC\u30FC\u30EB\u3092\u3001\u533A\u5225\u3057\u306A\u3044\
    box\u500B\u306E\u7BB1\u306B\u914D\u308B\u901A\u308A\u6570\u306B\u5E30\u7740\n\
    \    # -> way11(ball - box, box) \u3068\u540C\u7B49\u306E\u554F\u984C\u3068\u306A\
    \u308B\n"
  dependsOn:
  - Combination/modinv_combination.py
  isVerificationFile: false
  path: Combination/twelvefold_way.py
  requiredBy: []
  timestamp: '2021-01-06 00:51:01+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DPL_5_L.test.py
  - TestCase/AOJ/DPL_5_J.test.py
  - TestCase/AOJ/DPL_5_B.test.py
  - TestCase/AOJ/DPL_5_I.test.py
  - TestCase/AOJ/DPL_5_G.test.py
  - TestCase/AOJ/DPL_5_C.test.py
  - TestCase/AOJ/DPL_5_E.test.py
  - TestCase/AOJ/DPL_5_K.test.py
  - TestCase/AOJ/DPL_5_A.test.py
  - TestCase/AOJ/DPL_5_F.test.py
  - TestCase/AOJ/DPL_5_D.test.py
  - TestCase/AOJ/DPL_5_H.test.py
documentation_of: Combination/twelvefold_way.py
layout: document
title: "\u5199\u50CF12\u76F8(twelvefold way)"
---
