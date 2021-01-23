---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\BinaryIndexedTree\PointAddRangeSum.py
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
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_range_sum\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom DataStructure.BinaryIndexedTree.PointAddRangeSum\
    \ import BinaryIndexedTree\r\n\r\n\r\ndef main():\r\n    n, q = map(int, input().split())\r\
    \n    a = list(map(int, input().split()))\r\n    queries = [list(map(int, input().split()))\
    \ for _ in range(q)]\r\n\r\n    bit = BinaryIndexedTree(n)\r\n    bit.build(a)\r\
    \n    ans = []\r\n    for flag, l, r in queries:\r\n        if flag:\r\n     \
    \       ans.append(bit.sum(l, r))\r\n        else:\r\n            bit.add(l, r)\
    \  # l = index, r = val\r\n\r\n    print(\"\\n\".join(map(str, ans)))\r\n\r\n\r\
    \nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - DataStructure\BinaryIndexedTree\PointAddRangeSum.py
  isVerificationFile: true
  path: TestCase\LibraryChecker\point_add_range_sum.test.py
  requiredBy: []
  timestamp: '2021-01-02 01:05:58+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\LibraryChecker\point_add_range_sum.test.py
layout: document
redirect_from:
- /verify\TestCase\LibraryChecker\point_add_range_sum.test.py
- /verify\TestCase\LibraryChecker\point_add_range_sum.test.py.html
title: TestCase\LibraryChecker\point_add_range_sum.test.py
---
