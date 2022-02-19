---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/AccumulateSum/AccumulateSumLR.py
    title: "\u5DE6\u53F3\u304B\u3089\u306E\u7D2F\u7A4D\u548C"
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
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.AccumulateSum.AccumulateSumLR\
    \ import AccumulateSumLR\n\n\ndef bruteforce_test(array, n):\n    acc_lr = AccumulateSumLR(array,\
    \ min, n)\n    for r in range(1, n + 1):\n        assert(acc_lr.left_fold(r) ==\
    \ min(array[:r]))\n    for l in range(n):\n        assert(acc_lr.right_fold(l)\
    \ == min(array[l:]))\n    for i in range(n):\n        val = n\n        if i !=\
    \ 0:\n            val = min(min(array[0:i]), val)\n        if i != n - 1:\n  \
    \          val = min(min(array[i + 1:n]), val)\n        assert(acc_lr.fold(i)\
    \ == val)\n\n\ndef test_asc():\n    n = 100\n    array = [i for i in range(n)]\n\
    \    bruteforce_test(array, n)\n\n\ndef test_desc():\n    n = 100\n    array =\
    \ [i for i in reversed(range(n))]\n    bruteforce_test(array, n)\n\n\ndef main():\n\
    \    test_asc()\n    test_desc()\n\n\nif __name__ == '__main__':\n    main()\n\
    \    print(\"Hello World\")\n"
  dependsOn:
  - DataStructure/AccumulateSum/AccumulateSumLR.py
  isVerificationFile: true
  path: TestCase/unittest/AccumulateSumLR.unittest.test.py
  requiredBy: []
  timestamp: '2021-05-05 21:41:55+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/AccumulateSumLR.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/AccumulateSumLR.unittest.test.py
- /verify/TestCase/unittest/AccumulateSumLR.unittest.test.py.html
title: TestCase/unittest/AccumulateSumLR.unittest.test.py
---
