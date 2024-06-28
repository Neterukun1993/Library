---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/misc/FoldableQueue.py
    title: Foldable Queue
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_D
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_D\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.misc.FoldableQueue\
    \ import FoldableQueue\n\n\ndef main():\n    n, l = map(int, input().split())\n\
    \    a = list(map(int, input().split()))\n\n    fq = FoldableQueue(min)\n    for\
    \ i in range(l - 1):\n        fq.append(a[i])\n\n    ans = []\n    for i in range(l\
    \ - 1, n):\n        fq.append(a[i])\n        ans.append(fq.all_fold())\n     \
    \   fq.popleft()\n\n    print(*ans)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/misc/FoldableQueue.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_3_D.test.py
  requiredBy: []
  timestamp: '2022-09-12 02:00:29+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_3_D.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_3_D.test.py
- /verify/TestCase/AOJ/DSL_3_D.test.py.html
title: TestCase/AOJ/DSL_3_D.test.py
---
