---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: DataStructure/AccumulateSum/Imos.py
    title: "\u3044\u3082\u3059\u6CD5"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_5_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.AccumulateSum.Imos\
    \ import Imos\n\n\ndef main():\n    n, t = map(int, input().split())\n    queries\
    \ = [list(map(int, input().split())) for i in range(n)]\n\n    imos = Imos(10\
    \ ** 5)\n    for l, r in queries:\n        imos.add(l, r, 1)\n    imos.build()\n\
    \n    ans = 0\n    for i in range(10 ** 5):\n        ans = max(imos[i], ans)\n\
    \    print(ans)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/AccumulateSum/Imos.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_5_A.test.py
  requiredBy: []
  timestamp: '2021-01-02 06:20:11+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_5_A.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_5_A.test.py
- /verify/TestCase/AOJ/DSL_5_A.test.py.html
title: TestCase/AOJ/DSL_5_A.test.py
---
