---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/Basic/extended_gcd.py
    title: "\u62E1\u5F35\u30E6\u30FC\u30AF\u30EA\u30C3\u30C9\u306E\u4E92\u9664\u6CD5"
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
  code: "from NumberTheory.Basic.extended_gcd import extended_gcd\n\n\ndef linear_congruence(a,\
    \ b, m):\n    def gcd(a, b):\n        while b:\n            a, b = b, a % b\n\
    \        return a\n\n    if b % gcd(a, m) != 0:\n        # \u89E3\u306A\u3057\n\
    \        return False, -1, -1\n    g, x, y = extended_gcd(a, m)\n    x *= b //\
    \ g\n    cycle = m // g\n    x -= cycle * (x // cycle)\n    return True, x, cycle\n"
  dependsOn:
  - NumberTheory/Basic/extended_gcd.py
  isVerificationFile: false
  path: NumberTheory/ModularArithmetic/linear_congruence.py
  requiredBy: []
  timestamp: '2021-03-07 01:51:55+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: NumberTheory/ModularArithmetic/linear_congruence.py
layout: document
redirect_from:
- /library/NumberTheory/ModularArithmetic/linear_congruence.py
- /library/NumberTheory/ModularArithmetic/linear_congruence.py.html
title: NumberTheory/ModularArithmetic/linear_congruence.py
---
