---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: NumberTheory/ModularArithmetic/baby_step_giant_step.py
    title: "\u96E2\u6563\u5BFE\u6570 (Baby-step giant-step)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/discrete_logarithm_mod
    links:
    - https://judge.yosupo.jp/problem/discrete_logarithm_mod
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/discrete_logarithm_mod\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom NumberTheory.ModularArithmetic.baby_step_giant_step\
    \ import baby_step_giant_step\n\n\ndef main():\n    t = int(input())\n    info\
    \ = [list(map(int, input().split())) for i in range(t)]\n\n    for x, y, m in\
    \ info:\n        print(baby_step_giant_step(x, y, m))\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - NumberTheory/ModularArithmetic/baby_step_giant_step.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/discrete_logarithm_mod.test.py
  requiredBy: []
  timestamp: '2021-03-07 00:19:35+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/discrete_logarithm_mod.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/discrete_logarithm_mod.test.py
- /verify/TestCase/LibraryChecker/discrete_logarithm_mod.test.py.html
title: TestCase/LibraryChecker/discrete_logarithm_mod.test.py
---
