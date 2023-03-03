---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/Wavelet/RectangleSum.py
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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/rectangle_sum\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.Wavelet.RectangleSum\
    \ import CompressedRectangleSum\n\n\ndef main():\n    n, q = map(int, input().split())\n\
    \    points = [list(map(int, input().split())) for i in range(n)]\n    queries\
    \ = [list(map(int, input().split())) for i in range(q)]\n\n    crs = CompressedRectangleSum(points)\n\
    \n    ans = []\n    for l, lower, r, upper in queries:\n        ans.append(crs.rect_sum(l,\
    \ r, lower, upper))\n\n    print(\"\\n\".join(map(str, ans)))\n\n\nif __name__\
    \ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/Wavelet/RectangleSum.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/rectangle_sum.WaveletMatrix.test.py
  requiredBy: []
  timestamp: '2022-07-16 00:12:27+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/rectangle_sum.WaveletMatrix.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/rectangle_sum.WaveletMatrix.test.py
- /verify/TestCase/LibraryChecker/rectangle_sum.WaveletMatrix.test.py.html
title: TestCase/LibraryChecker/rectangle_sum.WaveletMatrix.test.py
---
