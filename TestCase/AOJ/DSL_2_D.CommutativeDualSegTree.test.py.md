---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/RUQ.py
    title: RUQ
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_D
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_D\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.SegmentTree.RUQ\
    \ import RUQ\n\n\ndef main():\n    n, q = map(int, input().split())\n    queries\
    \ = [list(map(int, input().split())) for i in range(q)]\n\n    ruq = RUQ(n)\n\
    \    ruq.range_apply(0, n, (1 << 31) - 1)\n    ans = []\n    for flag, *query\
    \ in queries:\n        if flag == 0:\n            l, r, x = query\n          \
    \  r += 1\n            ruq.range_apply(l, r, x)\n        else:\n            i\
    \ = query[0]\n            ans.append(ruq[i])\n\n    print('\\n'.join(map(str,\
    \ ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/SegmentTree/RUQ.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_2_D.CommutativeDualSegTree.test.py
  requiredBy: []
  timestamp: '2022-04-24 23:38:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_2_D.CommutativeDualSegTree.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_2_D.CommutativeDualSegTree.test.py
- /verify/TestCase/AOJ/DSL_2_D.CommutativeDualSegTree.test.py.html
title: TestCase/AOJ/DSL_2_D.CommutativeDualSegTree.test.py
---
