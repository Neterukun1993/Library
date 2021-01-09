---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/TwoSAT.py
    title: 2-SAT
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/two_sat
    links:
    - https://judge.yosupo.jp/problem/two_sat
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/two_sat\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.TwoSAT import TwoSAT\n\
    \n\ndef main():\n    p, cfn, n, m = input().split()\n    n, m = int(n), int(m)\n\
    \    info = [list(map(int, input().split())) for i in range(m)]\n\n    ts = TwoSAT(n)\n\
    \    for i, j, _ in info:\n        f, g = True, True\n        if i < 0:\n    \
    \        i = -i\n            f = False\n        if j < 0:\n            j = -j\n\
    \            g = False\n        i -= 1\n        j -= 1\n        ts.add_clause(i,\
    \ f, j, g)\n\n    flag = ts.satisfy()\n    if flag:\n        print(\"s\", \"SATISFIABLE\"\
    )\n        res = ts.answer()\n        print(\"v\", *[(i + 1) if b else -(i + 1)\
    \ for i, b in enumerate(res)], 0)\n    else:\n        print(\"s\", \"UNSATISFIABLE\"\
    )\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/TwoSAT.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/two_sat.test.py
  requiredBy: []
  timestamp: '2021-01-10 04:02:27+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/two_sat.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/two_sat.test.py
- /verify/TestCase/LibraryChecker/two_sat.test.py.html
title: TestCase/LibraryChecker/two_sat.test.py
---
