---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/misc/LowLink.py
    title: "\u95A2\u7BC0\u70B9\u30FB\u6A4B\u306E\u5217\u6319\u3001DFS \u6728\u306E\
      \u69CB\u7BC9 (Low Link)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.4/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.misc.LowLink import\
    \ LowLink\n\n\ndef main():\n    n, m = map(int, input().split())\n    edges =\
    \ [list(map(int, input().split())) for i in range(m)]\n\n    ll = LowLink(n)\n\
    \    for u, v in edges:\n        ll.add_edge(u, v)\n\n    ll.build()\n    for\
    \ v in sorted(ll.enumerate_articulations()):\n        print(v)\n\n\nif __name__\
    \ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/misc/LowLink.py
  isVerificationFile: true
  path: TestCase/AOJ/GRL_3_A.test.py
  requiredBy: []
  timestamp: '2021-01-25 22:00:12+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_3_A.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_3_A.test.py
- /verify/TestCase/AOJ/GRL_3_A.test.py.html
title: TestCase/AOJ/GRL_3_A.test.py
---
