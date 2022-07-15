---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/misc/DynamicMedian.py
    title: "\u52D5\u7684\u4E2D\u592E\u5024\u30AF\u30A8\u30EA"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc127/tasks/abc127_f
    links:
    - https://atcoder.jp/contests/abc127/tasks/abc127_f
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc127/tasks/abc127_f\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.misc.DynamicMedian\
    \ import DynamicMedian\n\n\ndef main():\n    q = int(input())\n    queries = [list(map(int,\
    \ input().split())) for i in range(q)]\n    dm = DynamicMedian()\n \n    b = 0\n\
    \    for i in range(q):\n        if queries[i][0] == 1:\n            _, tmp_a,\
    \ tmp_b = queries[i]\n            dm.add(tmp_a)\n            b += tmp_b\n    \
    \    else:\n            print(dm.median_low(), dm.minimum_query() + b)\n\n\nif\
    \ __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/misc/DynamicMedian.py
  isVerificationFile: true
  path: TestCase/AtCoder/abc127_f.test.py
  requiredBy: []
  timestamp: '2022-01-22 18:47:07+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AtCoder/abc127_f.test.py
layout: document
redirect_from:
- /verify/TestCase/AtCoder/abc127_f.test.py
- /verify/TestCase/AtCoder/abc127_f.test.py.html
title: TestCase/AtCoder/abc127_f.test.py
---
