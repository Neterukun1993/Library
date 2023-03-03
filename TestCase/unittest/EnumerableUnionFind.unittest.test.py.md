---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/UnionFind/EnumerableUnionFind.py
    title: Enumerable Union Find
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.UnionFind.EnumerableUnionFind\
    \ import EnumerableUnionFind\n\n\ndef test_initialize():\n    n = 10\n    euf\
    \ = EnumerableUnionFind(n)\n    for i in range(n):\n        group = euf.enumerate(i)\n\
    \        assert(len(group) == 1)\n        assert(group[0] == i )\n\n\ndef test_merge_and_enumerate():\n\
    \    n = 6\n    euf = EnumerableUnionFind(n)\n\n    # [0]\n    # [1, 2]\n    #\
    \ [3, 4, 5]\n    euf.merge(1, 2)\n    euf.merge(3, 4)\n    euf.merge(4, 5)\n\n\
    \    for i in (0, ):\n        group = euf.enumerate(i)\n        assert(len(group)\
    \ == 1)\n        assert(0 in group)\n\n    for i in (1, 2):\n        group = euf.enumerate(i)\n\
    \        assert(len(group) == 2)\n        assert(1 in group and 2 in group)\n\n\
    \    for i in (3, 4, 5):\n        group = euf.enumerate(i)\n        assert(len(group)\
    \ == 3)\n        assert(3 in group and 4 in group and 5 in group)\n\n    # [0,\
    \ 1, 2, 3, 4, 5]\n    euf.merge(0, 1)\n    euf.merge(2, 3)\n\n    for i in (0,\
    \ 1, 2, 3, 4, 5):\n        group = euf.enumerate(i)\n        assert(len(group)\
    \ == 6)\n        assert(0 in group and 1 in group and 2 in group)\n        assert(3\
    \ in group and 4 in group and 5 in group)\n\n\ndef main():\n    test_initialize()\n\
    \    test_merge_and_enumerate()\n\n\nif __name__ == '__main__':\n    main()\n\
    \    print(\"Hello World\")\n"
  dependsOn:
  - DataStructure/UnionFind/EnumerableUnionFind.py
  isVerificationFile: true
  path: TestCase/unittest/EnumerableUnionFind.unittest.test.py
  requiredBy: []
  timestamp: '2022-08-20 05:25:06+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/EnumerableUnionFind.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/EnumerableUnionFind.unittest.test.py
- /verify/TestCase/unittest/EnumerableUnionFind.unittest.test.py.html
title: TestCase/unittest/EnumerableUnionFind.unittest.test.py
---
