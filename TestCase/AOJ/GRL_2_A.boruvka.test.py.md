---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/SpanningTree/boruvka.py
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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_2_A\n\
    import sys\ninput = sys.stdin.readline\n\nfrom Graph.SpanningTree.boruvka import\
    \ boruvka \n\n\ndef main():\n    n, m = map(int, input().split())\n    edges =\
    \ [list(map(int, input().split())) for i in range(m)]\n\n    print(boruvka(n,\
    \ edges))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/SpanningTree/boruvka.py
  isVerificationFile: true
  path: TestCase/AOJ/GRL_2_A.boruvka.test.py
  requiredBy: []
  timestamp: '2021-01-04 22:11:12+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_2_A.boruvka.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_2_A.boruvka.test.py
- /verify/TestCase/AOJ/GRL_2_A.boruvka.test.py.html
title: TestCase/AOJ/GRL_2_A.boruvka.test.py
---
