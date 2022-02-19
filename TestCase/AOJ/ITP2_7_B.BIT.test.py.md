---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/SortedSet/SortedSetBIT.py
    title: "\u9806\u5E8F\u4ED8\u304D\u96C6\u5408 (Binary Indexed Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.2/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_B\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.SortedSet.SortedSetBIT\
    \ import SortedSetBIT\n\n\ndef main():\n    # __len__, __contains__, add, remove\n\
    \    q = int(input())\n    queries = [list(map(int, input().split())) for _ in\
    \ range(q)]\n\n    cands = [x for flag, x in queries if flag == 0]\n    sset =\
    \ SortedSetBIT(cands)\n    ans = []\n    for flag, x in queries:\n        if flag\
    \ == 0:\n            sset.add(x)\n            ans.append(len(sset))\n        elif\
    \ flag == 1:\n            ans.append(int(x in sset))\n        else:\n        \
    \    sset.remove(x)\n\n    print(\"\\n\".join(map(str, ans)))\n\n\nif __name__\
    \ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/SortedSet/SortedSetBIT.py
  isVerificationFile: true
  path: TestCase/AOJ/ITP2_7_B.BIT.test.py
  requiredBy: []
  timestamp: '2021-02-06 18:04:37+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ITP2_7_B.BIT.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ITP2_7_B.BIT.test.py
- /verify/TestCase/AOJ/ITP2_7_B.BIT.test.py.html
title: TestCase/AOJ/ITP2_7_B.BIT.test.py
---
