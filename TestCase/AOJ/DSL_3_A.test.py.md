---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/misc/SlidingWindowAggregation.py
    title: DataStructure/misc/SlidingWindowAggregation.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.8.7/x64/lib/python3.8/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.8.7/x64/lib/python3.8/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.misc.SlidingWindowAggregation\
    \ import SlidingWindowAggregation\n\n\ndef main():\n    n, s = map(int, input().split())\n\
    \    a = list(map(int, input().split()))\n\n    swag = SlidingWindowAggregation(lambda\
    \ x, y: x + y)\n    ans = 10 ** 18\n    r = 0\n    for l in range(n):\n      \
    \  if not swag:\n            swag.append(a[r])\n            r += 1\n        while\
    \ r < n and swag.all_fold() < s:\n            swag.append(a[r])\n            r\
    \ += 1\n        if swag.all_fold() >= s:\n            ans = min(r - l, ans)\n\
    \        swag.popleft()\n\n    if ans == 10 ** 18:\n        print(0)\n    else:\n\
    \        print(ans)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/misc/SlidingWindowAggregation.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_3_A.test.py
  requiredBy: []
  timestamp: '2021-01-03 19:45:45+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_3_A.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_3_A.test.py
- /verify/TestCase/AOJ/DSL_3_A.test.py.html
title: TestCase/AOJ/DSL_3_A.test.py
---
