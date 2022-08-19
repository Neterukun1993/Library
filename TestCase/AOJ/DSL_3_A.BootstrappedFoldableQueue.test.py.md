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
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_3_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.misc.BootstrappedFoldableQueue\
    \ import BootstrappedFoldableQueue\n\n\ndef main():\n    n, s = map(int, input().split())\n\
    \    a = list(map(int, input().split()))\n\n    bfq = BootstrappedFoldableQueue(lambda\
    \ x, y: x + y)\n    ans = 10 ** 18\n    r = 0\n    for l in range(n):\n      \
    \  if not bfq:\n            bfq = bfq.snoc(a[r])\n            r += 1\n       \
    \ while r < n and bfq.all_fold() < s:\n            bfq = bfq.snoc(a[r])\n    \
    \        r += 1\n        if bfq.all_fold() >= s:\n            ans = min(r - l,\
    \ ans)\n        bfq = bfq.tail()\n\n    if ans == 10 ** 18:\n        print(0)\n\
    \    else:\n        print(ans)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/misc/BootstrappedFoldableQueue.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_3_A.BootstrappedFoldableQueue.test.py
  requiredBy: []
  timestamp: '2022-02-20 01:21:01+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_3_A.BootstrappedFoldableQueue.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_3_A.BootstrappedFoldableQueue.test.py
- /verify/TestCase/AOJ/DSL_3_A.BootstrappedFoldableQueue.test.py.html
title: TestCase/AOJ/DSL_3_A.BootstrappedFoldableQueue.test.py
---
