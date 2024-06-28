---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/misc/BootstrappedFoldableQueue.py
    title: "\u6C38\u7D9A Sliding Window Aggregation"
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
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.misc.BootstrappedFoldableQueue\
    \ import BootstrappedFoldableQueue\n\n\ndef main():\n    n, l = map(int, input().split())\n\
    \    a = list(map(int, input().split()))\n\n    bfq = BootstrappedFoldableQueue(min)\n\
    \    for i in range(l - 1):\n        bfq = bfq.snoc(a[i])\n\n    ans = []\n  \
    \  for i in range(l - 1, n):\n        bfq = bfq.snoc(a[i])\n        ans.append(bfq.all_fold())\n\
    \        bfq = bfq.tail()\n\n    print(*ans)\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - DataStructure/misc/BootstrappedFoldableQueue.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_3_D.BootstrappedFoldableQueue.test.py
  requiredBy: []
  timestamp: '2022-02-20 01:21:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_3_D.BootstrappedFoldableQueue.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_3_D.BootstrappedFoldableQueue.test.py
- /verify/TestCase/AOJ/DSL_3_D.BootstrappedFoldableQueue.test.py.html
title: TestCase/AOJ/DSL_3_D.BootstrappedFoldableQueue.test.py
---
