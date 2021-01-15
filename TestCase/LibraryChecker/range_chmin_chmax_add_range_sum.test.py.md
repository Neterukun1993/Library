---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: DataStructure/SegmentTree/SegmentTreeBeats.py
    title: Segment Tree Beats
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_chmin_chmax_add_range_sum
    links:
    - https://judge.yosupo.jp/problem/range_chmin_chmax_add_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_chmin_chmax_add_range_sum\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.SegmentTree.SegmentTreeBeats\
    \ import SegmentTreeBeats\n\n\ndef main():\n    n, q = map(int, input().split())\n\
    \    a = list(map(int, input().split()))\n    queries = [list(map(int, input().split()))\
    \ for i in range(q)]\n\n    stb = SegmentTreeBeats(n)\n    stb.build(a)\n\n  \
    \  ans = []\n    for flag, *query in queries:\n        if flag == 0:\n       \
    \     l, r, b = query\n            stb.range_chmin(l, r, b)\n        elif flag\
    \ == 1:\n            l, r, b = query\n            stb.range_chmax(l, r, b)\n \
    \       elif flag == 2:\n            l, r, b = query\n            stb.range_add(l,\
    \ r, b)\n        else:\n            l, r = query\n            ans.append(stb.fold_sum(l,\
    \ r))\n\n    print(*ans, sep=\"\\n\")\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/SegmentTree/SegmentTreeBeats.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/range_chmin_chmax_add_range_sum.test.py
  requiredBy: []
  timestamp: '2021-01-15 08:52:59+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/range_chmin_chmax_add_range_sum.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/range_chmin_chmax_add_range_sum.test.py
- /verify/TestCase/LibraryChecker/range_chmin_chmax_add_range_sum.test.py.html
title: TestCase/LibraryChecker/range_chmin_chmax_add_range_sum.test.py
---
