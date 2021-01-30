---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith:
  - icon: ':x:'
    path: TestCase/yukicoder/yuki0649.SortedMultiSetBIT.test.py
    title: TestCase/yukicoder/yuki0649.SortedMultiSetBIT.test.py
  - icon: ':x:'
    path: TestCase/yukicoder/yuki1110.SortedMultiSetBIT.test.py
    title: TestCase/yukicoder/yuki1110.SortedMultiSetBIT.test.py
  _isVerificationFailed: true
  _pathExtension: py
  _verificationStatusIcon: ':x:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n  File \"/opt/hostedtoolcache/Python/3.9.1/x64/lib/python3.9/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "from DataStructure.OrderedSet.SortedSetBIT import SortedSetBIT\n\n\nclass\
    \ SortedMultiSetBIT(SortedSetBIT):\n    def __init__(self, cands):\n        super().__init__(cands)\n\
    \n    def add(self, val):\n        i = self.comp[val] + 1\n        while i <=\
    \ self.size:\n            self.bit[i] += 1\n            i += i & -i\n        self.cnt\
    \ += 1\n        return True\n"
  dependsOn: []
  isVerificationFile: false
  path: DataStructure/SortedSet/SortedMultiSetBIT.py
  requiredBy: []
  timestamp: '2021-01-30 18:34:52+09:00'
  verificationStatus: LIBRARY_ALL_WA
  verifiedWith:
  - TestCase/yukicoder/yuki0649.SortedMultiSetBIT.test.py
  - TestCase/yukicoder/yuki1110.SortedMultiSetBIT.test.py
documentation_of: DataStructure/SortedSet/SortedMultiSetBIT.py
layout: document
redirect_from:
- /library/DataStructure/SortedSet/SortedMultiSetBIT.py
- /library/DataStructure/SortedSet/SortedMultiSetBIT.py.html
title: DataStructure/SortedSet/SortedMultiSetBIT.py
---
