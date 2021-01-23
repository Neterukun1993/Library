---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\Heap\DAryHeap.py
    title: D-Ary Heap
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_C
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_C
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_9_C\r\
    \nimport sys\r\ninput = sys.stdin.readline\r\n\r\nfrom DataStructure.Heap.DAryHeap\
    \ import DAryHeap\r\n\r\n\r\ndef main():\r\n    hp = DAryHeap(D=8)\r\n    ans\
    \ = []\r\n    while True:\r\n        a = input()\r\n        if a[0] == \"i\":\r\
    \n            hp.push(-int(a[7:]))\r\n        elif a[2] == \"t\":\r\n        \
    \    ans.append(-hp.pop())\r\n        else:\r\n            break\r\n\r\n    print(\"\
    \\n\".join(map(str, ans)))\r\n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\
    \n"
  dependsOn:
  - DataStructure\Heap\DAryHeap.py
  isVerificationFile: true
  path: TestCase\AOJ\ALDS1_9_C.DAryHeap8.test.py
  requiredBy: []
  timestamp: '2021-01-15 07:30:33+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\ALDS1_9_C.DAryHeap8.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\ALDS1_9_C.DAryHeap8.test.py
- /verify\TestCase\AOJ\ALDS1_9_C.DAryHeap8.test.py.html
title: TestCase\AOJ\ALDS1_9_C.DAryHeap8.test.py
---
