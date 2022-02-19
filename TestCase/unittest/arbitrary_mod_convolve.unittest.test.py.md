---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Convolution/arbitrary_mod_convolve.py
    title: "\u4EFB\u610F MOD \u7573\u307F\u8FBC\u307F"
  - icon: ':heavy_check_mark:'
    path: misc/xorshift.py
    title: "\u4E71\u6570\u751F\u6210 (Xorshift)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom misc.xorshift import xorshift32\n\
    from NumberTheory.Convolution.arbitrary_mod_convolve import arbitrary_mod_convolve\n\
    \n\nrand = xorshift32()\n\n\ndef check(a, b, MOD):\n    res1 = arbitrary_mod_convolve(a,\
    \ b, MOD)\n    res2 = [0] * (len(a) + len(b) - 1)\n    for i, va in enumerate(a):\n\
    \        for j, vb in enumerate(b):\n            res2[i + j] += va * vb\n    \
    \        res2[i + j] %= MOD\n    assert(res1 == res2)\n\n\ndef mod_2():\n    a\
    \ = [rand() for i in range(100)]\n    b = [rand() for i in range(100)]\n    MOD\
    \ = 2\n    check(a, b, MOD)\n\n\ndef mod_998244353():\n    a = [rand() for i in\
    \ range(100)]\n    b = [rand() for i in range(100)]\n    MOD = 10 ** 9 + 7\n \
    \   check(a, b, MOD)\n\n\ndef mod_1000000007():\n    a = [rand() for i in range(100)]\n\
    \    b = [rand() for i in range(100)]\n    MOD = 10 ** 9 + 7\n    check(a, b,\
    \ MOD)\n\n\ndef main():\n    for _ in range(100):\n        mod_2()\n        mod_998244353()\n\
    \        mod_1000000007()\n\n\nif __name__ == '__main__':\n    main()\n    print(\"\
    Hello World\")\n"
  dependsOn:
  - misc/xorshift.py
  - NumberTheory/Convolution/arbitrary_mod_convolve.py
  isVerificationFile: true
  path: TestCase/unittest/arbitrary_mod_convolve.unittest.test.py
  requiredBy: []
  timestamp: '2021-06-13 01:12:48+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/arbitrary_mod_convolve.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/arbitrary_mod_convolve.unittest.test.py
- /verify/TestCase/unittest/arbitrary_mod_convolve.unittest.test.py.html
title: TestCase/unittest/arbitrary_mod_convolve.unittest.test.py
---
