---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: Graph/misc/cycle_detection.py
    title: "\u30B5\u30A4\u30AF\u30EB\u691C\u51FA"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_4_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.misc.cycle_detection\
    \ import cycle_detection\n\n\ndef main():\n    n, m = map(int, input().split())\n\
    \    edges = [list(map(int, input().split())) for i in range(m)]\n\n    graph\
    \ = [[] for i in range(n)]\n    for u, v in edges:\n        graph[u].append(v)\n\
    \n    cycle = cycle_detection(graph)\n    if cycle:\n        print(1)\n    else:\n\
    \        print(0)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/misc/cycle_detection.py
  isVerificationFile: true
  path: TestCase/AOJ/GRL_4_A.test.py
  requiredBy: []
  timestamp: '2021-01-14 17:41:58+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_4_A.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_4_A.test.py
- /verify/TestCase/AOJ/GRL_4_A.test.py.html
title: TestCase/AOJ/GRL_4_A.test.py
---
