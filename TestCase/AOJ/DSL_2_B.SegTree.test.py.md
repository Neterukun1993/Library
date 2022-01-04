---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/SegmentTree/SegmentTree.py
    title: "\u30BB\u30B0\u30E1\u30F3\u30C8\u6728 (Segment Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_B\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.SegmentTree.SegmentTree\
    \ import SegmentTree\n\n\ndef main():\n    n, q = map(int, input().split())\n\
    \    queries = [list(map(int, input().split())) for i in range(q)]\n\n    st =\
    \ SegmentTree(n, lambda x, y: x + y, 0)\n    ans = []\n    for flag, x, y in queries:\n\
    \        if flag == 0:\n            i = x - 1\n            st[i] = st[i] + y\n\
    \        else:\n            l, r = x - 1, y\n            ans.append(st.fold(l,\
    \ r))\n\n    print('\\n'.join(map(str, ans)))\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - DataStructure/SegmentTree/SegmentTree.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_2_B.SegTree.test.py
  requiredBy: []
  timestamp: '2021-01-02 16:50:23+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_2_B.SegTree.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_2_B.SegTree.test.py
- /verify/TestCase/AOJ/DSL_2_B.SegTree.test.py.html
title: TestCase/AOJ/DSL_2_B.SegTree.test.py
---
