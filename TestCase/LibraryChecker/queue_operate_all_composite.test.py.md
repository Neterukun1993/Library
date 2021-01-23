---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\misc\SlidingWindowAggregation.py
    title: Sliding Window Aggregation
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/queue_operate_all_composite
    links:
    - https://judge.yosupo.jp/problem/queue_operate_all_composite
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/queue_operate_all_composite\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom DataStructure.misc.SlidingWindowAggregation\
    \ import SlidingWindowAggregation\r\n\r\n\r\nMOD = 998244353\r\nMASK = (1 << 32)\
    \ - 1\r\n\r\n\r\ndef X_f(x1, x2):\r\n    x = x1 + x2\r\n    return ((x >> 32)\
    \ % MOD << 32) + (x & MASK) % MOD\r\n\r\n\r\ndef XA_map(x, a):\r\n    x0, x1 =\
    \ x >> 32, x & MASK\r\n    a0, a1 = a >> 32, a & MASK\r\n    return (((x0 * a0\
    \ + x1 * a1) % MOD) << 32) + x1\r\n\r\n\r\ndef A_f(a1, a2):\r\n    a10, a11 =\
    \ a1 >> 32, a1 & MASK\r\n    a20, a21 = a2 >> 32, a2 & MASK\r\n    return ((a20\
    \ * a10 % MOD) << 32) + (a20 * a11 + a21) % MOD\r\n\r\n\r\ndef main():\r\n   \
    \ q = int(input())\r\n    queries = [list(map(int, input().split())) for i in\
    \ range(q)]\r\n\r\n    swag = SlidingWindowAggregation(A_f)\r\n    ans = []\r\n\
    \    for query in queries:\r\n        if query[0] == 0:\r\n            _, a, b\
    \ = query\r\n            swag.append((a << 32) + b)\r\n        elif query[0] ==\
    \ 1:\r\n            swag.popleft()\r\n        else:\r\n            _, x = query\r\
    \n            if len(swag) == 0:\r\n                ans.append(x)\r\n        \
    \    else:\r\n                a = swag.all_fold()\r\n                res = XA_map((x\
    \ << 32) + 1, a)\r\n                ans.append(res >> 32)\r\n\r\n    print('\\\
    n'.join(map(str, ans)))\r\n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - DataStructure\misc\SlidingWindowAggregation.py
  isVerificationFile: true
  path: TestCase\LibraryChecker\queue_operate_all_composite.test.py
  requiredBy: []
  timestamp: '2021-01-03 19:45:45+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\LibraryChecker\queue_operate_all_composite.test.py
layout: document
redirect_from:
- /verify\TestCase\LibraryChecker\queue_operate_all_composite.test.py
- /verify\TestCase\LibraryChecker\queue_operate_all_composite.test.py.html
title: TestCase\LibraryChecker\queue_operate_all_composite.test.py
---
