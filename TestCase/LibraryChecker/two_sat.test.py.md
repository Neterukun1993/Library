---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph\TwoSAT.py
    title: 2-SAT
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/two_sat
    links:
    - https://judge.yosupo.jp/problem/two_sat
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_sat\r\n\
    import sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom Graph.TwoSAT import\
    \ TwoSAT\r\n\r\n\r\ndef main():\r\n    p, cfn, n, m = input().split()\r\n    n,\
    \ m = int(n), int(m)\r\n    info = [list(map(int, input().split())) for i in range(m)]\r\
    \n\r\n    ts = TwoSAT(n)\r\n    for i, j, _ in info:\r\n        f, g = True, True\r\
    \n        if i < 0:\r\n            i = -i\r\n            f = False\r\n       \
    \ if j < 0:\r\n            j = -j\r\n            g = False\r\n        i -= 1\r\
    \n        j -= 1\r\n        ts.add_clause(i, f, j, g)\r\n\r\n    flag = ts.satisfy()\r\
    \n    if flag:\r\n        print(\"s\", \"SATISFIABLE\")\r\n        res = ts.answer()\r\
    \n        print(\"v\", *[(i + 1) if b else -(i + 1) for i, b in enumerate(res)],\
    \ 0)\r\n    else:\r\n        print(\"s\", \"UNSATISFIABLE\")\r\n\r\n\r\nif __name__\
    \ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - Graph\TwoSAT.py
  isVerificationFile: true
  path: TestCase\LibraryChecker\two_sat.test.py
  requiredBy: []
  timestamp: '2021-01-10 04:02:27+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\LibraryChecker\two_sat.test.py
layout: document
redirect_from:
- /verify\TestCase\LibraryChecker\two_sat.test.py
- /verify\TestCase\LibraryChecker\two_sat.test.py.html
title: TestCase\LibraryChecker\two_sat.test.py
---
