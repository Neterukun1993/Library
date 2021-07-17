---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/BinaryIndexedTree/RangeAddPointGet2D.py
    title: "\u77E9\u5F62\u52A0\u7B97\u30FB\u4E00\u70B9\u53D6\u5F97"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_B\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.BinaryIndexedTree.RangeAddPointGet2D\
    \ import BinaryIndexedTree\n\n\ndef main():\n    n = int(input())\n    queries\
    \ = [list(map(int, input().split())) for i in range(n)]\n\n    bit = BinaryIndexedTree(1000,\
    \ 1000)\n    for hl, wl, hr, wr in queries:\n        bit.add(hl, hr, wl, wr, 1)\n\
    \n    ans = 0\n    for i in range(1000):\n        for j in range(1000):\n    \
    \        ans = max(ans, bit.get(i, j))\n    print(ans)\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - DataStructure/BinaryIndexedTree/RangeAddPointGet2D.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_5_B.BIT.test.py
  requiredBy: []
  timestamp: '2021-05-08 19:01:44+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_5_B.BIT.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_5_B.BIT.test.py
- /verify/TestCase/AOJ/DSL_5_B.BIT.test.py.html
title: TestCase/AOJ/DSL_5_B.BIT.test.py
---
