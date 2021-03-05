---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import random\n\n\ndef fermat_test(n, rep=100):\n    def gcd(a, b):\n   \
    \     while b:\n            a, b = b, a % b\n        return a\n\n    if n == 1:\n\
    \        return False\n    if n == 2:\n        return True\n    for _ in range(rep):\n\
    \        a = random.randint(2, n - 1)\n        if gcd(a, n) != 1:\n          \
    \  # a \u3068 n \u304C\u4E92\u3044\u306B\u7D20\u3067\u306F\u306A\u3044\u6642\u70B9\
    \u3067 n \u306F\u5408\u6210\u6570\n            # \u30AB\u30FC\u30DE\u30A4\u30B1\
    \u30EB\u6570\u3092\u7D20\u6570\u3068\u8AA4\u5224\u5B9A\u3055\u305B\u308B\u305F\
    \u3081\u306B continue \u3057\u3066\u3044\u308B\n            continue\n       \
    \ if pow(a, n - 1, n) != 1:\n            return False\n    return True\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/Prime/fermat_test.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: NumberTheory/Prime/fermat_test.py
layout: document
redirect_from:
- /library/NumberTheory/Prime/fermat_test.py
- /library/NumberTheory/Prime/fermat_test.py.html
title: NumberTheory/Prime/fermat_test.py
---
