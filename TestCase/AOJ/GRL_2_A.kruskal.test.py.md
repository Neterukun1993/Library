---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\SpanningTree\kruskal.py
    title: "\u6700\u5C0F\u5168\u57DF\u6728 (\u30AF\u30E9\u30B9\u30AB\u30EB\u6CD5)"
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
    \nimport sys\r\ninput = sys.stdin.readline\r\n\r\nfrom Graph.SpanningTree.kruskal\
    \ import kruskal\r\n\r\n\r\ndef main():\r\n    n, m = map(int, input().split())\r\
    \n    edges = [list(map(int, input().split())) for i in range(m)]\r\n\r\n    print(kruskal(n,\
    \ edges))\r\n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - Graph\SpanningTree\kruskal.py
  isVerificationFile: true
  path: TestCase\AOJ\GRL_2_A.kruskal.test.py
  requiredBy: []
  timestamp: '2021-01-04 21:55:18+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\GRL_2_A.kruskal.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\GRL_2_A.kruskal.test.py
- /verify\TestCase\AOJ\GRL_2_A.kruskal.test.py.html
title: TestCase\AOJ\GRL_2_A.kruskal.test.py
---
