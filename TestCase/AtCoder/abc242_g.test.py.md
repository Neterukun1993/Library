---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: misc/mo_algorithm.py
    title: misc/mo_algorithm.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://atcoder.jp/contests/abc242/tasks/abc242_g
    links:
    - https://atcoder.jp/contests/abc242/tasks/abc242_g
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://atcoder.jp/contests/abc242/tasks/abc242_g\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom misc.mo_algorithm import\
    \ mo_algorithm\n\n\ndef main():\n    n = int(input())\n    a = list(map(int, input().split()))\n\
    \    q = int(input())\n    queries = [list(map(int, input().split())) for i in\
    \ range(q)]\n\n    cnt = [0]\n    count = [0] * (n + 1)\n\n    def add(x):\n \
    \       cnt[0] += count[a[x]]\n        count[a[x]] ^= 1\n\n    def rem(x):\n \
    \       count[a[x]] ^= 1\n        cnt[0] -= count[a[x]]\n\n    def get():\n  \
    \      return cnt[0]\n\n    ans = mo_algorithm(\n        n, q, [(l - 1, r) for\
    \ l, r in queries],\n        add, add, rem, rem, get\n    )\n\n    for res in\
    \ ans:\n        print(res)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - misc/mo_algorithm.py
  isVerificationFile: true
  path: TestCase/AtCoder/abc242_g.test.py
  requiredBy: []
  timestamp: '2023-03-12 18:21:59+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AtCoder/abc242_g.test.py
layout: document
redirect_from:
- /verify/TestCase/AtCoder/abc242_g.test.py
- /verify/TestCase/AtCoder/abc242_g.test.py.html
title: TestCase/AtCoder/abc242_g.test.py
---
