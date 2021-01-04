---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/misc/SparseTable.py
    title: DataStructure/misc/SparseTable.py
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: https://judge.yosupo.jp/problem/staticrmq
    links:
    - https://judge.yosupo.jp/problem/staticrmq
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM https://judge.yosupo.jp/problem/staticrmq\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.misc.SparseTable\
    \ import SparseTable\n\n\ndef main():\n    n, q = map(int, input().split())\n\
    \    a = list(map(int, input().split()))\n    queries = [list(map(int, input().split()))\
    \ for _ in range(q)]\n\n    st = SparseTable(a, min)\n    ans = []\n    for l,\
    \ r in queries:\n        ans.append(st.fold(l, r))\n\n    print('\\n'.join(map(str,\
    \ ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/misc/SparseTable.py
  isVerificationFile: true
  path: TestCase/LibraryChecker/staticrmq.test.py
  requiredBy: []
  timestamp: '2021-01-03 11:00:07+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/LibraryChecker/staticrmq.test.py
layout: document
redirect_from:
- /verify/TestCase/LibraryChecker/staticrmq.test.py
- /verify/TestCase/LibraryChecker/staticrmq.test.py.html
title: TestCase/LibraryChecker/staticrmq.test.py
---