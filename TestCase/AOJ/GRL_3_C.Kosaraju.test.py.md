---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\Decomposition\SCC_Kosaraju.py
    title: "\u5F37\u9023\u7D50\u6210\u5206\u5206\u89E3 (Kosaraju\u306E\u30A2\u30EB\
      \u30B4\u30EA\u30BA\u30E0)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_C
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_C\r\
    \nimport sys\r\nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom Graph.Decomposition.SCC_Kosaraju\
    \ import StronglyConnectedComponents\r\n\r\n\r\ndef main():\r\n    n, m = map(int,\
    \ input().split())\r\n    edges = [list(map(int, input().split())) for i in range(m)]\r\
    \n    q = int(input())\r\n    queries = [list(map(int, input().split())) for i\
    \ in range(q)]\r\n\r\n    scc = StronglyConnectedComponents(n)\r\n    for v, nxt_v\
    \ in edges:\r\n        scc.add_edge(v, nxt_v)\r\n    scc.build()\r\n\r\n    ans\
    \ = []\r\n    for u, v in queries:\r\n        ans.append(int(scc.labels[u] ==\
    \ scc.labels[v]))\r\n\r\n    print('\\n'.join(map(str, ans)))\r\n\r\n\r\nif __name__\
    \ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - Graph\Decomposition\SCC_Kosaraju.py
  isVerificationFile: true
  path: TestCase\AOJ\GRL_3_C.Kosaraju.test.py
  requiredBy: []
  timestamp: '2021-01-09 01:19:33+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\GRL_3_C.Kosaraju.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\GRL_3_C.Kosaraju.test.py
- /verify\TestCase\AOJ\GRL_3_C.Kosaraju.test.py.html
title: TestCase\AOJ\GRL_3_C.Kosaraju.test.py
---
