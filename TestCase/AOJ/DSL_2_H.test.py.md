---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\SegmentTree\RmQ_RAQ.py
    title: RmQ_RAQ
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_H
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_H
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_H\r\
    \nimport sys\r\ninput = sys.stdin.buffer.readline\r\n\r\nfrom DataStructure.SegmentTree.RmQ_RAQ\
    \ import RmQ_RAQ\r\n\r\n\r\ndef main():\r\n    n, q = map(int, input().split())\r\
    \n    queries = [list(map(int, input().split())) for i in range(q)]\r\n\r\n  \
    \  lst = RmQ_RAQ(n)\r\n    ans = []\r\n    for flag, *query in queries:\r\n  \
    \      if flag == 0:\r\n            l, r, x = query\r\n            r += 1\r\n\
    \            lst.range_apply(l, r, x)\r\n        else:\r\n            l, r = query\r\
    \n            r += 1\r\n            ans.append(lst.fold(l, r))\r\n\r\n    print('\\\
    n'.join(map(str, ans)))\r\n\r\n\r\nif __name__ == '__main__':\r\n    main()\r\n"
  dependsOn:
  - DataStructure\SegmentTree\RmQ_RAQ.py
  isVerificationFile: true
  path: TestCase\AOJ\DSL_2_H.test.py
  requiredBy: []
  timestamp: '2021-01-02 18:15:11+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase\AOJ\DSL_2_H.test.py
layout: document
redirect_from:
- /verify\TestCase\AOJ\DSL_2_H.test.py
- /verify\TestCase\AOJ\DSL_2_H.test.py.html
title: TestCase\AOJ\DSL_2_H.test.py
---
