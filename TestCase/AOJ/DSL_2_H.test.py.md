---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: DataStructure/SegmentTree/RmQ_RAQ.py
    title: RmQ_RAQ
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_H
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_H
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_H\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.SegmentTree.RmQ_RAQ\
    \ import RmQ_RAQ\n\n\ndef main():\n    n, q = map(int, input().split())\n    queries\
    \ = [list(map(int, input().split())) for i in range(q)]\n\n    lst = RmQ_RAQ(n)\n\
    \    ans = []\n    for flag, *query in queries:\n        if flag == 0:\n     \
    \       l, r, x = query\n            r += 1\n            lst.range_apply(l, r,\
    \ x)\n        else:\n            l, r = query\n            r += 1\n          \
    \  ans.append(lst.fold(l, r))\n\n    print('\\n'.join(map(str, ans)))\n\n\nif\
    \ __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/SegmentTree/RmQ_RAQ.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_2_H.test.py
  requiredBy: []
  timestamp: '2021-01-02 18:15:11+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_2_H.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_2_H.test.py
- /verify/TestCase/AOJ/DSL_2_H.test.py.html
title: TestCase/AOJ/DSL_2_H.test.py
---
