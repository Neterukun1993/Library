---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/Wavelet/PointAddRectangleSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u77ED\u5F62\u548C\u53D6\u5F97"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_add_rectangle_sum
    links:
    - https://judge.yosupo.jp/problem/point_add_rectangle_sum
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_rectangle_sum\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.Wavelet.PointAddRectangleSum\
    \ import CompressedPointAddRectangleSum\n\n\ndef main():\n    n, q = map(int,\
    \ input().split())\n    points = [tuple(map(int, input().split())) for i in range(n)]\n\
    \    queries = [list(map(int, input().split())) for i in range(q)]\n\n    for\
    \ flag, *query in queries:\n        if flag == 0:\n            x, y, _ = query\n\
    \            points.append((x, y, 0))\n\n    crs = CompressedPointAddRectangleSum(points)\n\
    \    ans = []\n    for flag, *query in queries:\n        if flag == 0:\n     \
    \       x, y, w = query\n            crs.point_add(x, y, w)\n        else:\n \
    \           l, lower, r, upper = query\n            ans.append(crs.rect_sum(l,\
    \ r, lower, upper))\n\n    print(\"\\n\".join(map(str, ans)))\n\n\nif __name__\
    \ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/Wavelet/PointAddRectangleSum.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/point_add_rectangle_sum.test.py
  requiredBy: []
  timestamp: '2021-01-12 04:24:03+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/point_add_rectangle_sum.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/point_add_rectangle_sum.test.py
- /verify/TestCase/LibraryChecker/point_add_rectangle_sum.test.py.html
title: TestCase/LibraryChecker/point_add_rectangle_sum.test.py
---
