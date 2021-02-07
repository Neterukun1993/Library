---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/SortedSet/SortedMultiSetBTree.py
    title: "\u9806\u5E8F\u4ED8\u304D\u591A\u91CD\u96C6\u5408 (B-Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_D
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_D
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_D\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.SortedSet.SortedMultiSetBTree\
    \ import SortedMultiSetBTree\n\n\ndef main():\n    # __len__, add, remove, iterate\n\
    \    q = int(input())\n    queries = [list(map(int, input().split())) for _ in\
    \ range(q)]\n\n    ssbt = SortedMultiSetBTree()\n    cnts = {}\n    ans = []\n\
    \    for flag, *query in queries:\n        if flag == 0:\n            x = query[0]\n\
    \            ssbt.add(x)\n            cnts[x] = cnts.get(x, 0) + 1\n         \
    \   ans.append(len(ssbt))\n        elif flag == 1:\n            x = query[0]\n\
    \            cnts[x] = cnts.get(x, 0)\n            ans.append(cnts[x])\n     \
    \   elif flag == 2:\n            x = query[0]\n            cnts[x] = cnts.get(x,\
    \ 0)\n            for _ in range(cnts[x]):\n                ssbt.remove(x)\n \
    \           cnts[x] = 0\n        else:\n            vl, vr = query\n         \
    \   for val in ssbt.iterate(vl):\n                if val <= vr:\n            \
    \        ans.append(val)\n                else:\n                    break\n\n\
    \    print(\"\\n\".join(map(str, ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/SortedSet/SortedMultiSetBTree.py
  isVerificationFile: true
  path: TestCase/AOJ/ITP2_7_D.BTree.test.py
  requiredBy: []
  timestamp: '2021-02-07 17:33:17+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ITP2_7_D.BTree.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ITP2_7_D.BTree.test.py
- /verify/TestCase/AOJ/ITP2_7_D.BTree.test.py.html
title: TestCase/AOJ/ITP2_7_D.BTree.test.py
---
