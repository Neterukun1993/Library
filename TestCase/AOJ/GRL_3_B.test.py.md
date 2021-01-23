---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\LowLink.py
    title: "\u95A2\u7BC0\u70B9\u30FB\u6A4B\u306E\u5217\u6319\u3001DFS\u6728\u306E\u69CB\
      \u7BC9 (LowLink)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_B
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_B\r\
    \nimport sys\r\ninput = sys.stdin.readline\r\n\r\nfrom Graph.LowLink import LowLink\r\
    \n\r\n\r\ndef main():\r\n    n, m = map(int, input().split())\r\n    edges = [list(map(int,\
    \ input().split())) for i in range(m)]\r\n\r\n    ll = LowLink(n)\r\n    for u,\
    \ v in edges:\r\n        ll.add_edge(u, v)\r\n\r\n    ll.build()\r\n    bs = [(u,\
    \ v) if u < v else (v, u) for u, v in ll.enumerate_bridges()]\r\n    for u, v\
    \ in sorted(bs):\r\n        print(u, v)\r\n\r\n\r\nif __name__ == '__main__':\r\
    \n    main()\r\n"
  dependsOn:
  - Graph\LowLink.py
  isVerificationFile: true
  path: TestCase\AOJ\GRL_3_B.test.py
  requiredBy: []
  timestamp: '2021-01-10 06:06:37+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\GRL_3_B.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\GRL_3_B.test.py
- /verify\TestCase\AOJ\GRL_3_B.test.py.html
title: TestCase\AOJ\GRL_3_B.test.py
---
