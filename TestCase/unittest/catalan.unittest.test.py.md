---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Combination/catalan.py
    title: "\u30AB\u30BF\u30E9\u30F3\u6570"
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
    import sys\ninput = sys.stdin.buffer.readline\n\nimport itertools\nfrom Combination.catalan\
    \ import catalan, catalan_trapezoid\n\n\ndef naive_catalan(n):\n    \"\"\"DFS\
    \ naive calculation\"\"\"\n    def dfs(cnt_pl, cnt_mi):\n        if cnt_pl > n\
    \ or cnt_mi > n or cnt_pl < cnt_mi:\n            return 0\n        if cnt_pl ==\
    \ n and cnt_mi == n:\n            return 1\n        return dfs(cnt_pl + 1, cnt_mi)\
    \ + dfs(cnt_pl, cnt_mi + 1)\n\n    return dfs(0, 0)\n\n\ndef naive_catalan_trapezoid(n,\
    \ k, m):\n    \"\"\"DFS naive calculation\"\"\"\n    def dfs(cnt_pl, cnt_mi):\n\
    \        if cnt_pl > n or cnt_mi > k or cnt_pl + (m - 1) < cnt_mi:\n         \
    \   return 0\n        if cnt_pl == n and cnt_mi == k:\n            return 1\n\
    \        return dfs(cnt_pl + 1, cnt_mi) + dfs(cnt_pl, cnt_mi + 1)\n\n    return\
    \ dfs(0, 0)\n\n\ndef main():\n    for n in range(10):\n        assert(catalan(n)\
    \ == naive_catalan(n))\n\n    for n in range(5):\n        for k in range(5):\n\
    \            for m in range(5):\n                assert(catalan_trapezoid(n, k,\
    \ m)\n                       == naive_catalan_trapezoid(n, k, m))\n\n\nif __name__\
    \ == '__main__':\n    main()\n    print(\"Hello World\")\n"
  dependsOn:
  - Combination/catalan.py
  isVerificationFile: true
  path: TestCase/unittest/catalan.unittest.test.py
  requiredBy: []
  timestamp: '2021-09-04 15:01:27+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/catalan.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/catalan.unittest.test.py
- /verify/TestCase/unittest/catalan.unittest.test.py.html
title: TestCase/unittest/catalan.unittest.test.py
---
