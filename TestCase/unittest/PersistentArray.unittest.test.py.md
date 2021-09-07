---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure/misc/PersistentArray.py
    title: "\u6C38\u7D9A\u914D\u5217"
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    PROBLEM: http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
    links:
    - http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.6/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "# verification-helper: PROBLEM http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ITP1_1_A\n\
    import sys\ninput = sys.stdin.buffer.readline\n\nfrom DataStructure.misc.PersistentArray\
    \ import (\n    PersistentArray,\n    init_persistent_array\n)\n\n\ndef main():\n\
    \    n = 100\n    arr = [-1] * n\n    per_arr = init_persistent_array(arr)\n\n\
    \    versions = [per_arr]\n    for i in range(n):\n        per_arr = versions[-1].set(i,\
    \ i)\n        versions.append(per_arr)\n\n    for i in range(n + 1):\n       \
    \ per_arr = versions[i]\n        for j in range(n):\n            if j < i:\n \
    \               assert(per_arr.get(j) == j)\n            else:\n             \
    \   assert(per_arr.get(j) == -1)\n\n\nif __name__ == '__main__':\n    main()\n\
    \    print(\"Hello World\")\n"
  dependsOn:
  - DataStructure/misc/PersistentArray.py
  isVerificationFile: true
  path: TestCase/unittest/PersistentArray.unittest.test.py
  requiredBy: []
  timestamp: '2021-09-08 02:11:43+09:00'
  verificationStatus: TEST_ACCEPTED
  verifiedWith: []
documentation_of: TestCase/unittest/PersistentArray.unittest.test.py
layout: document
redirect_from:
- /verify/TestCase/unittest/PersistentArray.unittest.test.py
- /verify/TestCase/unittest/PersistentArray.unittest.test.py.html
title: TestCase/unittest/PersistentArray.unittest.test.py
---
