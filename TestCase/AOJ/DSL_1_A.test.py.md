---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\UnionFind\UnionFind.py
    title: Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_1_A\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom DataStructure.UnionFind.UnionFind\
    \ import UnionFind\r\n\r\n\r\ndef main():\r\n    n, q = map(int, input().split())\r\
    \n    queries = [list(map(int, input().split())) for i in range(q)]\r\n\r\n  \
    \  uf = UnionFind(n)\r\n    ans = []\r\n    for flag, x, y in queries:\r\n   \
    \     if flag == 0:\r\n            uf.merge(x, y)\r\n        else:\r\n       \
    \     ans.append(int(uf.same(x, y)))\r\n\r\n    print('\\n'.join(map(str, ans)))\r\
    \n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - DataStructure\UnionFind\UnionFind.py
  isVerificationFile: true
  path: TestCase\AOJ\DSL_1_A.test.py
  requiredBy: []
  timestamp: '2021-01-02 02:09:18+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\DSL_1_A.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\DSL_1_A.test.py
- /verify\TestCase\AOJ\DSL_1_A.test.py.html
title: TestCase\AOJ\DSL_1_A.test.py
---
