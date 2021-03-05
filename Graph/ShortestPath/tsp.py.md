---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/AOJ/DPL_2_A.test.py
    title: TestCase/AOJ/DPL_2_A.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def tsp(matrix):\n    INF = 10 ** 18\n    n = len(matrix)\n    dp = [[INF]\
    \ * n for i in range(1 << n)]\n    dp[1 << 0][0] = 0\n\n    for bit_state in range(1\
    \ << n):\n        for i in range(n):\n            if not((bit_state >> i) & 1):\n\
    \                continue\n            for j in range(n):\n                if\
    \ (bit_state >> j) & 1:\n                    continue\n                new_state\
    \ = bit_state | (1 << j)\n                if dp[new_state][j] > dp[bit_state][i]\
    \ + matrix[i][j]:\n                    dp[new_state][j] = dp[bit_state][i] + matrix[i][j]\n\
    \n    ans = INF\n    last = -1\n    for i in range(n):\n        if ans > dp[(1\
    \ << n) - 1][i] + matrix[i][0]:\n            ans = dp[(1 << n) - 1][i] + matrix[i][0]\n\
    \            last = i\n    if ans == INF:\n        return ans, []\n\n    path\
    \ = [last]\n    v = last\n    bit_state = (1 << n) - 1\n    while v != 0:\n  \
    \      for prv_v in range(n):\n            if (bit_state >> prv_v) & 1 and dp[bit_state][v]\
    \ == dp[bit_state ^ (1 << v)][prv_v] + matrix[prv_v][v]:\n                path.append(prv_v)\n\
    \                bit_state -= 1 << v\n                v = prv_v\n            \
    \    break\n    return ans, path[::-1]\n"
  dependsOn: []
  isVerificationFile: false
  path: Graph/ShortestPath/tsp.py
  requiredBy: []
  timestamp: '2021-01-24 02:57:32+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/AOJ/DPL_2_A.test.py
documentation_of: Graph/ShortestPath/tsp.py
layout: document
title: "\u5DE1\u56DE\u30BB\u30FC\u30EB\u30B9\u30DE\u30F3\u554F\u984C"
---
