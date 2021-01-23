---
data:
  _extendedDependsOn:
  - icon: ':x:'
    path: DataStructure/Heap/SkewHeap.py
    title: "\u4F75\u5408\u53EF\u80FD\u30D2\u30FC\u30D7 (Skew Heap)"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_C
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_C\n\
    import sys\ninput = sys.stdin.readline\n\nfrom DataStructure.Heap.SkewHeap import\
    \ SkewHeap\n\n\ndef main():\n    sh = SkewHeap()\n    ans = []\n    while True:\n\
    \        a = input()\n        if a[0] == \"i\":\n            sh.push(-int(a[7:]))\n\
    \        elif a[2] == \"t\":\n            ans.append(-sh.pop())\n        else:\n\
    \            break\n\n    print(\"\\n\".join(map(str, ans)))\n\n\nif __name__\
    \ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/Heap/SkewHeap.py
  isVerificationFile: true
  path: TestCase/AOJ/ALDS1_9_C.SkewHeap.test.py
  requiredBy: []
  timestamp: '2021-01-14 12:29:07+09:00'
  verificationStatus: TEST_WRONG_ANSWER
  verifiedWith: []
documentation_of: TestCase/AOJ/ALDS1_9_C.SkewHeap.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ALDS1_9_C.SkewHeap.test.py
- /verify/TestCase/AOJ/ALDS1_9_C.SkewHeap.test.py.html
title: TestCase/AOJ/ALDS1_9_C.SkewHeap.test.py
---
