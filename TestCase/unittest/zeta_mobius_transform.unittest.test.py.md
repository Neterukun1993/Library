---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Convolution/mobius_transform.py
    title: "\u9AD8\u901F\u30E1\u30D3\u30A6\u30B9\u5909\u63DB (fast m\xF6bius transform)"
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Convolution/zeta_transform.py
    title: "\u9AD8\u901F\u30BC\u30FC\u30BF\u5909\u63DB (fast zeta transform)"
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
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.1/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.Convolution.zeta_transform\
    \ import subset_zeta_transform, superset_zeta_transform\nfrom NumberTheory.Convolution.mobius_transform\
    \ import subset_mobius_transform, superset_mobius_transform\nfrom misc.xorshift\
    \ import xorshift32\n\n\ndef naive_subset_zeta_transform(a, op):\n    \"\"\"O(N^2)\
    \ naive calculation\"\"\"\n    n = len(a)\n    res = a[:]\n    for i in range(n):\n\
    \        for j in range(n):\n            if i != j and i & j == j:\n         \
    \       res[i] = op(res[i], a[j])\n    return res\n\n\ndef naive_superset_zeta_transform(a,\
    \ op):\n    \"\"\"O(N^2) naive calculation\"\"\"\n    n = len(a)\n    res = a[:]\n\
    \    for i in range(n):\n        for j in range(n):\n            if i != j and\
    \ i | j == j:\n                res[i] = op(res[i], a[j])\n    return res\n\n\n\
    def group_test(arr, op, inv):\n    sub_zeta = subset_zeta_transform(arr, op)\n\
    \    naive_sub_zeta = naive_subset_zeta_transform(arr, op)\n    assert(sub_zeta\
    \ == naive_sub_zeta)\n\n    sup_zeta = superset_zeta_transform(arr, op)\n    naive_sup_zeta\
    \ = naive_superset_zeta_transform(arr, op)\n    assert(sup_zeta == naive_sup_zeta)\n\
    \n    sub_mobius = subset_mobius_transform(sub_zeta, op, inv)\n    assert(arr\
    \ == sub_mobius)\n\n    sup_mobius = superset_mobius_transform(sup_zeta, op, inv)\n\
    \    assert(arr == sup_mobius)\n\n\ndef monoid_test(arr, op):\n    sub_zeta =\
    \ subset_zeta_transform(arr, op)\n    naive_sub_zeta = naive_subset_zeta_transform(arr,\
    \ op)\n    assert(sub_zeta == naive_sub_zeta)\n\n    sup_zeta = superset_zeta_transform(arr,\
    \ op)\n    naive_sup_zeta = naive_superset_zeta_transform(arr, op)\n    assert(sup_zeta\
    \ == naive_sup_zeta)\n\n\ndef main():\n    rand32 = xorshift32()\n    arr = [rand32()\
    \ for i in range(1000)]\n\n    op = lambda x, y: x + y\n    inv = lambda x: -x\n\
    \    group_test(arr, op, inv)\n\n    monoid_test(arr, max)\n\n\nif __name__ ==\
    \ '__main__':\n    main()\n    print(\"Hello World\")\n"
  dependsOn:
  - NumberTheory/Convolution/zeta_transform.py
  - NumberTheory/Convolution/mobius_transform.py
  - misc/xorshift.py
  isVerificationFile: true
  path: TestCase/unittest/zeta_mobius_transform.unittest.test.py
  requiredBy: []
  timestamp: '2021-06-20 22:49:02+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/zeta_mobius_transform.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/zeta_mobius_transform.unittest.test.py
- /verify/TestCase/unittest/zeta_mobius_transform.unittest.test.py.html
title: TestCase/unittest/zeta_mobius_transform.unittest.test.py
---
