---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/LowLink.py
    title: "\u95A2\u7BC0\u70B9\u30FB\u6A4B\u306E\u5217\u6319\u3001DFS\u6728\u306E\u69CB\
      \u7BC9 (LowLink)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_B\n\
    import sys\ninput = sys.stdin.readline\n\nfrom Graph.LowLink import LowLink\n\n\
    \ndef main():\n    n, m = map(int, input().split())\n    edges = [list(map(int,\
    \ input().split())) for i in range(m)]\n\n    ll = LowLink(n)\n    for u, v in\
    \ edges:\n        ll.add_edge(u, v)\n\n    ll.build()\n    bs = [(u, v) if u <\
    \ v else (v, u) for u, v in ll.enumerate_bridges()]\n    for u, v in sorted(bs):\n\
    \        print(u, v)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/LowLink.py
  isVerificationFile: true
  path: TestCase/AOJ/GRL_3_B.test.py
  requiredBy: []
  timestamp: '2021-01-10 06:06:37+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_3_B.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_3_B.test.py
- /verify/TestCase/AOJ/GRL_3_B.test.py.html
title: TestCase/AOJ/GRL_3_B.test.py
---
