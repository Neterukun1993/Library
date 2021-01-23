---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Combination\modinv_combination.py
    title: "MOD\u4E0A\u3067\u306E\u7D44\u5408\u305B\u8A08\u7B97"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_E
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_E
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DPL_5_E\r\
    \nimport sys\r\ninput = sys.stdin.readline\r\n\r\nfrom Combination.modinv_combination\
    \ import combination\r\n\r\n\r\ndef main():\r\n    n, k = map(int, input().split())\r\
    \n    MOD = 10 ** 9 + 7\r\n    if n > k:\r\n        print(0)\r\n    else:\r\n\
    \        print(combination(k, n, MOD))\r\n\r\n\r\nif __name__ == '__main__':\r\
    \n    main()\r\n"
  dependsOn:
  - Combination\modinv_combination.py
  isVerificationFile: true
  path: TestCase\AOJ\DPL_5_E.naive.test.py
  requiredBy: []
  timestamp: '2021-01-06 00:51:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\DPL_5_E.naive.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\DPL_5_E.naive.test.py
- /verify\TestCase\AOJ\DPL_5_E.naive.test.py.html
title: TestCase\AOJ\DPL_5_E.naive.test.py
---
