---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/misc/LazyBinaryTrie.py
    title: "\u9045\u5EF6\u8A55\u4FA1 Binary Trie"
  - icon: ':heavy_check_mark:'
    path: misc/xorshift.py
    title: "\u4E71\u6570\u751F\u6210 (Xorshift)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.7/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.misc.LazyBinaryTrie\
    \ import LazyBinaryTrie\nfrom misc.xorshift import xorshift32\n\n\ndef main():\n\
    \    rand32 = xorshift32()\n    lbt = LazyBinaryTrie()\n    s = set()\n\n    for\
    \ _ in range(10000):\n        # add\n        val = rand32()\n        lbt.add(val)\n\
    \        s.add(val)\n\n        # all_xor\n        val = rand32()\n        lbt.all_xor(val)\n\
    \        s = set(v ^ val for v in s)\n\n        # get_xor_min\n        val = rand32()\n\
    \        ans1 = lbt.get_xor_min(val)\n        ans2 = min(v ^ val for v in s)\n\
    \        assert(ans1 == ans2)\n\n\nif __name__ == '__main__':\n    main()\n  \
    \  print(\"Hello World\")\n"
  dependsOn:
  - DataStructure/misc/LazyBinaryTrie.py
  - misc/xorshift.py
  isVerificationFile: true
  path: TestCase/unittest/LazyBinaryTrie.unittest.test.py
  requiredBy: []
  timestamp: '2021-06-19 15:29:27+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/LazyBinaryTrie.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/LazyBinaryTrie.unittest.test.py
- /verify/TestCase/unittest/LazyBinaryTrie.unittest.test.py.html
title: TestCase/unittest/LazyBinaryTrie.unittest.test.py
---
