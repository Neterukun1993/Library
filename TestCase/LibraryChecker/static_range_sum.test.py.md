---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/AccumulateSum/AccumulateSum.py
    title: "\u7D2F\u7A4D\u548C"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/static_range_sum
    links:
    - https://judge.yosupo.jp/problem/static_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/static_range_sum\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.AccumulateSum.AccumulateSum\
    \ import AccumulateSum\n\n\ndef main():\n    n, q = map(int, input().split())\n\
    \    a = list(map(int, input().split()))\n    queries = [list(map(int, input().split()))\
    \ for _ in range(q)]\n\n    acc = AccumulateSum(a)\n    ans = []\n    for l, r\
    \ in queries:\n        ans.append(acc.sum(l, r))\n    print('\\n'.join(map(str,\
    \ ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/AccumulateSum/AccumulateSum.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/static_range_sum.test.py
  requiredBy: []
  timestamp: '2021-01-01 21:11:21+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/static_range_sum.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/static_range_sum.test.py
- /verify/TestCase/LibraryChecker/static_range_sum.test.py.html
title: TestCase/LibraryChecker/static_range_sum.test.py
---
