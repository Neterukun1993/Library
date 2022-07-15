---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Flow/MaxFlow.py
    title: "\u6700\u5927\u6D41 (Dinic \u6CD5)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Flow.MaxFlow import MaxFlow\n\
    \n\ndef main():\n    v, e = map(int, input().split())\n    edges = [list(map(int,\
    \ input().split())) for i in range(e)]\n\n    mf = MaxFlow(v)\n    for fr, to,\
    \ cap in edges:\n        mf.add_edge(fr, to, cap)\n\n    print(mf.max_flow(0,\
    \ v - 1, 10 ** 9))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Flow/MaxFlow.py
  isVerificationFile: true
  path: TestCase/AOJ/GRL_6_A.dinic.test.py
  requiredBy: []
  timestamp: '2022-01-04 20:45:42+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_6_A.dinic.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_6_A.dinic.test.py
- /verify/TestCase/AOJ/GRL_6_A.dinic.test.py.html
title: TestCase/AOJ/GRL_6_A.dinic.test.py
---
