---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\Wavelet\PointAddRectangleSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u77E9\u5F62\u548C\u53D6\u5F97"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/point_add_rectangle_sum
    links:
    - https://judge.yosupo.jp/problem/point_add_rectangle_sum
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/point_add_rectangle_sum\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom DataStructure.Wavelet.PointAddRectangleSum\
    \ import CompressedPointAddRectangleSum\r\n\r\n\r\ndef main():\r\n    n, q = map(int,\
    \ input().split())\r\n    points = [tuple(map(int, input().split())) for i in\
    \ range(n)]\r\n    queries = [list(map(int, input().split())) for i in range(q)]\r\
    \n\r\n    for flag, *query in queries:\r\n        if flag == 0:\r\n          \
    \  x, y, _ = query\r\n            points.append((x, y, 0))\r\n\r\n    crs = CompressedPointAddRectangleSum(points)\r\
    \n    ans = []\r\n    for flag, *query in queries:\r\n        if flag == 0:\r\n\
    \            x, y, w = query\r\n            crs.point_add(x, y, w)\r\n       \
    \ else:\r\n            l, lower, r, upper = query\r\n            ans.append(crs.rect_sum(l,\
    \ r, lower, upper))\r\n\r\n    print(\"\\n\".join(map(str, ans)))\r\n\r\n\r\n\
    if __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - DataStructure\Wavelet\PointAddRectangleSum.py
  isVerificationFile: true
  path: TestCase\LibraryChecker\point_add_rectangle_sum.test.py
  requiredBy: []
  timestamp: '2021-01-12 04:24:03+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\LibraryChecker\point_add_rectangle_sum.test.py
layout: document
redirect_from:
- /verify\TestCase\LibraryChecker\point_add_rectangle_sum.test.py
- /verify\TestCase\LibraryChecker\point_add_rectangle_sum.test.py.html
title: TestCase\LibraryChecker\point_add_rectangle_sum.test.py
---
