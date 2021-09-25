---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Convolution/multiple_divisor_transform.py
    title: "\u7D04\u6570/\u500D\u6570\u3092\u96C6\u5408\u3068\u3057\u305F\u7D2F\u7A4D\
      \u548C/\u5DEE\u5206"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.Convolution.multiple_divisor_transform\
    \ import (\n    multiple_zeta_transform,\n    multiple_mobius_transform,\n   \
    \ divisor_zeta_transform,\n    divisor_mobius_transform\n)\n\n\ndef naive_count_divisors(n):\n\
    \    \"\"\"O(N^2) naive calculation\"\"\"\n    res = [0] * n\n    for val in range(1,\
    \ n):\n        for div in range(1, val + 1):\n            if val % div == 0:\n\
    \                res[val] += 1\n    return res\n\n\ndef naive_count_multiples(n):\n\
    \    \"\"\"O(N^2) naive calculation\"\"\"\n    res = [0] * n\n    for div in range(1,\
    \ n):\n        for val in range(div, n):\n            if val % div == 0:\n   \
    \             res[div] += 1\n    return res\n\n\ndef test(n):\n    op = lambda\
    \ x, y: x + y\n    inv = lambda x: -x\n\n    arr = [1] * n\n    arr[0] = 0\n\n\
    \    mul_zeta = multiple_zeta_transform(arr, op)\n    naive_mul_cnt = naive_count_multiples(n)\n\
    \    assert(mul_zeta == naive_mul_cnt)\n\n    div_zeta = divisor_zeta_transform(arr,\
    \ op)\n    naive_div_cnt = naive_count_divisors(n)\n    assert(div_zeta == naive_div_cnt)\n\
    \n    mul_mobius = multiple_mobius_transform(mul_zeta, op, inv)\n    assert(arr\
    \ == mul_mobius)\n\n    div_mobius = divisor_mobius_transform(div_zeta, op, inv)\n\
    \    assert(arr == div_mobius)\n\n\ndef main():\n    test(1000)\n\n\nif __name__\
    \ == '__main__':\n    main()\n    print(\"Hello World\")\n"
  dependsOn:
  - NumberTheory/Convolution/multiple_divisor_transform.py
  isVerificationFile: true
  path: TestCase/unittest/multiple_divisor_transform.unittest.test.py
  requiredBy: []
  timestamp: '2021-06-21 06:14:17+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/multiple_divisor_transform.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/multiple_divisor_transform.unittest.test.py
- /verify/TestCase/unittest/multiple_divisor_transform.unittest.test.py.html
title: TestCase/unittest/multiple_divisor_transform.unittest.test.py
---
