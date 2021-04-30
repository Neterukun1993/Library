---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/BinaryIndexedTree/PointAddRangeSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_add_range_sum
    links:
    - https://judge.yosupo.jp/problem/point_add_range_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.BinaryIndexedTree.PointAddRangeSum\
    \ import BinaryIndexedTree\n\n\ndef main():\n    n, q = map(int, input().split())\n\
    \    a = list(map(int, input().split()))\n    queries = [list(map(int, input().split()))\
    \ for _ in range(q)]\n\n    bit = BinaryIndexedTree(n)\n    bit.build(a)\n   \
    \ ans = []\n    for flag, l, r in queries:\n        if flag:\n            ans.append(bit.sum(l,\
    \ r))\n        else:\n            bit.add(l, r)  # l = index, r = val\n\n    print(\"\
    \\n\".join(map(str, ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/BinaryIndexedTree/PointAddRangeSum.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/point_add_range_sum.test.py
  requiredBy: []
  timestamp: '2021-01-02 01:05:58+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/point_add_range_sum.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/point_add_range_sum.test.py
- /verify/TestCase/LibraryChecker/point_add_range_sum.test.py.html
title: TestCase/LibraryChecker/point_add_range_sum.test.py
---
