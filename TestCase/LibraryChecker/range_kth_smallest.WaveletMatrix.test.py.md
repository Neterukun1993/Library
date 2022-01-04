---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/Wavelet/WaveletMatrix.py
    title: "\u30A6\u30A7\u30FC\u30D6\u30EC\u30C3\u30C8\u884C\u5217"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/range_kth_smallest
    links:
    - https://judge.yosupo.jp/problem/range_kth_smallest
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/range_kth_smallest\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.Wavelet.WaveletMatrix\
    \ import WaveletMatrix\n\n\ndef main():\n    n, q = map(int, input().split())\n\
    \    a = list(map(int, input().split()))\n    queries = [list(map(int, input().split()))\
    \ for i in range(q)]\n\n    wm = WaveletMatrix(a)\n    ans = []\n    for l, r,\
    \ k in queries:\n        ans.append(wm.kth_smallest(l, r, k))\n\n    print(\"\\\
    n\".join(map(str, ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/Wavelet/WaveletMatrix.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/range_kth_smallest.WaveletMatrix.test.py
  requiredBy: []
  timestamp: '2021-01-10 20:36:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/range_kth_smallest.WaveletMatrix.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/range_kth_smallest.WaveletMatrix.test.py
- /verify/TestCase/LibraryChecker/range_kth_smallest.WaveletMatrix.test.py.html
title: TestCase/LibraryChecker/range_kth_smallest.WaveletMatrix.test.py
---
