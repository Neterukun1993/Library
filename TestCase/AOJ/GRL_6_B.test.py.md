---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Flow/MinCostFlow.py
    title: "\u6700\u5C0F\u8CBB\u7528\u6D41 (Primal-Dual \u6CD5)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_6_B\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Flow.MinCostFlow import\
    \ MinCostFlow\n\n\ndef main():\n    n, m, f = map(int, input().split())\n    edges\
    \ = [list(map(int, input().split())) for _ in range(m)]\n\n    mcf = MinCostFlow(n)\n\
    \    for fr, to, c, d in edges:\n        mcf.add_edge(fr, to, c, d)\n\n    ans\
    \ = mcf.min_cost_flow(0, n - 1, f)\n    print(ans)\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - Flow/MinCostFlow.py
  isVerificationFile: true
  path: TestCase/AOJ/GRL_6_B.test.py
  requiredBy: []
  timestamp: '2022-01-20 17:35:30+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_6_B.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_6_B.test.py
- /verify/TestCase/AOJ/GRL_6_B.test.py.html
title: TestCase/AOJ/GRL_6_B.test.py
---
