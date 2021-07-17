---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/misc/LazyBinaryTrie.py
    title: "\u9045\u5EF6\u8A55\u4FA1 Binary Trie"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP2_7_C\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.misc.LazyBinaryTrie\
    \ import LazyBinaryTrie\n\n\ndef main():\n    # __len__, __contains__, add, remove,\
    \ kth_smallest, bisect_left, bisect_right\n    q = int(input())\n    queries =\
    \ [list(map(int, input().split())) for _ in range(q)]\n\n    lbt = LazyBinaryTrie()\n\
    \    ans = []\n    for flag, *query in queries:\n        if flag == 0:\n     \
    \       x = query[0]\n            lbt.add(x)\n            ans.append(len(lbt))\n\
    \        elif flag == 1:\n            x = query[0]\n            ans.append(int(x\
    \ in lbt))\n        elif flag == 2:\n            x = query[0]\n            lbt.remove(x)\n\
    \        else:\n            vl, vr = query\n            l = lbt.bisect_left(vl)\n\
    \            r = lbt.bisect_right(vr)\n            for i in range(l, r):\n   \
    \             ans.append(lbt.kth_smallest(i))\n\n    print(\"\\n\".join(map(str,\
    \ ans)))\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/misc/LazyBinaryTrie.py
  isVerificationFile: true
  path: TestCase/AOJ/ITP2_7_C.LazyBinaryTrie.test.py
  requiredBy: []
  timestamp: '2021-06-19 15:29:27+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ITP2_7_C.LazyBinaryTrie.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ITP2_7_C.LazyBinaryTrie.test.py
- /verify/TestCase/AOJ/ITP2_7_C.LazyBinaryTrie.test.py.html
title: TestCase/AOJ/ITP2_7_C.LazyBinaryTrie.test.py
---
