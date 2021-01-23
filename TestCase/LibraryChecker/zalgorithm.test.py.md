---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: String\z_algorithm.py
    title: Z algorithm
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/zalgorithm
    links:
    - https://judge.yosupo.jp/problem/zalgorithm
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/zalgorithm\r\
    \nimport sys\r\ninput = sys.stdin.readline\r\n\r\nfrom String.z_algorithm import\
    \ z_algorithm\r\n\r\n\r\ndef main():\r\n    s = input().replace('\\n', '')\r\n\
    \    ans = z_algorithm(s)\r\n    print(*ans)\r\n\r\n\r\nif __name__ == '__main__':\r\
    \n    main()\r\n"
  dependsOn:
  - String\z_algorithm.py
  isVerificationFile: true
  path: TestCase\LibraryChecker\zalgorithm.test.py
  requiredBy: []
  timestamp: '2021-01-05 22:30:17+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\LibraryChecker\zalgorithm.test.py
layout: document
redirect_from:
- /verify\TestCase\LibraryChecker\zalgorithm.test.py
- /verify\TestCase\LibraryChecker\zalgorithm.test.py.html
title: TestCase\LibraryChecker\zalgorithm.test.py
---
