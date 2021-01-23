---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\BinaryIndexedTree\RangeAddRangeSum.py
    title: "\u533A\u9593\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_G
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_G
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_G\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom DataStructure.BinaryIndexedTree.RangeAddRangeSum\
    \ import BinaryIndexedTree\r\n\r\n\r\ndef main():\r\n    n, q = map(int, input().split())\r\
    \n    queries = [list(map(int, input().split())) for i in range(q)]\r\n\r\n  \
    \  bit = BinaryIndexedTree(n)\r\n    ans = []\r\n    for flag, *query in queries:\r\
    \n        if flag == 0:\r\n            l, r, x = query\r\n            l -= 1\r\
    \n            bit.add(l, r, x)\r\n        else:\r\n            l, r = query\r\n\
    \            l -= 1\r\n            ans.append(bit.sum(l, r))\r\n\r\n    print('\\\
    n'.join(map(str, ans)))\r\n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - DataStructure\BinaryIndexedTree\RangeAddRangeSum.py
  isVerificationFile: true
  path: TestCase\AOJ\DSL_2_G.test.py
  requiredBy: []
  timestamp: '2021-01-02 01:52:07+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\DSL_2_G.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\DSL_2_G.test.py
- /verify\TestCase\AOJ\DSL_2_G.test.py.html
title: TestCase\AOJ\DSL_2_G.test.py
---
