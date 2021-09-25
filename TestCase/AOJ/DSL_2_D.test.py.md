---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/DualSegmentTree.py
    title: "\u53CC\u5BFE\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Dual Segment Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_D
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_D\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.SegmentTree.DualSegmentTree\
    \ import DualSegmentTree\n\n\ndef main():\n    n, q = map(int, input().split())\n\
    \    queries = [list(map(int, input().split())) for i in range(q)]\n\n    unitA\
    \ = (False, (1 << 31) - 1)\n    A_f = lambda a1, a2: a2 if a2[0] else a1\n   \
    \ dst = DualSegmentTree(n, unitA, A_f)\n    ans = []\n    for flag, *query in\
    \ queries:\n        if flag == 0:\n            l, r, x = query\n            r\
    \ += 1\n            dst.range_apply(l, r, (True, x))\n        else:\n        \
    \    i = query[0]\n            ans.append(dst[i][1])\n\n    print('\\n'.join(map(str,\
    \ ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/SegmentTree/DualSegmentTree.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_2_D.test.py
  requiredBy: []
  timestamp: '2021-01-02 05:02:24+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_2_D.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_2_D.test.py
- /verify/TestCase/AOJ/DSL_2_D.test.py.html
title: TestCase/AOJ/DSL_2_D.test.py
---
