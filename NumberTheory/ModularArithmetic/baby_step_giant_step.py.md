---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase/LibraryChecker/discrete_logarithm_mod.test.py
    title: TestCase/LibraryChecker/discrete_logarithm_mod.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.2/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "def baby_step_giant_step(x, y, MOD):\n    def gcd(a, b):\n        while b:\n\
    \            a, b = b, a % b\n        return a\n\n    x %= MOD\n    y %= MOD\n\
    \    k, add, g = 1, 0, gcd(x, MOD)\n    while g > 1:\n        if y == k:\n   \
    \         return add\n        if y % g:\n            return -1\n        y //=\
    \ g\n        MOD //= g\n        add += 1\n        k = (k * x // g) % MOD\n   \
    \     g = gcd(x, MOD)\n\n    sqrtMOD = int(MOD ** 0.5) + 1\n    baby = {}\n  \
    \  cur = y\n    for i in range(sqrtMOD + 1):\n        baby[cur] = i\n        cur\
    \ = (cur * x) % MOD\n\n    xpow = pow(x, sqrtMOD, MOD)\n    cur = k\n    for i\
    \ in range(1, sqrtMOD + 1):\n        cur = (cur * xpow) % MOD\n        if cur\
    \ in baby:\n            return sqrtMOD * i - baby[cur] + add\n\n    return -1\n"
  dependsOn: []
  isVerificationFile: false
  path: NumberTheory/ModularArithmetic/baby_step_giant_step.py
  requiredBy: []
  timestamp: '2021-03-07 00:19:35+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase/LibraryChecker/discrete_logarithm_mod.test.py
documentation_of: NumberTheory/ModularArithmetic/baby_step_giant_step.py
layout: document
redirect_from:
- /library/NumberTheory/ModularArithmetic/baby_step_giant_step.py
- /library/NumberTheory/ModularArithmetic/baby_step_giant_step.py.html
title: NumberTheory/ModularArithmetic/baby_step_giant_step.py
---
