---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/misc/Doubling.py
    title: "functional graph \u4E0A\u306E (\u9806\u5217\u4E0A\u306E) \u30C0\u30D6\u30EA\
      \u30F3\u30B0"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc175/tasks/abc175_d
    links:
    - https://atcoder.jp/contests/abc175/tasks/abc175_d
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc175/tasks/abc175_d\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.misc.Doubling import\
    \ Doubling\n\n\ndef main():\n    n, k = map(int, input().split())\n    p = list(map(int,\
    \ input().split()))\n    c = list(map(int, input().split()))\n\n    p = [p[i]\
    \ - 1 for i in range(n)]\n    db = Doubling(p)\n\n    values = [(c[i], c[i]) for\
    \ i in range(n)]\n    op = lambda x1, x2: (x1[0] + x2[0], max(x1[1], x1[0] + x2[1]))\n\
    \    e = (0, -10 ** 18)\n    db.build_path(values, op, e)\n\n    ans = -10 **\
    \ 18\n    for i in range(n):\n        ans = max(ans, db.fold(i, k)[1])\n\n   \
    \ print(ans)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/misc/Doubling.py
  isVerificationFile: true
  path: TestCase/AtCoder/abc175_d.test.py
  requiredBy: []
  timestamp: '2021-09-06 14:34:02+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AtCoder/abc175_d.test.py
layout: document
redirect_from:
- /verify/TestCase/AtCoder/abc175_d.test.py
- /verify/TestCase/AtCoder/abc175_d.test.py.html
title: TestCase/AtCoder/abc175_d.test.py
---
