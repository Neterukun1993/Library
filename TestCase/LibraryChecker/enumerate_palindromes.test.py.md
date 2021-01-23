---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: String\Manacher.py
    title: String\Manacher.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/enumerate_palindromes
    links:
    - https://judge.yosupo.jp/problem/enumerate_palindromes
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/enumerate_palindromes\r\
    \nimport sys\r\ninput = sys.stdin.readline\r\n\r\nfrom String.Manacher import\
    \ Manacher\r\n\r\n\r\ndef main():\r\n    s = input().replace('\\n', '')\r\n  \
    \  mn = Manacher(s)\r\n\r\n    print(*mn.len_p[1:-1])\r\n\r\n\r\nif __name__ ==\
    \ '__main__':\r\n    main()\r\n"
  dependsOn:
  - String\Manacher.py
  isVerificationFile: true
  path: TestCase\LibraryChecker\enumerate_palindromes.test.py
  requiredBy: []
  timestamp: '2021-01-06 00:03:29+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\LibraryChecker\enumerate_palindromes.test.py
layout: document
redirect_from:
- /verify\TestCase\LibraryChecker\enumerate_palindromes.test.py
- /verify\TestCase\LibraryChecker\enumerate_palindromes.test.py.html
title: TestCase\LibraryChecker\enumerate_palindromes.test.py
---
