---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: Graph/Decomposition/SCC_Kosaraju.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3 (Kosaraju\u306E\u30A2\u30EB\
      \u30B4\u30EA\u30BA\u30E0)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_C\n\
    import sys\nimport sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.Decomposition.SCC_Kosaraju\
    \ import StronglyConnectedComponents\n\n\ndef main():\n    n, m = map(int, input().split())\n\
    \    edges = [list(map(int, input().split())) for i in range(m)]\n    q = int(input())\n\
    \    queries = [list(map(int, input().split())) for i in range(q)]\n\n    scc\
    \ = StronglyConnectedComponents(n)\n    for v, nxt_v in edges:\n        scc.add_edge(v,\
    \ nxt_v)\n    scc.build()\n\n    ans = []\n    for u, v in queries:\n        ans.append(int(scc.labels[u]\
    \ == scc.labels[v]))\n\n    print('\\n'.join(map(str, ans)))\n\n\nif __name__\
    \ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/Decomposition/SCC_Kosaraju.py
  isVerificationFile: true
  path: TestCase/AOJ/GRL_3_C.Kosaraju.test.py
  requiredBy: []
  timestamp: '2021-01-09 01:19:33+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_3_C.Kosaraju.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_3_C.Kosaraju.test.py
- /verify/TestCase/AOJ/GRL_3_C.Kosaraju.test.py.html
title: TestCase/AOJ/GRL_3_C.Kosaraju.test.py
---
