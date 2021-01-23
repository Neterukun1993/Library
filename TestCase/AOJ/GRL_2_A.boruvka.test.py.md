---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\SpanningTree\boruvka.py
    title: "\u6700\u5C0F\u5168\u57DF\u6728 (\u30D6\u30EB\u30FC\u30D5\u30AB\u6CD5)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A\r\
    \nimport sys\r\ninput = sys.stdin.readline\r\n\r\nfrom Graph.SpanningTree.boruvka\
    \ import boruvka \r\n\r\n\r\ndef main():\r\n    n, m = map(int, input().split())\r\
    \n    edges = [list(map(int, input().split())) for i in range(m)]\r\n\r\n    print(boruvka(n,\
    \ edges))\r\n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - Graph\SpanningTree\boruvka.py
  isVerificationFile: true
  path: TestCase\AOJ\GRL_2_A.boruvka.test.py
  requiredBy: []
  timestamp: '2021-01-04 22:11:12+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\GRL_2_A.boruvka.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\GRL_2_A.boruvka.test.py
- /verify\TestCase\AOJ\GRL_2_A.boruvka.test.py.html
title: TestCase\AOJ\GRL_2_A.boruvka.test.py
---
