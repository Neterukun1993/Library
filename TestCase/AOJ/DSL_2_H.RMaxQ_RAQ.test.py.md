---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/RMaxQ_RAQ.py
    title: DataStructure/SegmentTree/RMaxQ_RAQ.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_H
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_H
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_H\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.SegmentTree.RMaxQ_RAQ\
    \ import RMaxQ_RAQ\n\n\ndef main():\n    n, q = map(int, input().split())\n  \
    \  queries = [list(map(int, input().split())) for i in range(q)]\n\n    lst =\
    \ RMaxQ_RAQ(n)\n    ans = []\n    for flag, *query in queries:\n        if flag\
    \ == 0:\n            l, r, x = query\n            r += 1\n            lst.range_apply(l,\
    \ r, -x)\n        else:\n            l, r = query\n            r += 1\n      \
    \      ans.append(-lst.fold(l, r))\n\n    print('\\n'.join(map(str, ans)))\n\n\
    \nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/SegmentTree/RMaxQ_RAQ.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_2_H.RMaxQ_RAQ.test.py
  requiredBy: []
  timestamp: '2022-04-25 00:19:30+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_2_H.RMaxQ_RAQ.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_2_H.RMaxQ_RAQ.test.py
- /verify/TestCase/AOJ/DSL_2_H.RMaxQ_RAQ.test.py.html
title: TestCase/AOJ/DSL_2_H.RMaxQ_RAQ.test.py
---
