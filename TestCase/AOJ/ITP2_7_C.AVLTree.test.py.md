---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/SortedSet/SortedSetAVLTree.py
    title: "\u9806\u5E8F\u4ED8\u304D\u96C6\u5408 (AVL Tree)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.5/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_C\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.SortedSet.SortedSetAVLTree\
    \ import SortedSetAVLTree\n\n\ndef main():\n    # __len__, __contains__, add,\
    \ remove, iterate\n    q = int(input())\n    queries = [list(map(int, input().split()))\
    \ for _ in range(q)]\n\n    ssavl = SortedSetAVLTree()\n    ans = []\n    for\
    \ flag, *query in queries:\n        if flag == 0:\n            x = query[0]\n\
    \            ssavl.add(x)\n            ans.append(len(ssavl))\n        elif flag\
    \ == 1:\n            x = query[0]\n            ans.append(int(x in ssavl))\n \
    \       elif flag == 2:\n            x = query[0]\n            ssavl.remove(x)\n\
    \        else:\n            vl, vr = query\n            for val in ssavl.iterate(vl):\n\
    \                if val <= vr:\n                    ans.append(val)\n        \
    \        else:\n                    break\n\n    print(\"\\n\".join(map(str, ans)))\n\
    \n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/SortedSet/SortedSetAVLTree.py
  isVerificationFile: true
  path: TestCase/AOJ/ITP2_7_C.AVLTree.test.py
  requiredBy: []
  timestamp: '2021-05-13 01:21:14+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ITP2_7_C.AVLTree.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ITP2_7_C.AVLTree.test.py
- /verify/TestCase/AOJ/ITP2_7_C.AVLTree.test.py.html
title: TestCase/AOJ/ITP2_7_C.AVLTree.test.py
---
