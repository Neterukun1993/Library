---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: DataStructure/misc/SlidingWindowAggregation.py
    title: Sliding Window Aggregation
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_D
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_D\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.misc.SlidingWindowAggregation\
    \ import SlidingWindowAggregation\n\n\ndef main():\n    n, l = map(int, input().split())\n\
    \    a = list(map(int, input().split()))\n\n    swag = SlidingWindowAggregation(min)\n\
    \    for i in range(l - 1):\n        swag.append(a[i])\n\n    ans = []\n    for\
    \ i in range(l - 1, n):\n        swag.append(a[i])\n        ans.append(swag.all_fold())\n\
    \        swag.popleft()\n\n    print(*ans)\n\n\nif __name__ == '__main__':\n \
    \   main()\n"
  dependsOn:
  - DataStructure/misc/SlidingWindowAggregation.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_3_D.test.py
  requiredBy: []
  timestamp: '2021-01-03 19:45:45+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_3_D.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_3_D.test.py
- /verify/TestCase/AOJ/DSL_3_D.test.py.html
title: TestCase/AOJ/DSL_3_D.test.py
---
