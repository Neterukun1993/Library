---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: DataStructure/SegmentTree/SegmentTree.py
    title: "\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.SegmentTree.SegmentTree\
    \ import SegmentTree\n\n\ndef main():\n    n, q = map(int, input().split())\n\
    \    queries = [list(map(int, input().split())) for i in range(q)]\n\n    e =\
    \ (1 << 31) - 1\n    st = SegmentTree(n, min, e)\n    ans = []\n    for flag,\
    \ x, y in queries:\n        if flag == 0:\n            st[x] = y\n        else:\n\
    \            l, r = x, y + 1\n            ans.append(st.fold(l, r))\n\n    print('\\\
    n'.join(map(str, ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/SegmentTree/SegmentTree.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_2_A.test.py
  requiredBy: []
  timestamp: '2021-01-02 16:36:13+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_2_A.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_2_A.test.py
- /verify/TestCase/AOJ/DSL_2_A.test.py.html
title: TestCase/AOJ/DSL_2_A.test.py
---
