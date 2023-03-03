---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: Graph/misc/DigraphDFSTree.py
    title: "\u6709\u5411\u30B0\u30E9\u30D5\u306EDFS\u6728\u306E\u69CB\u7BC9"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.2/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_11_B\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom Graph.misc.DigraphDFSTree\
    \ import DigraphDFSTree\n\n\ndef main():\n    n = int(input())\n    info = [list(map(int,\
    \ input().split())) for i in range(n)]\n\n    dfst = DigraphDFSTree(n)\n    for\
    \ v, k, *nxt_vs in info:\n        v -= 1\n        for nxt_v in nxt_vs:\n     \
    \       nxt_v -= 1\n            dfst.add_edge(v, nxt_v)\n\n    dfst.build()\n\
    \    for i, (arr, dep) in enumerate(zip(dfst.arrival, dfst.depature)):\n     \
    \   print(i + 1, arr + 1, dep + 1)\n\n\nif __name__ == '__main__':\n    main()\n"
  dependsOn:
  - Graph/misc/DigraphDFSTree.py
  isVerificationFile: true
  path: TestCase/AOJ/ALDS1_11_B.test.py
  requiredBy: []
  timestamp: '2021-01-25 23:26:41+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/ALDS1_11_B.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/ALDS1_11_B.test.py
- /verify/TestCase/AOJ/ALDS1_11_B.test.py.html
title: TestCase/AOJ/ALDS1_11_B.test.py
---
