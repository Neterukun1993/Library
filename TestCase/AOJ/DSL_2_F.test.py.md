---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/RmQ_RUQ.py
    title: RmQ_RUQ
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_F
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_F
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_F\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.SegmentTree.RmQ_RUQ\
    \ import RmQ_RUQ\n\n\ndef main():\n    n, q = map(int, input().split())\n    queries\
    \ = [list(map(int, input().split())) for i in range(q)]\n\n    lst = RmQ_RUQ(n)\n\
    \    ans = []\n    for flag, *query in queries:\n        if flag == 0:\n     \
    \       l, r, x = query\n            r += 1\n            lst.range_apply(l, r,\
    \ x)\n        else:\n            l, r = query\n            r += 1\n          \
    \  ans.append(lst.fold(l, r))\n\n    print('\\n'.join(map(str, ans)))\n\n\nif\
    \ __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/SegmentTree/RmQ_RUQ.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_2_F.test.py
  requiredBy: []
  timestamp: '2022-04-25 00:19:30+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_2_F.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_2_F.test.py
- /verify/TestCase/AOJ/DSL_2_F.test.py.html
title: TestCase/AOJ/DSL_2_F.test.py
---
