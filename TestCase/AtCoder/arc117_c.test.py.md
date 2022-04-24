---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Combination/LucasTheorem.py
    title: "Lucas \u306E\u5B9A\u7406"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/arc117/tasks/arc117_c
    links:
    - https://atcoder.jp/contests/arc117/tasks/arc117_c
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.4/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/arc117/tasks/arc117_c\n\
    import sys\ninput = sys.stdin.readline\n\nfrom Combination.LucasTheorem import\
    \ LucasTheorem\n\n\ndef main():\n    value = {\"B\": 0, \"W\": 1, \"R\": 2}\n\
    \    ans = [\"B\", \"W\", \"R\"]\n    n = int(input())\n    s = input()[:-1]\n\
    \n    lt = LucasTheorem(3)\n    res = 0\n    for i, si in enumerate(s):\n    \
    \    res += lt.comb(n - 1, i) * value[si]\n        res %= 3\n\n    if n % 2 ==\
    \ 0:\n        res = (-res) % 3\n\n    print(ans[res])\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - Combination/LucasTheorem.py
  isVerificationFile: true
  path: TestCase/AtCoder/arc117_c.test.py
  requiredBy: []
  timestamp: '2021-09-13 00:46:50+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AtCoder/arc117_c.test.py
layout: document
redirect_from:
- /verify/TestCase/AtCoder/arc117_c.test.py
- /verify/TestCase/AtCoder/arc117_c.test.py.html
title: TestCase/AtCoder/arc117_c.test.py
---
