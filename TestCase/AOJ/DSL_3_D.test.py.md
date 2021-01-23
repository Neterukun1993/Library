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
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_D
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_D
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_D\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom DataStructure.misc.SlidingWindowAggregation\
    \ import SlidingWindowAggregation\r\n\r\n\r\ndef main():\r\n    n, l = map(int,\
    \ input().split())\r\n    a = list(map(int, input().split()))\r\n\r\n    swag\
    \ = SlidingWindowAggregation(min)\r\n    for i in range(l - 1):\r\n        swag.append(a[i])\r\
    \n\r\n    ans = []\r\n    for i in range(l - 1, n):\r\n        swag.append(a[i])\r\
    \n        ans.append(swag.all_fold())\r\n        swag.popleft()\r\n\r\n    print(*ans)\r\
    \n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - DataStructure\misc\SlidingWindowAggregation.py
  isVerificationFile: true
  path: TestCase\AOJ\DSL_3_D.test.py
  requiredBy: []
  timestamp: '2021-01-03 19:45:45+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\DSL_3_D.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\DSL_3_D.test.py
- /verify\TestCase\AOJ\DSL_3_D.test.py.html
title: TestCase\AOJ\DSL_3_D.test.py
---
