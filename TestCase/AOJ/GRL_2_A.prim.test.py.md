---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A\n\
    import sys\ninput = sys.stdin.readline\n\nfrom Graph.SpanningTree.prim import\
    \ prim\n\n\ndef main():\n    n, m = map(int, input().split())\n    edges = [list(map(int,\
    \ input().split())) for i in range(m)]\n\n    graph = [[] for i in range(n)]\n\
    \    for u, v, cost in edges:\n        graph[u].append((v, cost))\n        graph[v].append((u,\
    \ cost))\n\n    print(prim(graph))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: TestCase/AOJ/GRL_2_A.prim.test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_2_A.prim.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_2_A.prim.test.py
- /verify/TestCase/AOJ/GRL_2_A.prim.test.py.html
title: TestCase/AOJ/GRL_2_A.prim.test.py
---
