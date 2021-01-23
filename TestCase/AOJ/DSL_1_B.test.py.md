---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\UnionFind\UnionFindWithPotential.py
    title: "\u30DD\u30C6\u30F3\u30B7\u30E3\u30EB\u4ED8\u304DUnion Find"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_B
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_B\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom DataStructure.UnionFind.UnionFindWithPotential\
    \ import UnionFindWithPotential\r\n\r\n\r\ndef main():\r\n    n, q = map(int,\
    \ input().split())\r\n    queries = [list(map(int, input().split())) for i in\
    \ range(q)]\r\n\r\n    INF = 10 ** 18\r\n    ufp = UnionFindWithPotential(n)\r\
    \n    ans = []\r\n    for flag, *query in queries:\r\n        if flag == 0:\r\n\
    \            x, y, p = query\r\n            ufp.merge(x, y, p)\r\n        else:\r\
    \n            x, y = query\r\n            p = ufp.diff(x, y)\r\n            ans.append(str(p)\
    \ if p != INF else \"?\")\r\n\r\n    print('\\n'.join(ans))\r\n\r\n\r\nif __name__\
    \ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - DataStructure\UnionFind\UnionFindWithPotential.py
  isVerificationFile: true
  path: TestCase\AOJ\DSL_1_B.test.py
  requiredBy: []
  timestamp: '2021-01-02 02:55:57+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\DSL_1_B.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\DSL_1_B.test.py
- /verify\TestCase\AOJ\DSL_1_B.test.py.html
title: TestCase\AOJ\DSL_1_B.test.py
---
