---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\BinaryIndexedTree\RangeAddPointGet2D.py
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
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_B\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom DataStructure.BinaryIndexedTree.RangeAddPointGet2D\
    \ import BinaryIndexedTree\r\n\r\n\r\ndef main():\r\n    n = int(input())\r\n\
    \    queries = [list(map(int, input().split())) for i in range(n)]\r\n\r\n   \
    \ bit = BinaryIndexedTree(1000, 1000)\r\n    for hl, wl, hr, wr in queries:\r\n\
    \        bit.add(hl, hr, wl, wr, 1)\r\n\r\n    ans = 0\r\n    for i in range(1000):\r\
    \n        for j in range(1000):\r\n            ans = max(ans, bit[i, j])\r\n \
    \   print(ans)\r\n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - DataStructure\BinaryIndexedTree\RangeAddPointGet2D.py
  isVerificationFile: true
  path: TestCase\AOJ\DSL_5_B.BIT.test.py
  requiredBy: []
  timestamp: '2021-01-02 15:42:36+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\DSL_5_B.BIT.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\DSL_5_B.BIT.test.py
- /verify\TestCase\AOJ\DSL_5_B.BIT.test.py.html
title: TestCase\AOJ\DSL_5_B.BIT.test.py
---
