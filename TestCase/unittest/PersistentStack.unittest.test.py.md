---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/misc/PersistentStack.py
    title: "\u6C38\u7D9A Stack"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.misc.PersistentStack\
    \ import PersistentStack\n\n\ndef main():\n    n = 10\n    ps = PersistentStack()\n\
    \    versions = [ps]\n\n    for i in range(n):\n        ps = versions[-1].push(i)\n\
    \        versions.append(ps)\n\n    for i in range(n + 1):\n        ps = versions[i]\n\
    \        for j in reversed(range(i)):\n            assert(ps.top() == j)\n   \
    \         ps = ps.pop()\n        assert(ps.top() is None)\n\n\nif __name__ ==\
    \ '__main__':\n    main()\n    print(\"Hello World\")\n"
  dependsOn:
  - DataStructure/misc/PersistentStack.py
  isVerificationFile: true
  path: TestCase/unittest/PersistentStack.unittest.test.py
  requiredBy: []
  timestamp: '2021-09-08 02:11:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/PersistentStack.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/PersistentStack.unittest.test.py
- /verify/TestCase/unittest/PersistentStack.unittest.test.py.html
title: TestCase/unittest/PersistentStack.unittest.test.py
---
