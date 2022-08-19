---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: String/run_length_encoding.py
    title: "\u30E9\u30F3\u30EC\u30F3\u30B0\u30B9\u5727\u7E2E"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom String.run_length_encoding\
    \ import encoding\n\n\ndef test(string):\n    comp = encoding(string)\n    res\
    \ = \"\"\n    for char, cnt in comp:\n        res += char * cnt\n    assert(res\
    \ == string)\n\n\ndef main():\n    string = \"\"\n    test(string)\n\n    string\
    \ = \"A\"\n    test(string)\n\n    string = \"AAAAA\"\n    test(string)\n\n  \
    \  string = \"AABA\"\n    test(string)\n\n    string = \"AABBAABB\"\n\n    string\
    \ = \"ABCDE\"\n    test(string)\n\n\nif __name__ == '__main__':\n    main()\n\
    \    print(\"Hello World\")\n"
  dependsOn:
  - String/run_length_encoding.py
  isVerificationFile: true
  path: TestCase/unittest/run_length_encoding.unittest.test.py
  requiredBy: []
  timestamp: '2021-05-07 02:19:56+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/run_length_encoding.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/run_length_encoding.unittest.test.py
- /verify/TestCase/unittest/run_length_encoding.unittest.test.py.html
title: TestCase/unittest/run_length_encoding.unittest.test.py
---
