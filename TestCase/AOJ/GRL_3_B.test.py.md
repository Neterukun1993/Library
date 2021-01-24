---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=GRL_3_B\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.misc.LowLink import\
    \ LowLink\n\n\ndef main():\n    n, m = map(int, input().split())\n    edges =\
    \ [list(map(int, input().split())) for i in range(m)]\n\n    ll = LowLink(n)\n\
    \    for u, v in edges:\n        ll.add_edge(u, v)\n\n    ll.build()\n    bs =\
    \ [(u, v) if u < v else (v, u) for u, v in ll.enumerate_bridges()]\n    for u,\
    \ v in sorted(bs):\n        print(u, v)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn: []
  isVerificationFile: true
  path: TestCase/AOJ/GRL_3_B.test.py
  requiredBy: []
  timestamp: '2021-01-24 18:01:48+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: TestCase/AOJ/GRL_3_B.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/GRL_3_B.test.py
- /verify/TestCase/AOJ/GRL_3_B.test.py.html
title: TestCase/AOJ/GRL_3_B.test.py
---
