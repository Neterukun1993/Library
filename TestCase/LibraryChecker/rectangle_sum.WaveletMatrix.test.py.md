---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\Wavelet\RectangleSum.py
    title: "\u77E9\u5F62\u548C\u53D6\u5F97"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/rectangle_sum
    links:
    - https://judge.yosupo.jp/problem/rectangle_sum
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rectangle_sum\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom DataStructure.Wavelet.RectangleSum\
    \ import CompressedRectangleSum\r\n\r\n\r\ndef main():\r\n    n, q = map(int,\
    \ input().split())\r\n    points = [list(map(int, input().split())) for i in range(n)]\r\
    \n    queries = [list(map(int, input().split())) for i in range(q)]\r\n\r\n  \
    \  crs = CompressedRectangleSum(points)\r\n\r\n    ans = []\r\n    for l, lower,\
    \ r, upper in queries:\r\n        ans.append(crs.rect_sum(l, r, lower, upper))\r\
    \n\r\n    print(\"\\n\".join(map(str, ans)))\r\n\r\n\r\nif __name__ == '__main__':\r\
    \n    main()\r\n"
  dependsOn:
  - DataStructure\Wavelet\RectangleSum.py
  isVerificationFile: true
  path: TestCase\LibraryChecker\rectangle_sum.WaveletMatrix.test.py
  requiredBy: []
  timestamp: '2021-01-11 00:02:29+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\LibraryChecker\rectangle_sum.WaveletMatrix.test.py
layout: document
redirect_from:
- /verify\TestCase\LibraryChecker\rectangle_sum.WaveletMatrix.test.py
- /verify\TestCase\LibraryChecker\rectangle_sum.WaveletMatrix.test.py.html
title: TestCase\LibraryChecker\rectangle_sum.WaveletMatrix.test.py
---
