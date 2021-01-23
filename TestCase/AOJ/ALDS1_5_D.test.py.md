---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\BinaryIndexedTree\inversion_number.py
    title: DataStructure\BinaryIndexedTree\inversion_number.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_D
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_D
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_5_D\r\
    \nimport sys\r\ninput = sys.stdin.readline\r\n\r\nfrom DataStructure.BinaryIndexedTree.inversion_number\
    \ import inversion_number\r\n\r\n\r\ndef main():\r\n    n = int(input())\r\n \
    \   a = list(map(int, input().split()))\r\n\r\n    print(inversion_number(a))\r\
    \n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\n\r\n"
  dependsOn:
  - DataStructure\BinaryIndexedTree\inversion_number.py
  isVerificationFile: true
  path: TestCase\AOJ\ALDS1_5_D.test.py
  requiredBy: []
  timestamp: '2021-01-02 16:13:46+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\ALDS1_5_D.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\ALDS1_5_D.test.py
- /verify\TestCase\AOJ\ALDS1_5_D.test.py.html
title: TestCase\AOJ\ALDS1_5_D.test.py
---
