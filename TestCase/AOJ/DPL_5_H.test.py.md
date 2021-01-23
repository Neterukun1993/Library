---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Combination\twelvefold_way.py
    title: "\u5199\u50CF12\u76F8"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_H
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_H
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_H\r\
    \nimport sys\r\ninput = sys.stdin.readline\r\n\r\nfrom Combination.twelvefold_way\
    \ import way8\r\n\r\n\r\ndef main():\r\n    n, k = map(int, input().split())\r\
    \n    print(way8(n, k))\r\n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - Combination\twelvefold_way.py
  isVerificationFile: true
  path: TestCase\AOJ\DPL_5_H.test.py
  requiredBy: []
  timestamp: '2021-01-02 20:38:41+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\DPL_5_H.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\DPL_5_H.test.py
- /verify\TestCase\AOJ\DPL_5_H.test.py.html
title: TestCase\AOJ\DPL_5_H.test.py
---
