---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/Heap/PersistentLeftistHeap.py
    title: "\u4F75\u5408\u53EF\u80FD\u6C38\u7D9A\u30D2\u30FC\u30D7 (Persistent Leftist\
      \ Heap)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.6/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_C\n\
    import sys\ninput = sys.stdin.readline\n\nfrom DataStructure.Heap.PersistentLeftistHeap\
    \ import LeftistHeap\n\n\ndef main():\n    lh = LeftistHeap()\n    ans = []\n\
    \    while True:\n        a = input()\n        if a[0] == \"i\":\n           \
    \ lh = lh.insert(-int(a[7:]), None)\n        elif a[2] == \"t\":\n           \
    \ res, _ = lh.find_min\n            lh = lh.delete_min()\n            ans.append(-res)\n\
    \        else:\n            break\n\n    print(\"\\n\".join(map(str, ans)))\n\n\
    \nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/Heap/PersistentLeftistHeap.py
  isVerificationFile: true
  path: TestCase/AOJ/ALDS1_9_C.PersistentLeftistHeap.test.py
  requiredBy: []
  timestamp: '2022-01-20 19:40:17+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ALDS1_9_C.PersistentLeftistHeap.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ALDS1_9_C.PersistentLeftistHeap.test.py
- /verify/TestCase/AOJ/ALDS1_9_C.PersistentLeftistHeap.test.py.html
title: TestCase/AOJ/ALDS1_9_C.PersistentLeftistHeap.test.py
---
