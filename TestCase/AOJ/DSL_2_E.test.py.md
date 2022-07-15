---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/BinaryIndexedTree/RangeAddPointGet.py
    title: "\u533A\u9593\u52A0\u7B97\u30FB\u4E00\u70B9\u53D6\u5F97"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_E
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_E
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.10.5/x64/lib/python3.10/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=DSL_2_E\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.BinaryIndexedTree.RangeAddPointGet\
    \ import BinaryIndexedTree\n\n\ndef main():\n    n, q = map(int, input().split())\n\
    \    queries = [list(map(int, input().split())) for i in range(q)]\n\n    bit\
    \ = BinaryIndexedTree(n)\n\n    ans = []\n    for flag, *query in queries:\n \
    \       if flag == 0:\n            l, r, x = query\n            l -= 1\n     \
    \       bit.add(l, r, x)\n        else:\n            i = query[0] - 1\n      \
    \      ans.append(bit[i])\n\n    print('\\n'.join(map(str, ans)))\n\n\nif __name__\
    \ == '__main__':\n    main()\n"
  dependsOn:
  - DataStructure/BinaryIndexedTree/RangeAddPointGet.py
  isVerificationFile: true
  path: TestCase/AOJ/DSL_2_E.test.py
  requiredBy: []
  timestamp: '2021-01-02 01:31:17+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/AOJ/DSL_2_E.test.py
layout: document
redirect_from:
- /verify/TestCase/AOJ/DSL_2_E.test.py
- /verify/TestCase/AOJ/DSL_2_E.test.py.html
title: TestCase/AOJ/DSL_2_E.test.py
---
