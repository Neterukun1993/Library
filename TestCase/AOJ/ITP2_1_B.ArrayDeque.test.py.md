---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/misc/ArrayDeque.py
    title: "\u4E21\u7AEF\u30AD\u30E5\u30FC (\u5FAA\u74B0\u30D0\u30C3\u30D5\u30A1/\u30E9\
      \u30F3\u30C0\u30E0\u30A2\u30AF\u30BB\u30B9$O(1)$)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_1_B\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.misc.ArrayDeque\
    \ import ArrayDeque\n\n\ndef main():\n    q = int(input())\n    queries = [list(map(int,\
    \ input().split())) for i in range(q)]\n\n    dq = ArrayDeque()\n    ans = []\n\
    \    for flag, *query in queries:\n        if flag == 0:\n            d, x = query\n\
    \            if d == 0:\n                dq.appendleft(x)\n            else:\n\
    \                dq.append(x)\n        elif flag == 1:\n            p = query[0]\n\
    \            ans.append(dq[p])\n        else:\n            d = query[0]\n    \
    \        if d == 0:\n                dq.popleft()\n            else:\n       \
    \         dq.pop()\n\n    print('\\n'.join(map(str, ans)))\n\n\nif __name__ ==\
    \ '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/misc/ArrayDeque.py
  isVerificationFile: true
  path: TestCase/AOJ/ITP2_1_B.ArrayDeque.test.py
  requiredBy: []
  timestamp: '2021-02-04 17:47:04+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ITP2_1_B.ArrayDeque.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ITP2_1_B.ArrayDeque.test.py
- /verify/TestCase/AOJ/ITP2_1_B.ArrayDeque.test.py.html
title: TestCase/AOJ/ITP2_1_B.ArrayDeque.test.py
---
