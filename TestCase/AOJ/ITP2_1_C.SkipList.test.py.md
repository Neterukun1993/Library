---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/List/SkipList.py
    title: "\u5BFE\u6570\u6642\u9593\u30E9\u30F3\u30C0\u30E0\u30A2\u30AF\u30BB\u30B9\
      /\u633F\u5165/\u524A\u9664\u53EF\u80FD\u30EA\u30B9\u30C8 (\u30B9\u30AD\u30C3\
      \u30D7\u30EA\u30B9\u30C8)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_C\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.List.SkipList\
    \ import SkipList\n\n\ndef main():\n    q = int(input())\n    queries = [list(map(int,\
    \ input().split())) for i in range(q)]\n\n    sl = SkipList()\n    idx = 0\n\n\
    \    for i in range(q):\n        if queries[i][0] == 0:\n            _, x = queries[i]\n\
    \            sl.insert(idx, x)\n        elif queries[i][0] == 1:\n           \
    \ _, d = queries[i]\n            idx += d\n        else:\n            sl.delete(idx)\n\
    \n    for i, res in enumerate(sl.dump()):\n        assert(res == sl[i])\n    \
    \    print(res)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/List/SkipList.py
  isVerificationFile: true
  path: TestCase/AOJ/ITP2_1_C.SkipList.test.py
  requiredBy: []
  timestamp: '2022-01-23 04:17:44+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ITP2_1_C.SkipList.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ITP2_1_C.SkipList.test.py
- /verify/TestCase/AOJ/ITP2_1_C.SkipList.test.py.html
title: TestCase/AOJ/ITP2_1_C.SkipList.test.py
---