---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/List/UnrolledLinkedList.py
    title: "\u5BFE\u6570\u6642\u9593\u30E9\u30F3\u30C0\u30E0\u30A2\u30AF\u30BB\u30B9\
      /\u633F\u5165/\u524A\u9664\u53EF\u80FD\u30EA\u30B9\u30C8 (UnrolledLinkedList)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_C\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.List.UnrolledLinkedList\
    \ import UnrolledLinkedList\n\n\ndef main():\n    q = int(input())\n    queries\
    \ = [list(map(int, input().split())) for i in range(q)]\n\n    ull = UnrolledLinkedList()\n\
    \    size = 0\n    idx = 0\n\n    for i in range(q):\n        if queries[i][0]\
    \ == 0:\n            _, x = queries[i]\n            ull.insert(idx, x)\n     \
    \       size += 1\n            assert(size == len(ull))\n        elif queries[i][0]\
    \ == 1:\n            _, d = queries[i]\n            idx += d\n        else:\n\
    \            ull.delete(idx)\n            size -= 1\n            assert(size ==\
    \ len(ull))\n\n    res = []\n    for i, val in enumerate(ull.dump()):\n      \
    \  assert(val == ull[i])\n        res.append(val)\n\n    new_ull = UnrolledLinkedList()\n\
    \    for _ in range(len(ull)):\n        new_ull.insert(0, 0)\n    for i, val in\
    \ enumerate(res):\n        new_ull[i] = val\n\n    for i, val in enumerate(res):\n\
    \        assert(val == new_ull[i])\n        print(val)\n\n\nif __name__ == '__main__':\n\
    \    main()\n"
  dependsOn:
  - DataStructure/List/UnrolledLinkedList.py
  isVerificationFile: true
  path: TestCase/AOJ/ITP2_1_C.UnrolledLinkedList.test.py
  requiredBy: []
  timestamp: '2022-07-31 03:52:21+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ITP2_1_C.UnrolledLinkedList.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ITP2_1_C.UnrolledLinkedList.test.py
- /verify/TestCase/AOJ/ITP2_1_C.UnrolledLinkedList.test.py.html
title: TestCase/AOJ/ITP2_1_C.UnrolledLinkedList.test.py
---