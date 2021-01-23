---
data:
  _extendedDependsOn:
  - icon: ':heavy_check_mark:'
    path: DataStructure\BinaryIndexedTree\PointAddRangeSum.py
    title: "\u4E00\u70B9\u52A0\u7B97\u30FB\u533A\u9593\u548C\u53D6\u5F97"
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':heavy_check_mark:'
    path: TestCase\AOJ\ALDS1_5_D.test.py
    title: TestCase\AOJ\ALDS1_5_D.test.py
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':heavy_check_mark:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"c:\\hostedtoolcache\\\
    windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\documentation\\\
    build.py\", line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"c:\\\
    hostedtoolcache\\windows\\python\\3.9.1\\x64\\lib\\site-packages\\onlinejudge_verify\\\
    languages\\python.py\", line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.BinaryIndexedTree.PointAddRangeSum import BinaryIndexedTree\r\
    \n\r\n\r\ndef inversion_number(array):\r\n    comp = {val: i for i, val in enumerate(sorted(set(array)))}\r\
    \n    for i, val in enumerate(array):\r\n        array[i] = comp[val]\r\n    max_val\
    \ = max(array)\r\n    bit = BinaryIndexedTree(max_val + 1)\r\n    inv_num = 0\r\
    \n    for i in array:\r\n        bit.add(i, 1)\r\n        inv_num += bit.sum(i\
    \ + 1, max_val + 1)\r\n    return inv_num\r\n"
  dependsOn:
  - DataStructure\BinaryIndexedTree\PointAddRangeSum.py
  isVerificationFile: false
  path: DataStructure\BinaryIndexedTree\inversion_number.py
  requiredBy: []
  timestamp: '2021-01-02 16:13:46+09:00'
  verificationStatus: LIBRARY_ALL_AC
  verifiedWith:
  - TestCase\AOJ\ALDS1_5_D.test.py
documentation_of: DataStructure\BinaryIndexedTree\inversion_number.py
layout: document
redirect_from:
- /library\DataStructure\BinaryIndexedTree\inversion_number.py
- /library\DataStructure\BinaryIndexedTree\inversion_number.py.html
title: DataStructure\BinaryIndexedTree\inversion_number.py
---
